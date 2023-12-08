import hashlib
import sqlite3
import tkinter as tk
import warnings
import MyTkinter as MyTk
import MySQL3

from PIL import Image, ImageTk
from icecream import ic

# 禁用lib-png警告
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=UserWarning, message=".*iCCP.*")


def main():
    #创建全屏窗口
    root = MyTk.create_full_screen("全屏登录界面")
    bg = MyTk.load_photo_image('Picture/bg.jpg')
    logo = MyTk.load_photo_image('Picture/logo.jpg')
    MyTk.create_login_screen_module(root, bg, logo)
    # 运行主循环
    root.mainloop()

    ic(MyTk.global_username)
    ic(MyTk.global_Authority)

    # 根据权限执行不同的模块
    if MyTk.global_Authority == 'root':
        root = MyTk.create_full_screen("root")
        MyTk.create_root_screen_module(root)
        root.mainloop()
        ic("我是最后")

    elif MyTk.global_Authority == 'teacher':
        root = MyTk.create_full_screen("root")
        MyTk.create_teacher_screen_module(root)
        root.mainloop()
        ic("我是最后")

    elif MyTk.global_Authority == 'student':
        root = MyTk.create_full_screen("root")
        MyTk.create_student_screen_module(root, MyTk.global_username)
        root.mainloop()
        ic("我是最后")

    #root
    # root = MyTk.create_full_screen("root")
    # MyTk.create_root_screen_module(root)
    # root.mainloop()
    # ic("我是最后")

    # #teacher
    # root = MyTk.create_full_screen("root")
    # MyTk.create_teacher_screen_module(root)
    # root.mainloop()
    # ic("我是最后")

    #student
    # root = MyTk.create_full_screen("root")
    # MyTk.create_student_screen_module(root,2021631097)
    # root.mainloop()
    # ic("我是最后")


if __name__=='__main__':
    main()


