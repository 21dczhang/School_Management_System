import hashlib
import sqlite3
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from icecream import ic

global_username = 0;
global_Authority = 0;

Authority_options = ['root', 'student', 'teacher']
Grades_options = ['Grade1', 'Grade2', 'Grade3', 'Grade4', 'Grade5', 'Grade6']


def insert_default_text(entry, default_text):
    entry.insert(0, default_text)
    entry.config(fg='grey')  # 设置默认文本颜色为灰色

def load_Grade_data_student(tree, student_id):
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT User_Name, Grade1, Grade2, Grade3, Grade4, Grade5, Grade6 FROM Grades WHERE User_Name=?", (student_id,))
    data = cursor.fetchall()

    for row in data:
        tree.insert('', 'end', values=row)

    conn.close()



def on_entry_click(event, entry, default_text):
    if entry.get() == default_text:
        entry.delete(0, "end")  # 删除默认文本
        entry.config(fg='grey')  # 设置文本颜色为灰色

# 新增的辅助函数，用于处理焦点离开输入框时的事件
def on_focus_out(event, entry, default_text):
    if not entry.get():
        entry.insert(0, default_text)
        entry.config(fg='grey')  # 设置默认文本颜色为灰色

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
    global global_username, global_Authority
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()
    username = temp_entry_username.get()
    global_username = username
    password = temp_entry_password.get()
    # ic(username)
    # ic(global_username)
    # 查询数据库中的账户和密码哈希值
    cursor.execute("SELECT PassWord_Hash , Name , Authority FROM School_User WHERE User_Name=?", (username,))
    result = cursor.fetchone()

    if result:
        # 如果用户名存在，验证密码
        stored_hash = result[0]
        entered_hash = hashlib.sha256(password.encode()).hexdigest()

        if stored_hash == entered_hash:
            show_welcome_screen(result[1], temp_root)
            global_Authority = result[2]
            ic(global_Authority)
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


def create_full_screen(temp_title):
    temp_root = tk.Tk()
    # 获取屏幕宽度和高度
    temp_root.title(temp_title)
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


def load_data(tree):
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT User_Name, Name, Authority FROM School_User")
    data = cursor.fetchall()

    for row in data:
        tree.insert('', 'end', values=row)

    conn.close()


def load_Grade_data(tree):
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT User_Name, Grade1, Grade2, Grade3, Grade4, Grade5, Grade6 FROM Grades")
    data = cursor.fetchall()

    for row in data:
        tree.insert('', 'end', values=row)

    conn.close()



def find_and_scroll(tree, username_entry):
    # 获取用户输入的账号
    username = username_entry.get()

    # 连接到SQLite数据库
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()

    # 查询数据库中对应账号的位置
    cursor.execute("SELECT ROWID FROM School_User WHERE User_Name=?", (username,))
    result = cursor.fetchone()

    cursor.execute("SELECT COUNT(*) FROM School_User")
    row_count = cursor.fetchone()[0]

    if result:
        # 获取对应的行号
        row_id = result[0]

        # 滑动到对应的位置
        tree.yview_moveto(row_id / row_count)
        ic(row_id / row_count)

    # 关闭连接
    conn.close()


def center_text(temp_tree):
    # 将单元格中的文字居中
    for col in temp_tree["columns"]:
        temp_tree.column(col, anchor='center')

def update_grades(tree, username_entry, combo_var, grade_entry):
    # 获取用户输入的账号、成绩和科目
    username = username_entry.get()
    new_grade = grade_entry.get()
    subject = combo_var.get()

    # 连接到SQLite数据库
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()

    # 更新数据库中对应账号的成绩
    cursor.execute(f"UPDATE Grades SET {subject}=? WHERE User_Name=?", (new_grade, username))

    # 提交更改并关闭连接
    conn.commit()
    conn.close()

    # 重新加载数据到Treeview
    tree.delete(*tree.get_children())  # 清空Treeview
    load_Grade_data(tree)  # 重新加载数据


# 创建一个新的函数用于更新权限
def update_authority(tree, username_entry, combo_var):
    # 获取用户输入的账号和新权限
    username = username_entry.get()
    new_authority = combo_var.get()

    # 连接到SQLite数据库
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()

    # 更新数据库中对应账号的权限
    cursor.execute("UPDATE School_User SET Authority=? WHERE User_Name=?", (new_authority, username))

    # 提交更改并关闭连接
    conn.commit()
    conn.close()

    # 重新加载数据到Treeview
    tree.delete(*tree.get_children())  # 清空Treeview
    load_data(tree)  # 重新加载数据


