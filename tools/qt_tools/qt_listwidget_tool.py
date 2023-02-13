from PySide6.QtWidgets import QListWidget, QMenu
from PySide6 import QtGui, Qt, QtCore
from PySide6.QtCore import QEvent, QObject
from PySide6.QtGui import QAction


class ListWidGetTool(object):
    def __init__(self, obj_listwidget=QListWidget()):
        self.listwidget = obj_listwidget

    def get_existed_items(self):
        existed_items = []
        # 获取listwidget中条目数
        count = self.listwidget.count()
        # 遍历listwidget中的内容
        for i in range(count):
            existed_items.append(self.listwidget.item(i).text())
        return existed_items

    def update_items(self, item_lst):
        self.listwidget.clear()
        for item in item_lst:
            self.listwidget.addItem(item)

    def example(self):
        pass
