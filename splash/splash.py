# -*- coding: utf-8 -*-
"""SplashScreen

Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""

import time
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtGui import *
from PySide6.QtWebChannel import QWebChannel
from PySide6.QtWidgets import *
from PySide6.QtCore import *


class SplashScreen(QSplashScreen):
    """Custom SplashScreen"""

    def __init__(self, picfile):
        pixmap = QPixmap(picfile)
        # , Qt.WindowStaysOnTopHint)
        super(SplashScreen, self).__init__(pixmap)
        # self.setMask(splash_pix.mask())
        self.raise_()

        self.labelAlignment = int(
            Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignAbsolute)
        self.show()
        # QApplication.

    def showMessage(self, msg):
        """Show the progress message on the splash image"""
        super(SplashScreen, self).showMessage(msg, self.labelAlignment, QColor(246, 221, 40))
        QApplication.processEvents()

    def clearMessage(self):
        """Clear message on the splash image"""
        super(SplashScreen, self).clearMessage()
        QApplication.processEvents()

    def setProgressText(self, percent, delay=0.1):
        """Show load percent in format 'Loading ... xx%' by showMessage method"""
        time.sleep(delay)  # 延时，给查看splashscreen更新数值
        self.showMessage(self.tr("Loading... {0}%").format(percent))

    def loadProgress(self):
        """Preimport qt_tools to improve start speed
        Following qt_tools are imported before splash:
        PySide6, PySide6.QtCore, PySide6.QtGui, PySide6.QtWidgets are imported before Splash.
        i18n is imported before Splash, for Splash using i18n.
        config is imported before i18n, for i18n using config.
        """
        self.setProgressText(0, 0)
        time.sleep(0.1)
        self.setProgressText(5)
        time.sleep(0.1)
        self.setProgressText(10)
        time.sleep(0.1)
        self.setProgressText(15)
        time.sleep(0.1)
        self.setProgressText(20)  # before 20% do nothing
        self.setProgressText(40)
        self.setProgressText(60)
        self.setProgressText(80)
        self.setProgressText(100)
