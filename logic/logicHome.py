# -*- coding: utf-8 -*-


import os

from app_config import APPIconPath

from qt_tools.import_qt_module import *
from ui.qt6_ui.Ui_homepage import Ui_HomePageMainWindow
from app_config import AppSettings


class HomePageMainWindow(QtWidgets.QMainWindow, Ui_HomePageMainWindow):
    switch_window = Signal(str)
    error_signal = Signal(str)
    app_settings = AppSettings

    def __init__(self, root_path=os.getcwd()):
        super(HomePageMainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon(APPIconPath))
        self.root_path = root_path
        self.load_and_save_configs()
        self.init_sign()
        self.init_data()

    def load_and_save_configs(self, option='load'):
        for lineEdit in []:
            if option == "load":
                lineEdit.setText(self.app_settings.value(lineEdit.objectName()))
            else:
                self.app_settings.setValue(lineEdit.objectName(), lineEdit.text())

    def init_sign(self):
        pass

    def init_data(self):
        home_url = 'https://mp.weixin.qq.com/mp/appmsgalbum?__biz=Mzg2MTY3Nzg1Nw==&action=getalbum&album_id=2169138775514284035'
        self.webview.load(QUrl(home_url))


if __name__ == "__main__":
    import sys, os

    app = QApplication(sys.argv)
    gui = HomePageMainWindow()
    gui.show()
    sys.exit(app.exec())
