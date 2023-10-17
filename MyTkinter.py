import tkinter as tk


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