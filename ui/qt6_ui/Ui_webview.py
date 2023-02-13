# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'webview.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QMainWindow, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(849, 562)
        icon = QIcon()
        icon.addFile(u":/icon/icons/EasyPoi_GapDe.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        MainWindow.setDocumentMode(True)
        self.action_help = QAction(MainWindow)
        self.action_help.setObjectName(u"action_help")
        icon1 = QIcon()
        icon1.addFile(u":/icon/img/help.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_help.setIcon(icon1)
        self.action_more_tools = QAction(MainWindow)
        self.action_more_tools.setObjectName(u"action_more_tools")
        icon2 = QIcon()
        icon2.addFile(u":/icon/img/more_tools.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_more_tools.setIcon(icon2)
        self.action_become_member = QAction(MainWindow)
        self.action_become_member.setObjectName(u"action_become_member")
        icon3 = QIcon()
        icon3.addFile(u":/icon/img/member.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_become_member.setIcon(icon3)
        self.action_customed_tools = QAction(MainWindow)
        self.action_customed_tools.setObjectName(u"action_customed_tools")
        self.action_customed_tools.setIcon(icon1)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.webview = QWebEngineView(self.centralwidget)
        self.webview.setObjectName(u"webview")

        self.verticalLayout.addWidget(self.webview)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u9ad8\u5fb7\u5730\u56fepoi\u5de5\u5177-EasyPoi", None))
        self.action_help.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u770b\u4f7f\u7528\u5e2e\u52a9", None))
        self.action_more_tools.setText(QCoreApplication.translate("MainWindow", u"\u83b7\u53d6\u66f4\u591a\u5de5\u5177", None))
#if QT_CONFIG(tooltip)
        self.action_more_tools.setToolTip(QCoreApplication.translate("MainWindow", u"\u5982\u679c\u4f60\u9700\u8981\u83b7\u53d6\u66f4\u591a\u6709\u7528\u5de5\u5177\uff0c\u8bf7\u70b9\u6211\uff01", None))
#endif // QT_CONFIG(tooltip)
        self.action_become_member.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u5165\u4eba\u6587\u5e2e\u8bfb\u8005\u4ff1\u4e50\u90e8", None))
#if QT_CONFIG(tooltip)
        self.action_become_member.setToolTip(QCoreApplication.translate("MainWindow", u"\u83b7\u53d6\u4eba\u6587\u5e2e\u4e13\u5c5e\u4f1a\u5458\u5361", None))
#endif // QT_CONFIG(tooltip)
        self.action_customed_tools.setText(QCoreApplication.translate("MainWindow", u"\u8054\u7cfb\u4f5c\u8005\u5b9a\u5236\u4e13\u5c5e\u5de5\u5177", None))
#if QT_CONFIG(shortcut)
        self.action_customed_tools.setShortcut(QCoreApplication.translate("MainWindow", u"B", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

if __name__ == "__main__":
    import sys
    from PySide6 import QtWidgets
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
