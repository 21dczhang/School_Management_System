# # #!/usr/bin/python
# #
# import sqlite3
# import hashlib
#
#
# def add_user(username, password_hash, name, authority):
#     temp_conn = sqlite3.connect("user_database.db")
#     temp_cursor = temp_conn.cursor()
#     password_hash = hashlib.sha256(password_hash.encode()).hexdigest()
#     # 插入用户数据
#     temp_cursor.execute("INSERT INTO School_User (User_Name, PassWord_Hash, Name, Authority) VALUES (?, ?, ?, ?)",
#                    (username, password_hash, name, authority))
#
#     temp_conn.commit()
#     temp_conn.close()
#
#

import tkinter as tk
from tkinter import ttk
import sqlite3

def connect_to_database():
    # 连接到SQLite数据库
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()

    # 创建一个示例表格
    cursor.execute('''CREATE TABLE IF NOT EXISTS Users
                      (ID INTEGER PRIMARY KEY,
                       Name TEXT,
                       Age INTEGER)''')

    # 插入一些示例数据
    cursor.execute("INSERT INTO Users (Name, Age) VALUES (?, ?)", ('Alice', 25))
    cursor.execute("INSERT INTO Users (Name, Age) VALUES (?, ?)", ('Bob', 30))

    # 提交更改并关闭连接
    conn.commit()
    conn.close()

def load_data(tree):
    # 连接到SQLite数据库
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # 从数据库中获取数据
    cursor.execute("SELECT * FROM Users")
    data = cursor.fetchall()

    # 在Treeview中插入数据
    for row in data:
        tree.insert('', 'end', values=row)

    # 关闭连接
    conn.close()

def main():
    # 连接到数据库并创建示例数据
    connect_to_database()

    # 创建主窗口
    root = tk.Tk()
    root.title("Database Table Example")

    # 创建Treeview表格
    tree = ttk.Treeview(root, columns=('ID', 'Name', 'Age'), show='headings')

    # 设置列的标题
    tree.heading('ID', text='ID')
    tree.heading('Name', text='Name')
    tree.heading('Age', text='Age')

    # 设置列的宽度
    tree.column('ID', width=50)
    tree.column('Name', width=100)
    tree.column('Age', width=50)

    # 加载数据到表格
    load_data(tree)

    # 将表格放置在主窗口中
    tree.pack(padx=10, pady=10)

    # 进入主循环
    root.mainloop()

if __name__ == "__main__":
    main()
