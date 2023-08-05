import time
import keyboard  # 监听键盘
import pyperclip
import backend
import win10toast

toaster = win10toast.ToastNotifier()
toaster.show_toast("运行成功！",
                   "按esc键退出程序,按ctrl+c翻译.",
                   "icon/3.ico",
                   duration=5)


def play():
    time.sleep(0.1)
    function = backend.trans()
    function.tran(pyperclip.paste())


keyboard.add_hotkey('ctrl+c', play, )
keyboard.wait('esc')
