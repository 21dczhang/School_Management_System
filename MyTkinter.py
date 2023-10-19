import hashlib
import sqlite3
import tkinter as tk

from PIL import Image, ImageTk
from icecream import ic


def create_full_screen():
    root = tk.Tk()

    # 获取屏幕宽度和高度
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # 设置窗口大小
    root.geometry("{}x{}".format(screen_width, screen_height))
    return root


def destroy_screen(root):
    root.mainloop()
    root.destroy()


def login(temp_entry_username, temp_entry_password, temp_root, temp_result_label):
    # 连接到数据库
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()
    username = temp_entry_username.get()
    password = temp_entry_password.get()
    ic(username)
    # 查询数据库中的账户和密码哈希值
    cursor.execute("SELECT PassWord_Hash , Name FROM School_User WHERE User_Name=?", (username,))
    result = cursor.fetchone()

    if result:
        # 如果用户名存在，验证密码
        stored_hash = result[0]
        entered_hash = hashlib.sha256(password.encode()).hexdigest()

        if stored_hash == entered_hash:
            show_welcome_screen(result[1], temp_root)
            # result_label.config(text="登录成功！")
            ic("登录成功！")
        else:
            temp_result_label.config(text="密码错误")
            ic("密码错误")
    else:
        # 用户名不存在
        temp_result_label.config(text="用户不存在")
        ic("用户不存在")
    # 关闭数据库连接
    conn.close()


def show_welcome_screen(username, temp_root):
    # 创建欢迎界面
    welcome_window = tk.Toplevel()
    welcome_window.title("欢迎回来")

    welcome_label = tk.Label(welcome_window, text=f"欢迎回来，{username}！", font=("宋体", 20))
    welcome_label.pack(padx=20, pady=20)

    # 添加确定按钮
    ok_button = tk.Button(welcome_window, text="确定", command=lambda: close_windows(welcome_window, temp_root),
                          font=20)
    ok_button.pack(pady=10)
    # 设置焦点在"确定"按钮上
    ok_button.focus_force()
    welcome_window.bind("<Return>", lambda event: ok_button.invoke())

    # 获取窗口的宽度和高度
    window_width = welcome_window.winfo_reqwidth()
    window_height = welcome_window.winfo_reqheight()
    screen_width = welcome_window.winfo_screenwidth()
    screen_height = welcome_window.winfo_screenheight()

    x_coordinate = (screen_width - window_width) // 2  # 居中计算
    y_coordinate = (screen_height - window_height) // 2  # 居中计算

    welcome_window.geometry(f"+{x_coordinate}+{y_coordinate}")

def close_windows(window, temp_root):
    # 关闭窗口
    window.destroy()
    temp_root.destroy()


def create_full_screen():
    temp_root = tk.Tk()
    # 获取屏幕宽度和高度
    screen_width = temp_root.winfo_screenwidth()
    screen_height = temp_root.winfo_screenheight()

    # 设置窗口大小
    temp_root.geometry("{}x{}".format(screen_width, screen_height))
    temp_root.configure(bg="#ADD8E6")
    temp_root.update()
    # 获取窗口的实际宽度和高度
    actual_width = temp_root.winfo_width()
    actual_height = temp_root.winfo_height()

    ic(actual_width, actual_height)
    return temp_root


def create_login_screen_module(temp_root, temp_photo_img_bg, temp_photo_img_logo):
    # 创建Canvas作为背景容器
    canvas = tk.Canvas(temp_root, width=temp_root.winfo_reqwidth(), height=temp_root.winfo_reqheight(), bg="#F8F8FF")
    canvas.pack(fill="both", expand=True)

    # # 在Canvas上放置图像
    canvas.create_image(temp_root.winfo_width() / 2, temp_root.winfo_height() / 2, anchor="center",
                        image=temp_photo_img_bg)

    canvas.create_image(temp_root.winfo_width() / 2 + 550, temp_root.winfo_height() / 2 - 300, anchor="center",
                        image=temp_photo_img_logo)

    # 用户名标签和输入框
    label_username = tk.Label(temp_root, text="账户:", font=20, height=2, relief=tk.RIDGE)
    label_username.place(x=temp_root.winfo_width() / 2 - 150, y=temp_root.winfo_height() / 2 - 160, anchor='e')

    entry_username = tk.Entry(temp_root, width=40, bd=10, relief=tk.RIDGE, font=15, justify="center")
    entry_username.place(x=temp_root.winfo_width() / 2 + 75, y=temp_root.winfo_height() / 2 - 160, anchor='center')

    # 密码标签和输入框
    label_password = tk.Label(temp_root, text="密码:", font=20, height=2, relief=tk.RIDGE)
    label_password.place(x=temp_root.winfo_width() / 2 - 150, y=temp_root.winfo_height() / 2 - 100, anchor='e')

    entry_password = tk.Entry(temp_root, width=40, bd=10, relief=tk.RIDGE, font=15, justify="center", show="*")
    entry_password.place(x=temp_root.winfo_width() / 2 + 75, y=temp_root.winfo_height() / 2 - 100, anchor='center')


    result_label = tk.Label(temp_root, text="", font=("宋体", 12), fg="red", bg="#F4F8F7", anchor='e')
    result_label.place(x=temp_root.winfo_width() / 2 - 80, y=temp_root.winfo_height() / 2 - 60, anchor='center')

    welcome_label = tk.Label(temp_root, text="学校管理系统登录", font=("宋体", 50, "bold"), bg="#F4F8F7")
    welcome_label.place(x=temp_root.winfo_width() / 2 + 75, y=100, anchor='center')

    make_label = tk.Label(temp_root, text="制作：21dczhang", font=("宋体", 14, "italic"), bg="#F4F8F7")
    make_label.place(x=100, y=50, anchor='center')

    make_label = tk.Label(temp_root, text="有问题？联系我：", font=("宋体", 14, "italic", "overstrike"), bg="#F4F8F7")
    make_label.place(x=100, y=70, anchor='center')

    #entry_password.bind("<Return>", login(entry_username, entry_password, temp_root, result_label))
    entry_password.bind("<Return>", lambda event: login(entry_username, entry_password, temp_root, result_label))

    # # 登录按钮
    login_button = tk.Button(temp_root, text="登录(Login)",
                             command=lambda: login(entry_username, entry_password, temp_root, result_label), font=20)
    login_button.place(x=temp_root.winfo_width() / 2 + 70, y=temp_root.winfo_height() / 2 + 20, anchor='center',
                       width=200,
                       height=50)

    change_button = tk.Button(temp_root, text="忘记密码？", command=login, font=10)
    change_button.place(x=temp_root.winfo_width() / 2 + 250, y=temp_root.winfo_height() / 2 + 100, anchor='w',
                        height=25)


def load_photo_image(image_path):
    img = Image.open(image_path)
    photo_img = ImageTk.PhotoImage(img)
    return photo_img


def load_photo_image_bg():
    return load_photo_image('Picture/bg.jpg')
