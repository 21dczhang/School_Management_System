import hashlib
import sqlite3
import tkinter as tk
import warnings
import MyTkinter as MyTk

from PIL import Image, ImageTk
from icecream import ic

# 禁用lib-png警告
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=UserWarning, message=".*iCCP.*")


def main():
    # 创建全屏窗口
    root = MyTk.create_full_screen()
    root.title("全屏登录界面")
    bg = MyTk.load_photo_image('Picture/bg.jpg')
    logo = MyTk.load_photo_image('Picture/logo.jpg')
    MyTk.create_login_screen_module(root, bg, logo)
    # 运行主循环
    root.mainloop()

    root = MyTk.create_full_screen()
    root.mainloop()
    ic("我是最后")

if __name__=='__main__':

    main()

