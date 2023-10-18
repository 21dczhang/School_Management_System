import hashlib
import sqlite3
import tkinter as tk
import warnings

from PIL import Image, ImageTk
from icecream import ic

# 禁用lib-png警告
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=UserWarning, message=".*iCCP.*")


# 连接到数据库
conn = sqlite3.connect('user_database.db')
cursor = conn.cursor()


def login(temp_entry_username, temp_entry_password):
    username = temp_entry_username.get()
    password = temp_entry_password.get()
    ic(username)
    # 查询数据库中的账户和密码哈希值
    cursor.execute("SELECT PassWord_Hash FROM School_User WHERE User_Name=?", (username,))
    result = cursor.fetchone()

    if result:
        # 如果用户名存在，验证密码
        stored_hash = result[0]
        entered_hash = hashlib.sha256(password.encode()).hexdigest()

        if stored_hash == entered_hash:
            #result_label.config(text="登录成功！")
            ic("登录成功！")
        else:
            #result_label.config(text="密码错误")
            ic("密码错误")
    else:
        # 用户名不存在
        #result_label.config(text="用户不存在")
        ic("用户不存在")


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

    return temp_root


def create_screen_module(temp_root, temp_photo_img_bg, temp_photo_img_logo):

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
    label_username.place(x=temp_root.winfo_width() / 2 - 150, y=temp_root.winfo_height() / 2 - 160, anchor='center')

    entry_username = tk.Entry(temp_root, width=40, bd=10, relief=tk.RIDGE, font=15, justify="center")
    entry_username.place(x=temp_root.winfo_width() / 2 + 75, y=temp_root.winfo_height() / 2 - 160, anchor='center')

    # 密码标签和输入框
    label_password = tk.Label(temp_root, text="密码:", font=20, height=2, relief=tk.RIDGE)
    label_password.place(x=temp_root.winfo_width() / 2 - 150, y=temp_root.winfo_height() / 2 - 100, anchor='center')

    entry_password = tk.Entry(temp_root, width=40, bd=10, relief=tk.RIDGE, font=15, justify="center", show="*")
    entry_password.place(x=temp_root.winfo_width() / 2 + 75, y=temp_root.winfo_height() / 2 - 100, anchor='center')

    welcome_label = tk.Label(root, text="学校管理系统登录", font=("宋体", 50, "bold"), bg="#F4F8F7")
    welcome_label.place(x=temp_root.winfo_width() / 2 + 75, y=100, anchor='center')

    make_label = tk.Label(root, text="制作：21dczhang", font=("宋体", 14, "italic"), bg="#F4F8F7")
    make_label.place(x=100, y=50, anchor='center')

    make_label = tk.Label(root, text="有问题？联系我：", font=("宋体", 14, "italic", "overstrike"), bg="#F4F8F7")
    make_label.place(x=100, y=70, anchor='center')

    # # 登录按钮
    login_button = tk.Button(temp_root, text="登录(Login)", command=lambda: login(entry_username, entry_password), font=20)
    login_button.place(x=temp_root.winfo_width() / 2 + 70, y=temp_root.winfo_height() / 2 + 20, anchor='center', width=200,
                       height=50)

    change_button = tk.Button(temp_root, text="忘记密码？", command=login, font=20)
    change_button.place(x=temp_root.winfo_width() / 2 + 250, y=temp_root.winfo_height() / 2 + 100, anchor='center', width=85,
                        height=25)

    bt = tk.Button(root, text="k", fg='black')
    #
    # # 显示登录结果的标签
    # result_label = tk.Label(root, text="")
    # result_label.grid(row=3, column=0, columnspan=3, pady=10)


def load_photo_image(image_path):
    img = Image.open(image_path)
    photo_img = ImageTk.PhotoImage(img)
    return photo_img


def load_photo_image_bg():
    return load_photo_image('Picture/bg.jpg')


# 创建全屏窗口
root = create_full_screen()
root.title("全屏登录界面")
bg = load_photo_image('Picture/bg.jpg')
logo = load_photo_image('Picture/logo.jpg')
create_screen_module(root, bg, logo)

# 运行主循环
root.mainloop()

# 关闭数据库连接
conn.close()

