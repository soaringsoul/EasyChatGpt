# encoding = utf-8
# =====================================================
#   Copyright (C) 2021 All rights reserved.
#   author   : gongzi.xu / 95168339@qq.com
#   date     : 2021/01/09
# =====================================================

from loguru import logger
import os
from ui.qt6_ui.images_rc import *
import webbrowser

from PySide6 import QtCore, QtWidgets
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *

from splash import SplashScreen
from functools import partial
from settings_json import app_settings_json as settings_json

from tools.custom_QMessageBox import MyQMessageBox

is_mysql_enabled = False

from ui.qt6_ui.Ui_main_page import Ui_MainWindow
from app_config import AppName, AppVersion, AppConfigDir
from qt_tools.UiToggleFunctions import UIFunctions


class RwbAppLogicMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    from app_config import AppSettings

    app_settings = AppSettings
    switch_window = Signal()
    close_window = Signal()
    chooseSignal = Signal(str)

    def __init__(self, root_path):
        super(RwbAppLogicMainWindow, self).__init__()
        self.setupUi(self)
        self.showMaximized()
        self.settings_json = settings_json
        self.root_path = root_path

        # 保存配置项时是否弹窗提示标识 ，若为保存按钮触发有弹窗，否则无弹窗

        self.setWindowTitle("%s_v%s" % (AppName, AppVersion))
        self.init_themes()
        self.init_sign()

        # 初始化数据
        self.init_data()
        # 初始化信号

        self.init_logic_guis()
        self.init_toggle_gui()



    def init_data(self):
        self.df_current_result = None
        from logic.workers.update_check import UpdateCheck
        self.btn_home.click()
        self.read_chatgpt_prompt_json()

    def read_chatgpt_prompt_json(self):
        import json
        with open('awesome_prompts/rwb_prompts.json') as f:
            self.prompt_dict = json.load(f)

        self.listWidget_act_cn.addItems(self.prompt_dict['cn'].keys())
        self.listWidget_act_en.addItems(self.prompt_dict['en'].keys())

    def init_sign(self):
        self.listWidget_act_cn.itemClicked.connect(self.show_clicked_item)
        self.listWidget_act_en.itemClicked.connect(self.show_clicked_item)
        # 打开导出数据前的设置界面

        self.btn_settings.clicked.connect(self.openCloseLeftBox)
        self.btn_home.clicked.connect(self.buttonClick)
        self.pushButton_copy.clicked.connect(self.copy_to_clipboard)

        # 设置菜单栏信号
        self.action_about.triggered.connect(partial(self.visit_urls, 'about'))
        self.action_help.triggered.connect(partial(self.visit_urls, 'help'))

    def open_webview_url_in_chrome(self):
        url = self.webview.url().url()
        webbrowser.open(url)

    def init_logic_guis(self):
        pass

    def buttonClick(self):
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            self.stackedWidget.setCurrentWidget(self.page_home)
            home_url = 'https://chat.openai.com/'

            self.webview.load(QUrl(home_url))

            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            self.stackedWidget.setStyleSheet(self.qss_str)
        elif True:
            pass

    def init_themes(self):
        useCustomTheme = True
        themeFile = "themes/dark.qss"
        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            self.qss_str = open(themeFile, 'r', encoding='utf8').read()
            self.styleSheet.setStyleSheet(self.qss_str)

    def init_toggle_gui(self):
        # TOGGLE MENU
        self.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        self.extraCloseColumnBtn.clicked.connect(self.openCloseLeftBox)

    def openCloseLeftBox(self):
        UIFunctions.toggleLeftBox(self, True)

    def show_clicked_item(self):
        if self.tabWidget.currentIndex() == 0:
            items = self.listWidget_act_cn.selectedItems()
            item = items[0]
            self.show_progress(item.text())
            value = self.prompt_dict['cn'].get(item.text())
            self.textEdit_prompt.setText(value)
        else:
            items = self.listWidget_act_en.selectedItems()
            item = items[0]
            self.show_progress(item.text())
            value = self.prompt_dict['en'].get(item.text())
            self.textEdit_prompt.setText(value)

    def copy_to_clipboard(self):
        import pyperclip
        from datetime import datetime
        text = self.textEdit_prompt.toPlainText()
        pyperclip.copy(text)

        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        print(formatted_time)

        self.label_copy_info.setText('%s:已复制内容到剪贴板' % formatted_time)

    def open_file_dialog(self):
        fileName, fileType = QFileDialog.getOpenFileName(self,
                                                         "选择文件",
                                                         r"%s" % os.path.join(os.getcwd(), 'result'),
                                                         "文件类型(*.xlsx;*.xls)")  # 设置文件扩展名过滤

        fileName = fileName.replace('/', '\\')  # windows下需要进行文件分隔符转换
        logger.info('当前指定的Excel路径为：%s' % fileName)
        return (fileName)

    def refresh_settings_json(self, settings_json):
        self.settings_json = settings_json
        # self.init_label_links()
        # self.check_update_version(is_start=True)

    def closeEvent(self, QCloseEvent):
        reply = MyQMessageBox('温馨提示', '确定要退出吗？', '确定', '取消')
        if reply == 16384:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

    def messageBox_error_warn(self, error_str):
        MyQMessageBox("温馨提醒", "%s" % error_str, "我知道了")

    def messageBox_success_dialog(self, success_str):
        MyQMessageBox("温馨提醒", "%s" % success_str, "我知道了")

    def show_progress(self, _str):
        pass
        # self.label_progress.setText(_str)

    def check_update_version(self, is_start=False):
        pass
        # TODO LiST

    def visit_urls(self, key):
        url = self.settings_json.get(key,
                                     'http://mp.weixin.qq.com/mp/homepage?__biz=Mzg2MTY3Nzg1Nw==&hid=3&sn=d544991a964fad28d06b6b2fe9013583&scene=18')
        webbrowser.open(url)


if __name__ == "__main__":
    import sys
    from app_config import APPIconPath

    if getattr(sys, 'frozen', False):
        root_path = os.path.dirname(sys.executable)
    else:
        root_path = os.path.dirname(__file__)

    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QtWidgets.QApplication(sys.argv)

    splash = SplashScreen(":/splash/images/images/app_splash.png")
    splash.loadProgress()
    LogicMainWindow = RwbAppLogicMainWindow(root_path=root_path)

    LogicMainWindow.setWindowIcon(QIcon(APPIconPath))
    LogicMainWindow.show()
    splash.finish(LogicMainWindow)

    sys.exit(app.exec())
