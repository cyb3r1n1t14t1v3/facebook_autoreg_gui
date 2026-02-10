import threading
from bin.__init__ import *

class StartAutoReg:
	def __init__(self, device):
		self.con = Connection()
		self.inst = Instructions(device=device)
		self.gen = Generation()
		self.emm = EmailManager()
		self.wdm = WebDriverManager()

		self.button_color = {
			"green" : [49, 162, 76],
			"blue"  : [27, 116, 228]
		}

	def start(self):
		# #Установка facebook-lite
		# self.inst.install_facebook()
		# self.inst.open_facebook()

		# #Смена языка на английский
		# self.inst.get_word("English")
		# self.inst.send_click_button(self.button_color["green"])

		# self.inst.send_click_button(self.button_color["blue"])

		# data_person = self.gen.data_person
		# # Ввод имени и фамилии
		# first_name, last_name = data_person["full_name"]
		# if self.inst.get_word("name", False):
		# 	self.inst.send_keys(first_name)
		# 	self.inst.send_keyevent(code = 61)
		# 	self.inst.send_keys(last_name)
		# 	self.inst.send_click_button(self.button_color["blue"])

		# # Ввод номера телефона
		# number = self.gen.number_person
		# if self.inst.get_word("number", False):
		# 	self.inst.send_keyevent(code = 61)
		# 	self.inst.send_keys(number)
		# 	self.inst.send_click_button(self.button_color["blue"])

		# # Выбор даты рождения
		# if self.inst.get_word("birth", False):
		# 	# self.inst.load_numpad_to_cfg()

		# 	birthdate = self.gen.birthdate_person
		# 	for cords in birthdate['birthdate_cords']:
		# 		self.inst.send_click_by_cords(cords[0], cords[1])
		# 	self.inst.send_click_button(self.button_color["blue"])

		# # Выбор гендера
		# gender = data_person["gender"]
		# if self.inst.get_word("gender", False):
		# 	for i in range(2 if gender == "male" else 1):
		# 		self.inst.send_keyevent(code = 61)
		# 	self.inst.send_keyevent(code = 66)

		# # Ввод пароля
		# password = self.gen.password_person	
		# if self.inst.get_word("password", False):
		# 	self.inst.send_keys(password)
		# 	self.inst.send_click_button(self.button_color["blue"])

		# self.inst.send_click_button(self.button_color["blue"])

		# # Проверка регистрации
		# if self.inst.get_word("login", False):
		# 	self.inst.reopen_facebook()

		# # Ввод почты
		# self.inst.get_word("email")
		# if self.inst.get_word("email", False):
		# 	for i in range(2):
		# 		self.inst.send_keyevent(code = 61)
		# 	self.inst.send_keyevent(code = 66)
		# 	self.inst.send_keys(self.emm.get_email_data[0])
		# 	print(password)
		# 	self.inst.send_click_button(self.button_color["blue"])
		# 	print(self.emm.get_confirm_url)
		print(self.wdm.get_cookies)	
		print(self.wdm.get_user_id)

def core(device):
	sar = StartAutoReg(device=device)
	sar.start()

if __name__ == "__main__":
	threads_num = 1
	devices = Connection().get_dvs()

	core(devices[0])

	# threads = [threading.Thread(target=core, args=(device,)) for device in devices]
	# for thread in threads:
	# 	thread.start()

	# for thread in threads:
	# 	thread.join()