def create_root_screen_module(temp_root):
    # 创建右侧的空白 Frame
    # right_frame = tk.Frame(temp_root, width=500)
    # right_frame.pack(side='right', fill='y')

    temp_tree = ttk.Treeview(temp_root, columns=('User_Name', 'Name', 'Authority'), show='headings')
    temp_tree.heading('User_Name', text='User_Name')
    temp_tree.heading('Name', text='Name')
    temp_tree.heading('Authority', text='Authority')
    temp_tree.column('User_Name', width=100)
    temp_tree.column('Name', width=150)
    temp_tree.column('Authority', width=80)

    load_data(temp_tree)

    # 创建滑动条
    yscroll = ttk.Scrollbar( temp_root, orient='vertical', command=temp_tree.yview)

    # 创建按钮
    button = tk.Button(temp_root, text="查询",width=6, height=1, command=lambda: find_and_scroll(temp_tree, username_entry1))
    change_button = tk.Button(temp_root, text="更改", width=2, height=1,command=lambda: update_authority(temp_tree, username_entry2,combo_var))

    # 创建输入框
    username_entry1 = tk.Entry(temp_root,justify='center')
    username_entry2 = tk.Entry(temp_root, justify='center')

    combo_var = tk.StringVar()
    combobox = ttk.Combobox(temp_root, textvariable=combo_var, values=Authority_options,width=5, state="readonly")
    combobox.set(Authority_options[2])  # 设置默认选项


    # 使用grid布局
    temp_tree.grid(row=0, column=0, sticky='nsew', padx=(100, 0))
    yscroll.grid(row=0, column=1, sticky='nsew', padx=(0,100))
    button.grid(row=0, column=2, sticky='nsew',padx=(0,200),columnspan=2,pady=(190,650))
    username_entry1.grid(row=0, column=2, sticky='ew',padx=(0,100),pady=(150,680))
    username_entry2.grid(row=0, column=2, sticky='ew', padx=(0, 100), pady=(250, 580))
    combobox.grid(row=0,column=2,sticky='ew',padx=(0, 100), pady=(280, 550))
    change_button.grid(row=0, column=2, sticky='ew', padx=(0, 200),  pady=(315, 515))
    # find_button = tk.Button(temp_root, text="Find and Scroll", command=lambda: find_and_scroll(temp_tree, 2021631096))
    # find_button.pack(pady=10)
    temp_tree.bind('<Map>', center_text(temp_tree))

    # 设置主窗口的行和列权重，以便调整大小时可以均匀分配空间
    temp_root.grid_rowconfigure(0, weight=1)
    temp_root.grid_columnconfigure(0, weight=1)


