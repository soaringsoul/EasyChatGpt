from chatgpt.api.core import chatgptCloud

version = '2.6.7'


def why_error(code):
    """错误原因"""
    if code == chatgptCloud.URL_INVALID:
        return '分享链接无效'
    elif code == chatgptCloud.LACK_PASSWORD:
        return '缺少提取码'
    elif code == chatgptCloud.PASSWORD_ERROR:
        return '提取码错误'
    elif code == chatgptCloud.FILE_CANCELLED:
        return '分享链接已失效'
    elif code == chatgptCloud.ZIP_ERROR:
        return '解压过程异常'
    elif code == chatgptCloud.NETWORK_ERROR:
        return '网络连接异常'
    elif code == chatgptCloud.CAPTCHA_ERROR:
        return '验证码错误'
    else:
        return f'未知错误 {code}'


__all__ = ['utils', 'types', 'models', 'chatgptCloud', 'version']
