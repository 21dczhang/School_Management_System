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
    # root = MyTk.create_full_screen("全屏登录界面")
    # bg = MyTk.load_photo_image('Picture/bg.jpg')
    # logo = MyTk.load_photo_image('Picture/logo.jpg')
    # MyTk.create_login_screen_module(root, bg, logo)
    # # 运行主循环
    # root.mainloop()

    #root
    # root = MyTk.create_full_screen("root")
    # MyTk.create_root_screen_module(root)
    # root.mainloop()
    # ic("我是最后")

    #teacher
    root = MyTk.create_full_screen("root")
    MyTk.create_root_screen_module(root)
    root.mainloop()
    ic("我是最后")

if __name__=='__main__':

    main()


# import tkinter as tk
# from tkinter import ttk
# import sqlite3
#
# def load_data(tree):
#     # 连接到SQLite数据库
#     conn = sqlite3.connect('user_database.db')
#     cursor = conn.cursor()
#
#     # 从数据库中获取数据
#     cursor.execute("SELECT User_Name, Name, PassWord_Hash FROM School_User")
#
#     data = cursor.fetchall()
#
#     # 在Treeview中插入数据
#     for row in data:
#         tree.insert('', 'end', values=row)
#
#     # 关闭连接
#     conn.close()
#
# def main():
#     # 创建主窗口
#
#     root = tk.Tk()
#     root.title("Database Table Example")
#     width = 1000
#     height = 500
#
#     root.geometry('{}x{}'.format(width, height))  # 大小以及位置
#
#
#     # # 创建一个框架
#     # tabel_frame = tk.Frame(root)
#     # tabel_frame.pack()
#     # xscroll = ttk.Scrollbar(tabel_frame, orient="horizontal")
#
#     # 创建Treeview表格
#     tree = ttk.Treeview(root, columns=('User_Name', 'Name', 'Authority', '121313201231123'), show='headings')
#
#     # 设置列的标题
#     tree.heading('User_Name', text='User_Name')
#     tree.heading('Name', text='Name')
#     tree.heading('Authority', text='Authority')
#
#     # 设置列的宽度
#     tree.column('User_Name', width=200)
#     tree.column('Name', width=500)
#     tree.column('Authority', width=200)
#
#     # 加载数据到表格
#     load_data(tree)
#
#     xbar = tk.Scrollbar(root, orient='horizontal', command=tree.xview)
#     xbar.pack(side='bottom', fill='x')
#     # 将表格放置在主窗口中
#     tree.pack(padx=10, pady=10)
#     #tree.pack(fill="both", expand=True)
#     # 将Treeview的xscrollcommand关联到滚动条的set方法
#     tree.configure(xscrollcommand=xbar.set)
#
#     # 将表格放置在框架中
#     tree.pack(padx=10, pady=10)
#     btn_frame = tk.Frame()
#     btn_frame.pack()
#
#     # 进入主循环
#     root.mainloop()
#
# import sqlite3
#
# # 连接到数据库
# conn = sqlite3.connect('user_database.db')
# cursor = conn.cursor()
#
# # 准备要插入的数据
# data_to_insert = [
#     ('2021631096', 'zhangdongyao', '1', 'student'),
#     ('2021631096', 'zhangdongyao', '1','student'),
#     ('2021631096', 'zhangdongyao', '1','student'),
#     ('2021631096', 'zhangdongyao', '1','student'),
#     ('2021631096', 'zhangdongyao', '1','student'),
#     ('2021631096', 'zhangdongyao', '1','student'),
#     ('2021631096', 'zhangdongyao', '1','student'),
#     ('2021631096', 'zhangdongyao', '1','student'),
#     ('2021631096', 'zhangdongyao', '1','student'),
#     ('2021631096', 'zhangdongyao', '1','student'),
#     ('2021631096', 'zhangdongyao', '1','student'),
#     ('2021631096', 'zhangdongyao', '1','student'),
#     ('2021631096', 'zhangdongyao', '1','student'),
#     ('2021631096', 'zhangdongyao', '1','teacher'),
#     ('2021631096', 'zhangdongyao', '1','teacher'),
#     ('2021631096', 'zhangdongyao', '1','teacher'),
#     ('2021631096', 'zhangdongyao', '1','teacher'),
#     ('2021631096', 'zhangdongyao', '1','teacher'),
#     ('2021631096', 'zhangdongyao', '1','teacher')
#
#
#
#     # 添加更多的数据行...
# ]
#
# # 使用executemany插入数据
# cursor.executemany('INSERT INTO School_User (User_Name, Name, PassWord_Hash, Authority) VALUES (?, ?, ?, ?)', data_to_insert)
#
# # 提交更改并关闭连接
# conn.commit()
# conn.close()
