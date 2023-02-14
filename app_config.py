import sys, os
from loguru import logger
from PySide6.QtCore import QSettings

if getattr(sys, 'frozen', False):
    root_path = os.path.dirname(sys.executable)
    logger.info('frozen')
else:
    logger.info('not frozen')
    root_path = os.path.dirname(__file__)

# app信息
AppName = 'EasyChatGpt'
AppEnName = 'EasyChatGpt'
APPIconPath = ':/icon/images/icons/favicon.png'
AppVersion = 1.1

# APP 云端配置信息
AppCloudSettingsUrl = 'https://202212-amap-tools-1258828407.cos.ap-guangzhou.myqcloud.com/lbs.amap.assistant_settings.json'
# 设置APP config信息
AppConfigDir = os.path.join(root_path, 'AppConfig')
# 不需要带.ini后缀
AppConfigName = 'chatgpt_config'

QSettings.setPath(
    QSettings.Format.IniFormat, QSettings.Scope.UserScope, AppConfigDir)
# 调用QSettings settings(QSettings::IniFormat, QSettings::UserScope, "organization_name", "application_name")，ubuntu系统下会创建/home/user/.config/organization_name/application_name.ini，如果已存在会自动加载；
AppSettings = QSettings(
    QSettings.Format.IniFormat,
    QSettings.Scope.UserScope,
    AppConfigName
)

logger.info(AppSettings.fileName())

# 使用PySide6或者PySide6
QtGuiPlugin = "PySide6"
# 点数据地图可视化html文件和依赖的js文件
