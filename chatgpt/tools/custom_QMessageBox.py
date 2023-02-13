from workers.import_qt_module import *
from configs.easypoi_config import APPIconPath


def MyQMessageBox(title, text, button1, button2=None, Qicon_fp=APPIconPath):
    '''
    :param title: 提示窗口标题
    :param text: 提示语
    :param button1: button1名称，string
    :param button2: button2 名称
    :param Qicon_fp: eg:':/icon/img/easypoi.png'
    :return:
    '''
    messageBox = QMessageBox()
    messageBox.setWindowTitle(title)
    if Qicon_fp is not None:
        messageBox.setWindowIcon(QtGui.QIcon('%s' % Qicon_fp))
    messageBox.setText(text)
    # button2 在左，button1在右
    if button2:
        messageBox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        buttonY = messageBox.button(QMessageBox.StandardButton.Yes)
        buttonY.setText(button1)
        buttonN = messageBox.button(QMessageBox.StandardButton.No)
        buttonN.setText(button2)
    else:
        messageBox.setStandardButtons(QMessageBox.StandardButton.Yes)
        buttonY = messageBox.button(QMessageBox.StandardButton.Yes)
        buttonY.setText(button1)
    messageBox.exec()
    if messageBox.clickedButton() == buttonY:
        return 16384
    else:
        return 0


if __name__ == "__main__":
    MyQMessageBox(title='test', text='it is a test', button1='yes')
