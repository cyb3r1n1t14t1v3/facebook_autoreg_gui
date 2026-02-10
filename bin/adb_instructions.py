import cv2
import numpy as np
# import pytesseract
import paddle
from paddleocr import PaddleOCR
from time import sleep
from bin.manage_config import get_delays, get_paths, get_attempts, get_params, set_numpad

class Instructions:
	def __init__(self, device):
		self.device = device
		self.facebook_pkg = "com.facebook.lite"
		self.img = np.array([])

	def __facebook_give_access(self):
		self.device.shell(f'pm grant {self.facebook_pkg} android.permission.CAMERA')
		self.device.shell(f'pm grant {self.facebook_pkg} android.permission.READ_CONTACTS')
		self.device.shell(f'pm grant {self.facebook_pkg} android.permission.READ_EXTERNAL_STORAGE')
		self.device.shell(f'pm grant {self.facebook_pkg} android.permission.WRITE_EXTERNAL_STORAGE')
		self.device.shell(f'pm grant {self.facebook_pkg} android.permission.CALL_PHONE')

	def __get_screen(self, color_type="B"):
		bimg = self.device.screencap()
		decoded = cv2.imdecode(np.frombuffer(bimg, np.uint8), -1)
		match color_type:
			case "B":
				self.img = cv2.cvtColor(decoded, cv2.COLOR_RGB2BGR)
			case "G":
				self.img = cv2.threshold(
						   cv2.cvtColor(decoded, cv2.COLOR_RGB2GRAY),
					0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
			case _:
				self.img = decoded

	def __uninstall_facebook(self):
		if self.device.is_installed(self.facebook_pkg):
			self.device.uninstall(self.facebook_pkg)

	def install_facebook(self) -> str:
		try:
			self.__uninstall_facebook()
			self.device.install(get_paths.facebook_apk)
			self.__facebook_give_access()

			sleep(get_delays.install_facebook)
		except FileNotFoundError:
			raise ValueError(f'Приложение \"{self.facebook_apk}\" не найдено.')

	def open_facebook(self):
		self.device.shell(f"monkey -p {self.facebook_pkg} 1")
		sleep(get_delays.open_facebook)

	def reopen_facebook(self):
		self.device.shell(f"am force-stop {self.facebook_pkg}");
		self.device.shell(f"monkey -p {self.facebook_pkg} 1")
		sleep(get_delays.open_facebook)

	def send_click_button(self, rgb):
		for _ in range(get_attempts.send_click):
			self.__get_screen()

			for y in range(len(self.img)):
				for x in range(0, y, get_params.sector_size):
					if x < len(self.img[y]):
						if (self.img[y][x] == rgb).all():
							self.device.input_tap(x, y)
							return x, y
			sleep(get_delays.send_click)
		else:
			return None

	def send_click_by_cords(self, x, y):
		self.device.input_tap(x, y)
		sleep(get_delays.send_click)

	def send_keys(self, string):
		self.device.input_text(string);
		sleep(get_delays.send_keys)

	def send_keyevent(self, code):
		self.device.shell(f"input keyevent {code}")
		sleep(get_delays.send_keys)

	def get_word(self, string, click=True, offset=0) -> tuple:
		# Получаем координаты нужного слова
		pytesseract.pytesseract.tesseract_cmd = get_paths.tesseractOCR
		for _ in range(get_attempts.get_word):
			self.__get_screen("G")

			# Получаем координаты каждой строки
			data = pytesseract.image_to_data(self.img, lang="eng", output_type=pytesseract.Output.DICT)
			for i in range(len(data['text'])):
				if int(data['conf'][i]) > 60 and string in data['text'][i]:
					if offset > 0:
						offset -= 1
						continue

					x = data['left'][i] + data['width'][i] / 2
					y = data['top'][i] + data['height'][i] / 2

					if click:
						self.send_click_by_cords(x, y)
					return x, y			

			sleep(get_delays.get_word)
		else:	
			return None	

	def load_numpad_to_cfg(self):
		numpad = [
			1, 2, 3,
			4, 5, 6,
			7, 8, 9,
			0
		]

		# Получаем координаты нужных цифр
		ocr = PaddleOCR(
			det_model_dir = get_paths.paddleOCR_det, det_algorithm = "DB",
			rec_model_dir = get_paths.paddleOCR_rec, rec_algorithm = "SVTR_LCNet",
			rec_char_type='en_number', max_text_length=1, show_log=False,
			rec_char_dict_path=get_paths.paddleOCR_digital_dict
		)
		for _ in range(get_attempts.get_word):
			self.__get_screen()

			cord_nums = []

			data = ocr.ocr(self.img)[0]
			for i, line in enumerate(data):
				text = line[1][0]; box = line[0]

				if text.isdigit():
					digit = int(text)

					if digit in numpad:
						cords = [box[0][0] - (box[0][0] - box[2][0]) / 2,  box[0][1] - (box[0][1] - box[2][1]) / 2]

						if cord_nums == []:
							if digit == 1:
								cord_nums.append(cords)
						else:
							if digit == len(cord_nums) + 1:
								cord_nums.append(cords)
							elif digit == 1 and len(cord_nums) == 1:
								continue
							elif len(cord_nums) == 9 and digit == 0:
								cord_nums.append(cords)
								break
							else:
								cord_nums.clear()
			else:
				cord_nums.clear()
				continue

			set_numpad.cord_nums(cord_nums)
			
			sleep(get_delays.get_word)
			return _
		else:
			return None