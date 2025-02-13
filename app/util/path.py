import os
import winreg

from app.person_pc import MePC
from app.util import dat2pic

if not os.path.exists('./data/'):
    os.mkdir('./data/')
if not os.path.exists('./data/image'):
    os.mkdir('./data/image')


def get_abs_path(path):
    # return os.path.join(os.getcwd(), 'app/data/icons/404.png')
    if path:
        base_path = os.getcwd() + "/data/image"
        output_path = dat2pic.decode_dat(os.path.join(MePC().wx_dir, path), base_path)  # './data/image')
        return output_path if output_path else ':/icons/icons/404.png'
    else:
        return ':/icons/icons/404.png'


def wx_path():
    ## 获取当前用户名
    users = os.path.expandvars('$HOMEPATH')
    ## 找到3ebffe94.ini配置文件
    f = open(r'C:' + users + '\\AppData\\Roaming\\Tencent\\WeChat\\All Users\\config\\3ebffe94.ini')
    txt = f.read()
    f.close()
    # 打开Windows注册表
    reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                             "Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders")
    # 获取“我的文档”路径的注册表键值
    documents_path_value = winreg.QueryValueEx(reg_key, "Personal")
    # 输出路径
    ##读取文件将路径放到wx_location变量里
    if txt == 'MyDocument:':
        wx_location = documents_path_value[0] + '\WeChat Files'
    else:
        wx_location = txt + "\WeChat Files"
    return wx_location