def create_teacher_screen_module(temp_root):
    # 创建右侧的空白 Frame
    temp_tree = ttk.Treeview(temp_root, columns=('User_Name', 'Grade1', 'Grade2', 'Grade3', 'Grade4', 'Grade5', 'Grade6'), show='headings')
    temp_tree.heading('User_Name', text='User_Name')
    temp_tree.heading('Grade1', text='Grade1')
    temp_tree.heading('Grade2', text='Grade2')
    temp_tree.heading('Grade3', text='Grade3')
    temp_tree.heading('Grade4', text='Grade4')
    temp_tree.heading('Grade5', text='Grade5')
    temp_tree.heading('Grade6', text='Grade6')

    # 设置列宽
    temp_tree.column('User_Name', width=100)
    for col in ['Grade1', 'Grade2', 'Grade3', 'Grade4', 'Grade5', 'Grade6']:
        temp_tree.column(col, width=80)

    load_Grade_data(temp_tree)

    # 创建滑动条
    yscroll = ttk.Scrollbar(temp_root, orient='vertical', command=temp_tree.yview)

    # 创建按钮
    button = tk.Button(temp_root, text="查询", width=6, height=1,
                       command=lambda: find_and_scroll(temp_tree, username_entry1))
    change_button = tk.Button(temp_root, text="更改", width=2, height=1,
                       command=lambda: update_grades(temp_tree, username_entry2, combo_var, username_entry3))
    combo_var = tk.StringVar()
    combobox = ttk.Combobox(temp_root, textvariable=combo_var, values=Grades_options,width=5, state="readonly")
    combobox.set(Grades_options[5])  # 设置默认选项

    # 创建输入框
    username_entry1 = tk.Entry(temp_root, justify='center')
    username_entry2 = tk.Entry(temp_root, justify='center')
    username_entry3 = tk.Entry(temp_root, justify='center')

    # 插入默认文字
    insert_default_text(username_entry1, "学号")
    insert_default_text(username_entry2, "学号")
    insert_default_text(username_entry3, "成绩")

    username_entry1.bind('<FocusIn>', lambda event: on_entry_click(event, username_entry1, "学号"))
    username_entry1.bind('<FocusOut>', lambda event: on_focus_out(event, username_entry1, "学号"))

    username_entry2.bind('<FocusIn>', lambda event: on_entry_click(event, username_entry2, "学号"))
    username_entry2.bind('<FocusOut>', lambda event: on_focus_out(event, username_entry2, "学号"))

    username_entry3.bind('<FocusIn>', lambda event: on_entry_click(event, username_entry3, "成绩"))
    username_entry3.bind('<FocusOut>', lambda event: on_focus_out(event, username_entry3, "成绩"))


    # 使用grid布局
    temp_tree.grid(row=0, column=0, sticky='nsew', padx=(100, 0))
    yscroll.grid(row=0, column=1, sticky='nsew', padx=(0, 100))
    button.grid(row=0, column=2, sticky='nsew',padx=(0,200),columnspan=2,pady=(190,650))
    username_entry1.grid(row=0, column=2, sticky='ew',padx=(0,100),pady=(150,680))
    username_entry2.grid(row=0, column=2, sticky='ew', padx=(0, 100), pady=(250, 580))
    change_button.grid(row=0, column=2, sticky='ew', padx=(0, 200),  pady=(350, 830-350))
    username_entry3.grid(row=0, column=2, sticky='ew', padx=(0, 100), pady=(310, 520))
    combobox.grid(row=0,column=2,sticky='ew',padx=(0, 100), pady=(280, 550))

    temp_tree.bind('<Map>', center_text(temp_tree))



    # 设置主窗口的行和列权重，以便调整大小时可以均匀分配空间
    temp_root.grid_rowconfigure(0, weight=1)
    temp_root.grid_columnconfigure(0, weight=1)



def create_student_screen_module(temp_root, student_id):
    # 创建右侧的空白 Frame
    temp_tree = ttk.Treeview(temp_root, columns=('User_Name', 'Grade1', 'Grade2', 'Grade3', 'Grade4', 'Grade5', 'Grade6'), show='headings')
    temp_tree.heading('User_Name', text='User_Name')
    temp_tree.heading('Grade1', text='Grade1')
    temp_tree.heading('Grade2', text='Grade2')
    temp_tree.heading('Grade3', text='Grade3')
    temp_tree.heading('Grade4', text='Grade4')
    temp_tree.heading('Grade5', text='Grade5')
    temp_tree.heading('Grade6', text='Grade6')

    # 设置列宽
    temp_tree.column('User_Name', width=100)
    for col in ['Grade1', 'Grade2', 'Grade3', 'Grade4', 'Grade5', 'Grade6']:
        temp_tree.column(col, width=80)

    load_Grade_data_student(temp_tree, student_id)

    # 创建滑动条
    yscroll = ttk.Scrollbar(temp_root, orient='vertical', command=temp_tree.yview)


    # 使用grid布局
    temp_tree.grid(row=0, column=0, sticky='nsew', padx=(100, 0))
    yscroll.grid(row=0, column=1, sticky='nsew', padx=(0, 100))
    
    temp_tree.bind('<Map>', center_text(temp_tree))



    # 设置主窗口的行和列权重，以便调整大小时可以均匀分配空间
    temp_root.grid_rowconfigure(0, weight=1)
    temp_root.grid_columnconfigure(0, weight=1)


def load_photo_image(image_path):
    img = Image.open(image_path)
    photo_img = ImageTk.PhotoImage(img)
    return photo_img


def load_photo_image_bg():
    return load_photo_image('Picture/bg.jpg')



