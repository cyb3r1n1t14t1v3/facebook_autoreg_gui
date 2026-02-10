import imaplib
import quopri
import re
from json import dumps
from base64 import b64encode
from seleniumwire import webdriver
from time import sleep
from bin.manage_config import get_delays, get_paths, get_attempts, get_proxy, get_params

class EmailManager(BaseManager):
    def __init__(self):
        self.email_data = list()

    @property
    def get_email_data(self) -> list:
        with open(get_paths.emails_txt, "r") as ems: 
            lines = ems.readlines()  
            self.email_data = lines[0].strip().split(":")[:2]
            print(self.email_data)
            del lines[0]

        with open(get_paths.emails_txt, "w") as ems:
            ems.writelines(lines)

        return self.email_data

    @property
    def get_confirm_url(self) -> str:
        with imaplib.IMAP4_SSL('imap.rambler.ru', port=993) as mail:
            mail.login(self.email_data[0], self.email_data[1])
            mail.select("inbox")

            for _ in range(get_attempts.get_confirm_url):
                try:
                    id = mail.search(None, 'FROM "registration@facebookmail.com"')[1][0].split()[0]
                except:
                    sleep(get_delays.get_confirm_url)
                else:
                    result, data = mail.fetch(id, '(BODY[0])')
                    if result == "OK":
                        self.confirm_url = quopri.decodestring(data[0][1]).decode('utf-8').split("\r\n")[2]
                        return self.confirm_url
            else:
                pass

class WebDriverManager(BaseManager):
    def __init__(self):
        self.confirm_url = "https://www.facebook.com/n/?confirmemail.php&e=arianna.arnold.982406\%40ro.ru&c=28263&cuid=AYgW5HefTzaZW0vfoI2XVJtzTvcsD3p8EjlcD0lAq_4VOlIZWzUEv5ApNbI-4QdYKcuhzNa5d1EEcjQv6xdmGALu7qkwymHZ9MCJ1pGSN2enz1CPaZirTfZqHCEC_Cpxc2A&aref=1684337785684121&medium=email&mid=5fbe529cfbdc7G5b08a4c4c2f5G5fbe57365c099G3c2&bcode=2.1684337785.Abwh0B0Tw-WaY0IQGHg&n_m=arianna.arnold.982406\%40ro.ru"

        options_wire = {
            'proxy': {
                'http': f'{get_proxy.type}://{get_proxy.username}:{get_proxy.password}@{get_proxy.hostname}:{get_proxy.port}',
                'https': f'{get_proxy.type}://{get_proxy.username}:{get_proxy.password}@{get_proxy.hostname}:{get_proxy.port}',
                'no_proxy': 'localhost,127.0.0.1',
            },
        }

        options = webdriver.ChromeOptions()
        options.add_argument("--log-level=3")
        options.add_argument('--no-sandbox')
        options.add_argument("--ignore-certificate-errors")
        options.add_argument('--ignore-certificate-errors-spki-list')
        options.add_argument('--ignore-ssl-errors')

        self.driver = webdriver.Chrome(seleniumwire_options=options_wire, options=options, executable_path=get_paths.chromedriver)
        self.driver.implicitly_wait(get_params.webdriver_implict_wait)

    def __connect_to_url(self, url):
        

    @property
    def get_cookies(self) -> str:
        self.driver.get(self.confirm_url)
        cs = self.driver.get_cookies()
        return b64encode(dumps(cs).encode('utf-8')).decode('utf-8')

    @property
    def get_user_id(self) -> str:
        self.driver.get(self.confirm_url)
        return re.findall(r'"(?:ACCOUNT_ID|USER_ID)":"(\d+)"', self.driver.page_source)[0]