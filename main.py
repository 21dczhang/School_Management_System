import tkinter as tk
from PIL import Image, ImageTk
import sqlite3
import hashlib
import warnings
from icecream import ic

# 禁用lib-png警告
warnings.filterwarnings("ignore", category=UserWarning)

# 连接到数据库
conn = sqlite3.connect('user_database.db')
cursor = conn.cursor()


def login():
    username = entry_username.get()
    password = entry_password.get()

    # 查询数据库中的账户和密码哈希值
    cursor.execute("SELECT password_hash FROM school_user WHERE username=?", (username,))
    result = cursor.fetchone()

    if result:
        # 如果用户名存在，验证密码
        stored_hash = result[0]
        entered_hash = hashlib.sha256(password.encode()).hexdigest()

        if stored_hash == entered_hash:
            result_label.config(text="登录成功！")
        else:
            result_label.config(text="密码错误")
    else:
        # 用户名不存在
        result_label.config(text="用户不存在")


def create_full_screen():
    temp_root = tk.Tk()
    ic(int(temp_root.winfo_screenwidth() / 2))
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

    print("实际宽度:", actual_width)
    print("实际高度:", actual_height)
    return temp_root


# 创建全屏窗口
root = create_full_screen()
root.title("全屏登录界面")
# 创建PhotoImage对象
image_path = 'Picture/雪山背景.jpg'
img = Image.open(image_path)
photo_img = ImageTk.PhotoImage(img)

# 创建Canvas作为背景容器
canvas = tk.Canvas(root, width=root.winfo_reqwidth(), height=root.winfo_reqheight(), bg="#F8F8FF")
canvas.pack(fill="both", expand=True)

# 在Canvas上放置图像
canvas.create_image(root.winfo_width()/2, root.winfo_height()/2, anchor="center", image=photo_img)

# 用户名标签和输入框
label_username = tk.Label(root, text="账户:", font=20, height=2, relief=tk.RIDGE)
label_username.place(x=root.winfo_width()/2 - 150, y=root.winfo_height()/2 - 160, anchor='center')

entry_username = tk.Entry(root, width=40, bd=10, relief=tk.RIDGE, font=15, justify="center")
entry_username.place(x=root.winfo_width()/2 + 75, y=root.winfo_height()/2 - 160, anchor='center')

# 密码标签和输入框
label_password = tk.Label(root, text="密码:", font=20, height=2, relief=tk.RIDGE)
label_password.place(x=root.winfo_width()/2 - 150, y=root.winfo_height()/2 - 100, anchor='center')

entry_password = tk.Entry(root, width=40, bd=10, relief=tk.RIDGE, font=15, justify="center", show="*")
entry_password.place(x=root.winfo_width()/2 + 75, y=root.winfo_height()/2 - 100, anchor='center')
#

# # 登录按钮
login_button = tk.Button(root, text="登录", command=login, font=20)
login_button.place(x=root.winfo_width()/2 + 70, y=root.winfo_height()/2 + 20, anchor='center', width=200, height=50)

change_button = tk.Button(root, text="忘记密码？", command=login, font=20)
change_button.place(x=root.winfo_width()/2 + 250, y=root.winfo_height()/2 + 100, anchor='center', width=85, height=25)
#
# bt = tk.Button(root, text="k", fg='black')
#
# # 显示登录结果的标签
# result_label = tk.Label(root, text="")
# result_label.grid(row=3, column=0, columnspan=3, pady=10)

# 运行主循环
root.mainloop()

# 关闭数据库连接
conn.close()




