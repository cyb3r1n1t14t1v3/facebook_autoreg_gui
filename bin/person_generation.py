import names
from random import choice, randint
from datetime import date, timedelta
from bin.manage_config import get_params, get_numpad

class Generation:
	def __init__(self):
		self.country_code = "+7"
		self.cellular_codes = [
			902, 922, 929, 934, 938,
			904, 923, 930, 936, 939,
			908, 924, 931, 937, 950,
			920, 925, 932, 938, 951,
			921, 926, 933, 939, 958,
			927, 934, 936, 950, 999,
			928, 936, 937, 951
		]

	@property
	def data_person(self) -> dict:
		gender = self.__gender_generate()
		full_name = self.__full_name_generate(gender = gender)
		return {
			"gender"    : gender,
			"full_name" : full_name
		}

	@property
	def password_person(self) -> str:
		return self.__password_generate()

	@property
	def number_person(self) -> str:
		return self.__number_generate()

	@property
	def birthdate_person(self) -> dict:
		return self.__birthdate_generate()

	def __gender_generate(self):
		return choice(['male', 'female'])

	def __full_name_generate(self, gender: str):
		return names.get_full_name(gender).split(" ")

	def __password_generate(self):
		return "".join([choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789%*()?@#$~-_') for i in range(max(6, get_params.password_length))])

	def __number_generate(self):
		return "{}{}{}".format(self.country_code, choice(self.cellular_codes), str(randint(1000000, 9999999)))

	def __birthdate_generate(self) -> dict:
		birth_date = self.__generate_birthdate(age=get_params.max_age)
		day = list(map(int, birth_date["day"]))
		month = list(map(int, birth_date["month"]))
		year = list(map(int, birth_date["year"]))

		if len(day) == 1: day.insert(0, 0)	
		if len(month) == 1: month.insert(0, 0)

		birthdate_cords = [
			get_numpad.cord_nums[num-1] for num in sum([day, month, year], [])
		]

		return {
			"birth_date" : ["".join(map(str, day)), "".join(map(str, month)), "".join(map(str, year))],
			"birthdate_cords" : birthdate_cords
		}

	def __generate_birthdate(self, age: int) -> dict:
		today = date.today()

		min_year = today.year - age - 1
		max_year = today.year - age

		year = randint(min_year, max_year)
		month = randint(1, 12)

		if month == 2:
			if self.__is_leap_year(year):
				day = randint(1, 29)
			else:
				day = randint(1, 28)
		elif month in [4, 6, 9, 11]:
			day = randint(1, 30)
		else:
			day = randint(1, 31)

		return {
			"day" : str(day),
			"month" : str(month),
			"year" : str(year)
		}

	def __is_leap_year(self, year) -> bool: 
		if year % 4 != 0:
			return False
		elif year % 100 != 0:
			return True
		elif year % 400 != 0:
			return False
		else:
			return True
