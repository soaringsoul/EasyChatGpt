
import requests
from loguru import logger
from PySide6 import QtCore
from PySide6.QtCore import *
from retrying import retry


class UpdateCheck(QtCore.QThread):
    result_signal = Signal(dict)
    finished_signal = Signal(str)
    error_signal = Signal(str)
    progress_signal = Signal(str)

    def __init__(self, current_verison):
        super(UpdateCheck, self).__init__()
        self.current_version = current_verison

    # 添加每次方法执行之间的等待时间
    @retry(stop_max_attempt_number=10, wait_fixed=3000)
    def get_cloud_settings_json(self):
        from configs.main_config import AppCloudSettingsUrl
        resq = requests.get(AppCloudSettingsUrl)
        return resq.json()

    def run(self):
        # 拉取云数据
        try:
            self.settings_json = self.get_cloud_settings_json()
            self.result_signal.emit(self.settings_json)
        except Exception as e:
            logger.info("拉取云端数据失败:", e)
        self.finished_signal.emit("已完成更新检测！")
