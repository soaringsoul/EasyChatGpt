# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_page.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTabWidget, QTextEdit,
    QVBoxLayout, QWidget)
import images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 688)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.action_help = QAction(MainWindow)
        self.action_help.setObjectName(u"action_help")
        icon = QIcon()
        icon.addFile(u":/rwb_icons/images/rwb_icons/help.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_help.setIcon(icon)
        self.action_about = QAction(MainWindow)
        self.action_about.setObjectName(u"action_about")
        icon1 = QIcon()
        icon1.addFile(u":/rwb_icons/images/rwb_icons/rwb_logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_about.setIcon(icon1)
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"\n"
"QTabWidget{\n"
"    border: none;\n"
"}\n"
"\n"
"QTabWidget:focus {\n"
"    border: none;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: none;\n"
"    padding: 0px;\n"
"    background-color: #e6e6e6;\n"
"    position: absolute;\n"
"    top: -15px;\n"
"    padding-top: 15px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    alignment: center;\n"
"}\n"
"\n"
"QTabBar {\n"
"    qproperty-drawBase: 0;\n"
"    left: 5px;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QTabBar:focus {\n"
"    border: 0px transparent black;\n"
"}\n"
"\n"
"QTabBar::close-button {\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"    border-radius: 2px;\n"
"    background-image: url(icons/close_dark.png);\n"
"    background-position: center center;\n"
"    background-repeat: none;\n"
"}\n"
"\n"
"QTabBar::close-button:hover {\n"
"    background-color: #fad57a;\n"
"}\n"
"\n"
"QTabBar::close-button:pressed {\n"
"    background-color: #fce6b1;\n"
"}\n"
"\n"
"QTabBar::scroller { /* the width of the scroll buttons */\n"
"    width: 20px"
                        ";\n"
"}\n"
"\n"
"/* the scroll buttons are tool buttons */\n"
"QTabBar QToolButton,\n"
"QTabBar QToolButton:hover { \n"
"    margin-top: 4px;\n"
"    margin-bottom: 4px;\n"
"    margin-left: 0px;\n"
"    margin-right: 0px;\n"
"    padding: 0px;\n"
"    border: none;\n"
"    background-color: #e6e6e6;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow:enabled {\n"
"     image: url(icons/right_arrow_light.png);\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow:disabled,\n"
"QTabBar QToolButton::right-arrow:off {\n"
"     image: url(icons/right_arrow_disabled_dark.png);\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow:hover {\n"
"     image: url(icons/right_arrow_lighter.png);\n"
"}\n"
"\n"
" QTabBar QToolButton::left-arrow:enabled {\n"
"     image: url(icons/left_arrow_light.png);\n"
"}\n"
"\n"
" QTabBar QToolButton::left-arrow:disabled,\n"
" QTabBar QToolButton::left-arrow:off {\n"
"     image: url(icons/left_arrow_disabled_dark.png);\n"
"}\n"
"\n"
" QTabBar QToolButton::left-arrow:hover {"
                        "\n"
"     image: url(icons/left_arrow_lighter.png);\n"
"}\n"
"\n"
" QTabBar QToolButton::up-arrow:enabled {\n"
"     image: url(icons/up_arrow_light.png);\n"
"}\n"
"\n"
" QTabBar QToolButton::up-arrow:disabled,\n"
" QTabBar QToolButton::up-arrow:off {\n"
"     image: url(icons/up_arrow_disabled_dark.png);\n"
"}\n"
"\n"
" QTabBar QToolButton::up-arrow:hover {\n"
"     image: url(icons/up_arrow_lighter.png);\n"
"}\n"
"\n"
" QTabBar QToolButton::down-arrow:enabled {\n"
"     image: url(icons/down_arrow_light.png);\n"
"}\n"
"\n"
" QTabBar QToolButton::down-arrow:disabled,\n"
" QTabBar QToolButton::down-arrow:off {\n"
"     image: url(icons/down_arrow_disabled_dark.png);\n"
"}\n"
"\n"
" QTabBar QToolButton::down-arrow:hover {\n"
"     image: url(icons/down_arrow_lighter.png);\n"
"}\n"
"\n"
"/* TOP and BOTTOM TABS */\n"
"QTabBar::tab:top,\n"
"QTabBar::tab:bottom {\n"
"    color: #ffffff;\n"
"    border: 1px solid #b6b6b6;\n"
"    border-left-color: #e6e6e6;\n"
"    border-right-width: 0px;\n"
"    background-color: "
                        "#b6b6b6;\n"
"    padding:5px 15px;\n"
"    margin-top: 4px;\n"
"    margin-bottom: 4px;\n"
"    position: center;\n"
"}\n"
"\n"
"QTabBar::tab:top:first,\n"
"QTabBar::tab:bottom:first {\n"
"    border-top-left-radius: 6px;\n"
"    border-bottom-left-radius: 6px;\n"
"}\n"
"\n"
"QTabBar::tab:top:last,\n"
"QTabBar::tab:bottom:last {\n"
"    border-top-right-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"    border-right-width: 1px;\n"
"}\n"
"\n"
"QTabBar::tab:top:selected,\n"
"QTabBar::tab:bottom:selected {\n"
"    color: black;\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0.545, x2:1, y2:0, stop:0 #e0a108, stop:1 #f8bf36);\n"
"    border-color: #e0a108;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected:hover,\n"
"QTabBar::tab:bottom:!selected:hover {\n"
"    color: black;\n"
"}\n"
"\n"
"QTabBar::tab:top:only-one ,\n"
"QTabBar::tab:bottom:only-one {\n"
"    border: 1px solid #9d7106;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"/* LEFT and RIGHT TABS */\n"
"QTabBar::tab:left,\n"
"QTabBar::tab:ri"
                        "ght {\n"
"    color: #ffffff;\n"
"    border: 1px solid #b6b6b6;\n"
"    border-top-color: #e6e6e6;\n"
"    border-bottom-width: 0px;\n"
"    background-color: #b6b6b6;\n"
"    padding: 15px 5px;\n"
"    margin-left: 4px;\n"
"    margin-right: 4px;\n"
"    position: center;\n"
"}\n"
"\n"
"QTabBar::tab:left:first,\n"
"QTabBar::tab:right:first {\n"
"    border-top-left-radius: 6px;\n"
"    border-top-right-radius: 6px;\n"
"}\n"
"\n"
"QTabBar::tab:left:last,\n"
"QTabBar::tab:right:last {\n"
"    border-bottom-left-radius: 6px;\n"
"    border-bottom-right-radius: 6px;\n"
"    border-bottom-width: 1px;\n"
"}\n"
"\n"
"QTabBar::tab:left:selected,\n"
"QTabBar::tab:right:selected {\n"
"    color: black;\n"
"    background-color: qlineargradient(spread:pad, x1:0.545, y1:1, x2:0, y2:1, stop:0 #e0a108, stop:1 #f8bf36);\n"
"    border-color: #e0a108;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected:hover,\n"
"QTabBar::tab:right:!selected:hover {\n"
"    color: black;\n"
"}\n"
"\n"
"QTabBar::tab:left:only-one ,\n"
"QTabBar::tab:r"
                        "ight:only-one {\n"
"    border: 1px solid #9d7106;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QDockWidget {\n"
"    color: #828282;\n"
"    border: 1px solid #e6e6e6;\n"
"    titlebar-close-icon: url(icons/close_dark.png);\n"
"    titlebar-normal-icon: url(icons/undock_dark.png);\n"
"}\n"
"\n"
"QDockWidget::title {\n"
"    text-align: center;\n"
"    background-color: #e0e0e0;\n"
"    padding: 4px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QDockWidget::close-button,\n"
"QDockWidget::float-button {\n"
"    border: 1px transparent #e6e6e6;\n"
"    border-radius: 2px;\n"
"    background: transparent;\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: right center;\n"
"}\n"
"\n"
"QDockWidget::close-button {\n"
"    right: 4px;\n"
"}\n"
"    \n"
"QDockWidget::float-button {\n"
"    right: 22px;\n"
"}\n"
"\n"
"QDockWidget::close-button:hover,\n"
"QDockWidget::float-button:hover {\n"
"    background: #f5f5f5;\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed,\n"
"QDockWidget::float-button:pressed {\n"
""
                        "    /*padding: 1px -1px -1px 1px;*/\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"QTreeView,\n"
"QListView {\n"
"    color: #828282;\n"
"    border: 1px solid #e6e6e6;\n"
"    border-radius: 4px;\n"
"    background-color: #d3d1cd;  /* related with alternate-background-color*/\n"
"    selection-color: black;\n"
"    selection-background-color: #f8bf36; /* should be similar to QListView::item selected background-color */\n"
"    show-decoration-selected: 1; /* make the selection span the entire width of the view */\n"
"    padding: 0px;\n"
"    margin: 0px 4px 0px 4px;\n"
"    min-width: 130px; /* hack to correctly align Preferences icon list  */\n"
"}\n"
"\n"
"QListView,\n"
"QListView::item,\n"
"QListView QAbstractItemView {\n"
"    margin: 0px;\n"
"    icon-size: 20px; /* temporal */\n"
"    paint-alternating-row-colors-for-empty-area: 1;\n"
"    position: absolute;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: left top;\n"
"}\n"
"\n"
"/* Control dropdown list margins of QComboBox */\n"
""
                        "QComboBox QTreeView,\n"
"QComboBox QListView {\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"QListView::item {\n"
"    border: 0px transparent #e6e6e6;\n"
"    border-radius: 4px;\n"
"    background-color: transparent;\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"    display: inline-block;\n"
"    position: relative;\n"
"}\n"
"\n"
"QListView::item:selected,\n"
"QTreeView::item:selected  {\n"
"    color: black;\n"
"    background-color: #f8bf36; /* should be similar to QListView selection-background-color */\n"
"}\n"
"\n"
"/* Branch system */\n"
"QTreeView::branch  {\n"
"    background: transparent;\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:!adjoins-item  {\n"
"    border-image: url(icons/branch_vline.png) 0;\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:adjoins-item  {\n"
"    border-image: url(icons/branch_more.png) 0;\n"
"}\n"
"\n"
"QTreeView::branch:!has-children:!has-siblings:adjoins-item  {\n"
"    border-image: url(icons/branch_end.png) 0;\n"
"}\n"
"\n"
"QTreeView::branch:closed:has-chi"
                        "ldren:has-siblings  {\n"
"    image: url(icons/branch_closed_dark.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed  {\n"
"    image: url(icons/branch_closed_dark.png);\n"
"    border-image: url(icons/branch_end.png) 0;\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:has-siblings  {\n"
"    image: url(icons/branch_open_dark.png);\n"
"    border-image: url(icons/branch_more.png) 0;\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings  {\n"
"    image: url(icons/branch_open_dark.png);\n"
"    border-image: url(icons/branch_end.png) 0;\n"
"}\n"
"\n"
"QSlider,\n"
"QSlider:active,\n"
"QSlider:!active {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QSlider:horizontal {\n"
"    padding: 0px 10px;\n"
"}\n"
"\n"
"QSlider:vertical {\n"
"    padding: 10px 0px;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #b6b6b6;\n"
"    background-color: #b6b6b6;\n"
"    height: 8px;\n"
"    border-radius: 5px;\n"
"    margin: 4px 0;\n"
"}\n"
"\n"
""
                        "QSlider::groove:vertical {\n"
"    border: 1px solid #b6b6b6;\n"
"    background-color: #b6b6b6;\n"
"    width: 8px;\n"
"    border-radius: 5px;\n"
"    margin: 4px 0;\n"
"}\n"
"\n"
"QSlider::groove:horizontal:disabled,\n"
"QSlider::groove:vertical:disabled {\n"
"    border-color:  #e0e0e0;\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal,\n"
"QSlider::handle:vertical {\n"
"    background-color: #828282;\n"
"    border: 1px solid #828282;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    margin: -4px 0;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    margin: 0 -4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover,\n"
"QSlider::handle:vertical:hover {\n"
"    border-color: #e0a108;\n"
"    background-color: #e0a108;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed,\n"
"QSlider::handle:vertical:pressed {\n"
"    border-color: #9d7106;\n"
"    background-color: #9d7106;\n"
"}\n"
"\n"
"QSlider::handle:horizontal"
                        ":disabled,\n"
"QSlider::handle:vertical:disabled {\n"
"    border-color: #b6b6b6;\n"
"    background-color: #e6e6e6;\n"
"}\n"
"\n"
"QToolButton {\n"
"    color: #ffffff;\n"
"    text-align: center;\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0.545, x2:1, y2:0, stop:0 #b6b6b6, stop:1 #e6e6e6);\n"
"    border: 1px solid #828282;\n"
"    padding-top: 5px;\n"
"    padding-bottom: 5px;\n"
"    padding-left: 15px;\n"
"    padding-right: 15px;\n"
"    margin-top: 5px;\n"
"    margin-bottom: 5px;\n"
"    margin-left: 10px;\n"
"    margin-right: 10px;\n"
"    border-radius: 3px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QToolButton:hover,\n"
"QToolButton:focus {\n"
"    color: black;\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0.545, x2:1, y2:0, stop:0 #e0a108, stop:1 #f8bf36);\n"
"    border-color: #e0a108;\n"
"}\n"
"\n"
"QToolButton:disabled,\n"
"QToolButton:disabled:checked {\n"
"    color: #b6b6b6;\n"
"    background-color: #e6e6e6;\n"
"    border-color: #b6b6b6;\n"
"}\n"
"\n"
"QTo"
                        "olButton:pressed {\n"
"    border-color: #fad57a;\n"
"}\n"
"\n"
"QToolButton:checked {\n"
"    background-color: #f8bf36;\n"
"    border-color: #e0a108;\n"
"}\n"
"\n"
"QToolButton::menu-indicator  {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: center right;\n"
"    right: 4px;\n"
"}\n"
"\n"
"/*The \"show more\" button  (it can also be stylable with \"QToolBarExtension\" */\n"
"QToolButton#qt_toolbar_ext_button {\n"
"    border-radius: 0px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"    /*background-image: url(icons/more_dark.png);*/\n"
"    image: transparent;\n"
"    background-repeat: none;\n"
"    background-position: center left;\n"
"}\n"
"\n"
"QToolButton#qt_toolbar_ext_button:hover {\n"
"    /*background-image: url(icons/more_light.png);*/\n"
"    border-color: #e0e0e0;\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"QToolButton#qt_toolbar_ext_button:on {\n"
"    /*background-image: url(icons/more_light.png);*/\n"
"    border-color: #e0e0e0;\n"
"    background-color: #e0e0e0;\n"
""
                        "}\n"
"\n"
"/*Buttons inside the Toolbar*/\n"
"QToolBar QToolButton {\n"
"    color: #828282;\n"
"    background-color: #e6e6e6;\n"
"    border: 1px transparent #e6e6e6;\n"
"    border-radius: 3px;\n"
"    margin: 0px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QToolBar QToolButton:disabled {\n"
"    background-color: #e6e6e6;\n"
"}\n"
"\n"
"QToolBar QToolButton:checked {\n"
"    color: #9d7106;\n"
"    background-color: #f8bf36;\n"
"    border: 1px solid #f8bf36;\n"
"}\n"
"\n"
"QToolBar QToolButton:hover {\n"
"    background-color: #e6e6e6;\n"
"}\n"
"\n"
"QToolBar QToolButton:pressed,\n"
"QToolBar QToolButton::menu-button:pressed {\n"
"    background-color: #e0e0e0;\n"
"    border: 1px solid #e0e0e0;\n"
"}\n"
"\n"
"\n"
"QToolBar QToolButton::menu-indicator:hover,\n"
"QToolBar QToolButton::menu-indicator:pressed {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* the subcontrols below are used only in the MenuButtonPopup mode */\n"
"QToolBar QToolButton::menu-button {\n"
"    border: 1px transparent #4A4949;\n"
""
                        "    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    width: 16px; /* 16px width + 4px for border = 20px allocated above */\n"
"    outline: none;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QToolBar QToolButton::menu-button:hover,\n"
"QToolBar QToolButton::menu-button:active,\n"
"QToolBar QToolButton::menu-button:disabled {\n"
"    border-color: transparent;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QToolBar QToolButton::menu-arrow {\n"
"    background-image: url(icons/down_arrow_light.png);\n"
"    background-position: center center;\n"
"    background-repeat: none;\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: bottom right;\n"
"    height: 10px; /* same as arrow image */\n"
"}\n"
"\n"
"QToolBar QToolButton::menu-arrow:open {\n"
"    background-image: url(icons/down_arrow_lighter.png);\n"
"}\n"
"\n"
"QToolBar:tear {\n"
"    color: blue;\n"
"    background-color: red;\n"
"}\n"
"\n"
"QTableView {\n"
"    color: #828282;\n"
"    border: 1px s"
                        "olid #b6b6b6;\n"
"    gridline-color: #f5f5f5;\n"
"    background-color: #d3d1cd;\n"
"    selection-color: #828282;\n"
"    selection-background-color: #fce6b1;\n"
"    border-radius: 3px;\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QTableView::item:hover  {\n"
"    background: #cbc9c4;\n"
"}\n"
"\n"
"QTableView::item:disabled  {\n"
"    color: #e6e6e6;\n"
"}\n"
"\n"
"QTableView::item:selected  {\n"
"    color: #9d7106;\n"
"    background-color: #fad57a;\n"
"}\n"
"\n"
"/* when editing a cell: */\n"
"QTableView QLineEdit {\n"
"    color: #828282;\n"
"    background-color: #cfcdc9;\n"
"    border-radius: 0px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"QHeaderView {\n"
"    border: none;\n"
"    background-color: #828282;\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"QHeaderView::section  {\n"
"    background-color: tra"
                        "nsparent;\n"
"    color: #ffffff;\n"
"    border: 1px solid transparent;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QHeaderView::section::vertical  {\n"
"    padding: 0px 6px 0px 6px;\n"
"    border-bottom: 1px solid #b6b6b6;\n"
"}\n"
"\n"
"QHeaderView::section::vertical:first {\n"
"    border-top: 1px solid  #b6b6b6;\n"
"}\n"
"\n"
"QHeaderView::section::vertical:last {\n"
"    border-bottom: none;\n"
"}\n"
"\n"
"QHeaderView::section::vertical:only-one {\n"
"    border: none;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal  {\n"
"    padding: 0px 0px 0px 6px;\n"
"    border-right: 1px solid #b6b6b6;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal:first {\n"
"    border-left: 1px solid #b6b6b6;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal:last {\n"
"    border-left: none;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal:only-one {\n"
"    border: none;\n"
"}\n"
"\n"
"QDockWidget QHeaderView::section {\n"
"    border-width: 6px 1px 6px 1px; /* hack to bigger margin for Model Panel t"
                        "able headers */\n"
"}\n"
"\n"
"QHeaderView::section:checked {\n"
"    color: #9d7106;\n"
"    background-color: #fad57a;\n"
"}\n"
"\n"
" /* style the sort indicator */\n"
"QHeaderView::down-arrow {\n"
"    image: url(icons/down_arrow_light.png);\n"
"}\n"
"\n"
"QHeaderView::up-arrow {\n"
"    image: url(icons/up_arrow_light.png);\n"
"}\n"
"\n"
"QTableCornerButton::section {\n"
"    background-color: #828282;\n"
"    border: 1px solid #828282;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QToolBox  {\n"
"    padding: 3px;\n"
"    color: #9d7106;\n"
"    border: none;\n"
"}\n"
"\n"
"QToolBox::tab { /* TODO */\n"
"    color: #ffffff;\n"
"    background-color: #b6b6b6;\n"
"    border: 1px transparent #828282;\n"
"    border-bottom: 1px transparent #b6b6b6;\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QToolBox::tab:selected { /* italicize selected tabs */\n"
"    color: #9d7106;\n"
"    font: italic;\n"
"    background-color: #f8bf36;\n"
"    border-col"
                        "or: #f8bf36;\n"
" }\n"
"\n"
"QStatusBar::item {\n"
"    color: #ffffff;\n"
"    background-color: #e6e6e6;\n"
"    border: 1px solid #e6e6e6;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSplitter::handle {\n"
"    background-color: #e6e6e6;\n"
"    margin: 0px 11px;\n"
"    padding: 0px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QSplitter::handle:vertical {\n"
"    background-image: url(icons/splitter_horizontal_dark.png);\n"
"    background-position: center center;\n"
"    background-repeat: none;\n"
"    margin: 2px 10px 2px 10px;\n"
"    height: 2px;\n"
"}\n"
"\n"
"QSplitter::handle:horizontal {\n"
"    background-image: url(icons/splitter_horizontal_dark.png);\n"
"    background-position: center center;\n"
"    background-repeat: none;\n"
"    margin: 10px 2px 10px 2px;\n"
"    width: 2px;\n"
"}\n"
"\n"
"QSplitter::handle:horizontal:hover,\n"
"QSplitter::handle:vertical:hover {\n"
"    background-color: #e6e6e6;\n"
"}\n"
"\n"
"/* Similar to the splitter is the following window separator: */\n"
"QMainWindow"
                        "::separator {\n"
"    border: 1px solid #e6e6e6;\n"
"    background-color: #e6e6e6;\n"
"    background-position: center center;\n"
"    background-repeat: none;\n"
"}\n"
"\n"
"QMainWindow::separator:hover {\n"
"    background-color: #e6e6e6;\n"
"}\n"
"\n"
"QMainWindow::separator:horizontal {\n"
"    height: 4px;\n"
"    background-image: url(icons/splitter_horizontal_dark.png);\n"
"}\n"
"\n"
"QMainWindow::separator:vertical {\n"
"    width: 4px;\n"
"    background-image: url(icons/splitter_vertical_dark.png);\n"
"}\n"
"\n"
"QLabel {\n"
"    padding-top: 3px;\n"
"    padding-bottom: 3px;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"    color: #b6b6b6;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Action group */\n"
"QFrame[class=\"panel\"] {\n"
"    border: none;\n"
"    background-color: #e6e6e6;\n"
"}\n"
"\n"
"QSint--ActionGroup QFrame[class=\"header\"] {\n"
"    border: none;\n"
"    background-color: #828282;\n"
"    border-top-left-radius: 3px;\n"
"    border-top-r"
                        "ight-radius: 3px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"QSint--ActionGroup QFrame[class=\"header\"]:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0.545, x2:1, y2:0, stop:0 #e0a108, stop:1 #f8bf36);\n"
"}\n"
"\n"
"QSint--ActionGroup QToolButton[class=\"header\"] {\n"
"    text-align: left;\n"
"    font-weight: bold;\n"
"    color: #ffffff;\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"QSint--ActionGroup QToolButton[class=\"header\"]:hover {\n"
"    color: black;\n"
"}\n"
"\n"
"QSint--ActionGroup QFrame[class=\"header\"] QLabel {\n"
"    background-color: transparent;\n"
"    background-image: url(icons/down_arrow_light.png);\n"
"    background-repeat: none;\n"
"    background-position: center center;\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QSint--ActionGroup QFrame[class=\"header\"] QLabel:hover {\n"
""
                        "    background-color: transparent;\n"
"    background-image: url(icons/down_arrow_lighter.png);\n"
"}\n"
"\n"
"QSint--ActionGroup QFrame[class=\"header\"] QLabel[fold=\"true\"] {\n"
"    background-color: transparent;\n"
"    background-image: url(icons/up_arrow_light.png);\n"
"    background-repeat: none;\n"
"    background-position: center center;\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QSint--ActionGroup QFrame[class=\"header\"] QLabel[fold=\"true\"]:hover {\n"
"    background-color: transparent;\n"
"    background-image: url(icons/up_arrow_lighter.png);\n"
"}\n"
"\n"
"QSint--ActionGroup QFrame[class=\"content\"] {\n"
"    background-color: #d3d1cd;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"    border: none;\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-left-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"/* HACK\n"
"This might not be the best way to reset the background color: */\n"
"QSint--ActionGroup QFrame[cla"
                        "ss=\"content\"] QWidget {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QSint--ActionGroup QFrame[class=\"content\"] QPushButton {\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0.545, x2:1, y2:0, stop:0 #b6b6b6, stop:1 #e6e6e6);\n"
"}\n"
"\n"
"QSint--ActionGroup QFrame[class=\"content\"] QPushButton:hover,\n"
"QSint--ActionGroup QFrame[class=\"content\"] QPushButton:focus {\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0.545, x2:1, y2:0, stop:0 #e0a108, stop:1 #f8bf36);\n"
"}\n"
"\n"
"QSint--ActionGroup QFrame[class=\"content\"] QPushButton:disabled,\n"
"QSint--ActionGroup QFrame[class=\"content\"] QPushButton:disabled:checked {\n"
"    color: #d3d1cd;\n"
"    border-color: #f5f5f5;\n"
"    background-color: #f5f5f5;\n"
"}\n"
"QSint--ActionGroup QFrame[class=\"content\"] QPushButton:checked {\n"
"    background-color: #f8bf36;\n"
"}\n"
"\n"
"QSint--ActionGroup QFrame[class=\"content\"] QComboBox {\n"
"    background-color: #b6b6b6;\n"
"}\n"
"\n"
"QSint--ActionGroup QFr"
                        "ame[class=\"content\"] QComboBox:on {\n"
"    background-color: #b6b6b6;\n"
"}\n"
"\n"
"QSint--ActionGroup QFrame[class=\"content\"] QComboBox QAbstractItemView {\n"
"    border-color: #828282;\n"
"    background-color: #828282;\n"
"}\n"
"\n"
"QSint--ActionGroup QFrame[class=\"content\"] QListView {\n"
"    border-color: #cbc9c4;\n"
"    background-color: #cbc9c4;\n"
"}\n"
"\n"
"QSint--ActionGroup QFrame[class=\"content\"] QAbstractSpinBox {\n"
"    background-color: #b6b6b6;\n"
"}\n"
"\n"
"QSint--ActionGroup QFrame[class=\"content\"] QLineEdit {\n"
"    background-color: #b6b6b6;\n"
"}\n"
"\n"
"QSint--ActionGroup QFrame[class=\"content\"] QComboBox:disabled,\n"
"QSint--ActionGroup QFrame[class=\"content\"] QAbstractSpinBox:disabled,\n"
"QSint--ActionGroup QFrame[class=\"content\"] QLineEdit:disabled {\n"
"    color: #d3d1cd;\n"
"    border-color: #f5f5f5;\n"
"    background-color: #f5f5f5;\n"
"}\n"
"\n"
"QSint--ActionGroup QFrame[class=\"content\"] QCheckBox:disabled,\n"
"QSint--ActionGroup QFrame[class=\"con"
                        "tent\"] QRadioButton:disabled {\n"
"    color: #f5f5f5;\n"
"    border-color: #f5f5f5;\n"
"}\n"
"\n"
"QSint--ActionGroup QFrame[class=\"content\"] QCheckBox::indicator:disabled,\n"
"QSint--ActionGroup QFrame[class=\"content\"] QRadioButton::indicator:disabled {\n"
"    border-color: #f5f5f5;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QSint--ActionGroup QFrame[class=\"content\"] QHeaderView {\n"
"    border: none;\n"
"    background-color: #828282;\n"
"    border-radius: 0px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"QSint--ActionGroup QFrame[class=\"content\"] QHeaderView::section  {\n"
"    background-color: transparent;\n"
"    color: #ffffff;\n"
"    border: 1px solid transparent;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QSint--ActionGroup QFrame[class=\"content\"] QHeaderView::section::horizontal  {\n"
"    padding: 6px 0px 6px 6px;\n"
"    border-right: 1px solid #b6b6b6;\n"
"}\n"
"\n"
"QSint--ActionGroup QFrame[class=\"content\"] QHeaderView::secti"
                        "on::horizontal:first {\n"
"    border-left: 1px solid #e6e6e6;\n"
"}\n"
"\n"
"QSint--ActionGroup QFrame[class=\"content\"] QHeaderView::section::horizontal:last {\n"
"    border-left: none;\n"
"}\n"
"\n"
"QSint--ActionGroup QFrame[class=\"content\"] QHeaderView::section::horizontal:only-one {\n"
"    border: none;\n"
"}\n"
"/* enf of HACK */\n"
"\n"
"QSint--ActionGroup QToolButton[class=\"action\"],\n"
"QSint--ActionGroup QToolButton[class=\"action\"]:enabled {\n"
"    font-weight: bold;\n"
"    color: #b6b6b6;\n"
"}\n"
"\n"
"QSint--ActionGroup QToolButton[class=\"action\"]:hover,\n"
"QSint--ActionGroup QToolButton[class=\"action\"]:enabled:hover {\n"
"    text-decoration: none;\n"
"    color: #828282;\n"
"    background-color: #cbc9c4;\n"
"    border-color: #cbc9c4;\n"
"}\n"
"\n"
"QSint--ActionGroup QToolButton[class=\"action\"]:disabled {\n"
"    color: #e6e6e6;\n"
"    background-color: #cbc9c4;\n"
"    border-color: #cbc9c4;\n"
"}\n"
"\n"
"QSint--ActionGroup QToolButton[class=\"action\"]:focus,\n"
"QSint--"
                        "ActionGroup QToolButton[class=\"action\"]:pressed\n"
"QSint--ActionGroup QToolButton[class=\"action\"]:enabled:focus,\n"
"QSint--ActionGroup QToolButton[class=\"action\"]:enabled:pressed {\n"
"    color: black;\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0.545, x2:1, y2:0, stop:0 #e0a108, stop:1 #f8bf36);\n"
"    border-color: #e0a108;\n"
"}\n"
"\n"
"QSint--ActionGroup QToolButton[class=\"action\"]:on {\n"
"    background-color: red;\n"
"    color: red;\n"
"}")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(0, 0, 0, 0)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setStyleSheet(u"background-image: url(:/rwb_icons/images/rwb_icons/rwb_logo_40.png);")
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 0))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icon/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_8.addItem(self.horizontalSpacer)

        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 0))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icon/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.toggleBox_help = QFrame(self.leftMenuFrame)
        self.toggleBox_help.setObjectName(u"toggleBox_help")
        self.toggleBox_help.setMaximumSize(QSize(16777215, 45))
        self.toggleBox_help.setFrameShape(QFrame.NoFrame)
        self.toggleBox_help.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.toggleBox_help)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)

        self.verticalMenuLayout.addWidget(self.toggleBox_help)

        self.toggleBox_about = QFrame(self.leftMenuFrame)
        self.toggleBox_about.setObjectName(u"toggleBox_about")
        self.toggleBox_about.setMaximumSize(QSize(16777215, 45))
        self.toggleBox_about.setFrameShape(QFrame.NoFrame)
        self.toggleBox_about.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.toggleBox_about)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)

        self.verticalMenuLayout.addWidget(self.toggleBox_about)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.btn_settings = QPushButton(self.bottomMenu)
        self.btn_settings.setObjectName(u"btn_settings")
        sizePolicy.setHeightForWidth(self.btn_settings.sizePolicy().hasHeightForWidth())
        self.btn_settings.setSizePolicy(sizePolicy)
        self.btn_settings.setMinimumSize(QSize(0, 0))
        self.btn_settings.setFont(font)
        self.btn_settings.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_settings.setLayoutDirection(Qt.LeftToRight)
        self.btn_settings.setStyleSheet(u"background-image: url(:/icon/images/icons/icon_settings.png);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_9.addWidget(self.btn_settings)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(300, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 30))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(0, 0, 0, -1)
        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(0, 0))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icon/images/icons/icon_close-circle-filled.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon2)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 1, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(100, 0))
        self.extraLabel.setStyleSheet(u"color: rgb(66, 66, 66);")

        self.extraTopLayout.addWidget(self.extraLabel, 0, 0, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraContent)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.extraContent)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_cn = QWidget()
        self.tab_cn.setObjectName(u"tab_cn")
        self.verticalLayout_10 = QVBoxLayout(self.tab_cn)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.listWidget_act_cn = QListWidget(self.tab_cn)
        self.listWidget_act_cn.setObjectName(u"listWidget_act_cn")
        self.listWidget_act_cn.setStyleSheet(u"")

        self.verticalLayout_10.addWidget(self.listWidget_act_cn)

        self.tabWidget.addTab(self.tab_cn, "")
        self.tab_en = QWidget()
        self.tab_en.setObjectName(u"tab_en")
        self.verticalLayout_6 = QVBoxLayout(self.tab_en)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.listWidget_act_en = QListWidget(self.tab_en)
        self.listWidget_act_en.setObjectName(u"listWidget_act_en")
        self.listWidget_act_en.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.listWidget_act_en)

        self.tabWidget.addTab(self.tab_en, "")

        self.verticalLayout_7.addWidget(self.tabWidget)

        self.line = QFrame(self.extraContent)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_7.addWidget(self.line)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.textEdit_prompt = QTextEdit(self.extraCenter)
        self.textEdit_prompt.setObjectName(u"textEdit_prompt")

        self.verticalLayout_2.addWidget(self.textEdit_prompt)

        self.pushButton_copy = QPushButton(self.extraCenter)
        self.pushButton_copy.setObjectName(u"pushButton_copy")
        self.pushButton_copy.setMinimumSize(QSize(0, 0))
        self.pushButton_copy.setStyleSheet(u"color: rgb(94, 94, 94);")

        self.verticalLayout_2.addWidget(self.pushButton_copy)

        self.label_copy_info = QLabel(self.extraCenter)
        self.label_copy_info.setObjectName(u"label_copy_info")

        self.verticalLayout_2.addWidget(self.label_copy_info)


        self.verticalLayout_7.addWidget(self.extraCenter)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.mainContent = QFrame(self.bgApp)
        self.mainContent.setObjectName(u"mainContent")
        self.mainContent.setFrameShape(QFrame.NoFrame)
        self.mainContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.mainContent)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.mainContent)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.stackedWidget.setLineWidth(0)
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_15 = QVBoxLayout(self.page_home)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.webview = QWebEngineView(self.page_home)
        self.webview.setObjectName(u"webview")

        self.verticalLayout_15.addWidget(self.webview)

        self.verticalLayout_15.setStretch(0, 1)
        self.stackedWidget.addWidget(self.page_home)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setStyleSheet(u"")
        self.pushButton = QPushButton(self.page)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(480, 340, 81, 38))
        self.pushButton.setStyleSheet(u" margin: 0;\n"
"    padding: 0;\n"
"    border: 1;\n"
"    font-size: 12px;\n"
"    border-radius: 6px;\n"
"    background: #fedd28;\n"
"    height: 36px;\n"
"    color: #666;\n"
"    text-align: center;\n"
"    border: 1px solid rgb(230, 230, 230);\n"
"    border-color: rgb(169, 169, 169);")
        self.pushButton_2 = QPushButton(self.page)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(590, 460, 81, 34))
        self.pushButton_2.setStyleSheet(u"")
        self.stackedWidget.addWidget(self.page)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.appLayout.addWidget(self.mainContent)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1280, 21))
        self.menu = QMenu(self.menuBar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menu.menuAction())
        self.menu.addAction(self.action_help)
        self.menu.addAction(self.action_about)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_help.setText(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
        self.action_about.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"\u4eba\u6587\u5e2e", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"\u7b80\u5355\u3001\u5b9e\u7528\u3001\u6709\u4ef7\u503c", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"\u9690\u85cf", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"\u9996\u9875", None))
        self.btn_settings.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u9009\u62e9\u89d2\u8272</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_cn), QCoreApplication.translate("MainWindow", u"\u4e2d\u6587", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_en), QCoreApplication.translate("MainWindow", u"\u82f1\u6587", None))
        self.pushButton_copy.setText(QCoreApplication.translate("MainWindow", u"\u4e00\u952e\u590d\u5236", None))
        self.label_copy_info.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9\u83dc\u5355", None))
    # retranslateUi

