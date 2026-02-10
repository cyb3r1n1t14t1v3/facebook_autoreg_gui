import subprocess
from ppadb.client import Client as AdbClient
from bin.manage_config import get_paths

class Connection:
    def __init__(self):
        self.path_to_adb = get_paths.adb_folder

    @property
    def adb_launched(self):
        return True if self.__adb_launch() else False

    def get_dvs(self):
        if self.adb_launched:
            client = AdbClient(host="127.0.0.1", port=5037)
            devices = client.devices()
            dvs = list()

            for device in devices:
                dvs.append(client.device(device.serial))
            if not len(dvs):
                raise ValueError("ADB не нашел ни одного устройства.")
            return dvs
        else:
            raise ValueError(f"ADB не запущен. Проверьте указанный путь до ADB:\n{self.path_to_adb}")
                
    def __adb_launch(self):
        try:
            cmd = f"{self.path_to_adb}\\adb devices"
            return subprocess.run(cmd)
        except FileNotFoundError:
            return None