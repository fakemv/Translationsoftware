import os
import time
import keyboard  # 监听键盘
import pyperclip
import backend
from win11toast import toast

currentPath = os.getcwd().replace('\\','/')
toast("运行成功！",
      "按esc键退出程序,选中翻译内容按ctrl+c翻译.",
      icon=f"{currentPath}/icon/head.ico",
      image=f"{currentPath}/icon/class.png")


def play():
    time.sleep(0.1)
    function = backend.trans()
    function.tran(pyperclip.paste())


keyboard.add_hotkey('ctrl+c', play, )
keyboard.wait('esc')
toast("退出成功！",
      "Exit successful!",
      icon=f'{currentPath}/icon/end.ico')
