from os.path import abspath, join, dirname
from json import loads, dump

class EditConfig:
	def __init__(self):
		with open("config.json", "r", encoding="utf-8") as config_file:
			data = config_file.read()
			self.cfg = loads(data)

	def edit(self):
		with open('config.json', 'w', encoding="utf-8") as config_file:
			dump(self.cfg, config_file)

class EditNumpad(EditConfig):
	def __init__(self):
		super().__init__()

	def cord_nums(self, data):
		self.cfg['numpad']['cordNums'] = data
		self.edit()

class GetConfig:
	def __init__(self):
		with open("config.json", "r", encoding="utf-8") as config_file:
			data = config_file.read()
			self.cfg = loads(data)

class GetDelays(GetConfig):
	def __init__(self):
		super().__init__()
		self.dsdata = self.cfg["delays"]["data"]

	@property
	def install_facebook(self):
		return self.dsdata["installFacebook"]

	@property
	def open_facebook(self):
		return self.dsdata["openFacebook"]

	@property
	def send_click(self):
		return self.dsdata["sendClick"]

	@property
	def send_keys(self):
		return self.dsdata["sendKeys"]

	@property
	def get_word(self):
		return self.dsdata["getWord"]

	@property
	def get_confirm_url(self):
		return self.dsdata["getConfirmURL"]

class GetPaths(GetConfig):
	def __init__(self):
		super().__init__()
		self.psdata = self.cfg["paths"]["data"]

	@property
	def adb_folder(self):
		return abspath(join(dirname(__file__), self.psdata["adbFolder"]))

	@property
	def facebook_apk(self):
		return abspath(join(dirname(__file__), self.psdata["facebookAPK"]))

	@property
	def chromedriver(self):
		return abspath(join(dirname(__file__), self.psdata["chromeDriverEXE"]))

	@property
	def tesseractOCR(self):
		return abspath(join(dirname(__file__), self.psdata["tesseractOcrEXE"]))

	@property
	def emails_txt(self):
		return abspath(join(dirname(__file__), self.psdata["emailsTXT"]))

	@property
	def paddleOCR_det(self):
		return abspath(join(dirname(__file__), self.psdata["PaddleOcrDetFolder"]))

	@property
	def paddleOCR_rec(self):
		return abspath(join(dirname(__file__), self.psdata["PaddleOcrRecFolder"]))

	@property
	def paddleOCR_digital_dict(self):
		return abspath(join(dirname(__file__), self.psdata["PaddleOcrDigitalDictTXT"]))

class GetAttempts(GetConfig):
	def __init__(self):
		super().__init__()
		self.asdata = self.cfg["attempts"]["data"]

	@property
	def send_click(self):
		return self.asdata["sendClick"]

	@property
	def get_word(self):
		return self.asdata["getWord"]
		
	@property
	def get_confirm_url(self):
		return self.asdata["getConfirmURL"]

class GetParams(GetConfig):
	def __init__(self):
		super().__init__()
		self.psdata = self.cfg["params"]["data"]

	@property
	def sector_size(self):
		return self.psdata["sectorSize"]

	@property
	def password_length(self):
		return self.psdata["passwordLength"]

	@property
	def max_age(self):
		return self.psdata["maxAge"]

	@property
	def webdriver_implict_wait(self):
		return self.psdata["webDriverImplictWait"]

class GetNumpad(GetConfig):
	def __init__(self):
		super().__init__()
		self.numpad = self.cfg["numpad"]

	@property
	def cord_nums(self):
		return self.numpad["cordNums"]

class GetProxy(GetConfig):
	def __init__(self):
		super().__init__()
		self.pdata = self.cfg["proxy"]["data"]

	@property
	def type(self):
		return self.pdata["type"]

	@property
	def username(self):
		return self.pdata["username"]

	@property
	def password(self):
		return self.pdata["password"]

	@property
	def hostname(self):
		return self.pdata["hostname"]

	@property
	def port(self):
		return self.pdata["port"]

set_numpad = EditNumpad()

get_delays = GetDelays()
get_paths = GetPaths()
get_attempts = GetAttempts()
get_params = GetParams()
get_numpad = GetNumpad()
get_proxy = GetProxy()