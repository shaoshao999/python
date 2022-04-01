import tkinter as tk
import keyboard
import pyperclip
root = tk.Tk()
root.title('文本快捷输入')  # 设置标题
root.geometry('400x300')  # 设置窗口大小

#label
f1 = tk.Label(root,text="1").place(relx=0.1, rely=0.1, anchor="center")
f2 = tk.Label(root,text="2").place(relx=0.1, rely=0.2, anchor="center")
f3 = tk.Label(root,text="3").place(relx=0.1, rely=0.3, anchor="center")
f4 = tk.Label(root,text="4").place(relx=0.1, rely=0.4, anchor="center")
f5 = tk.Label(root,text="5").place(relx=0.1, rely=0.5, anchor="center")
f6 = tk.Label(root,text="6").place(relx=0.1, rely=0.6, anchor="center")
f7 = tk.Label(root,text="7").place(relx=0.1, rely=0.7, anchor="center")
f8 = tk.Label(root,text="8").place(relx=0.1, rely=0.8, anchor="center")

#输入框
e1_text = tk.StringVar()
e1 = tk.Entry(root,width = 40,textvariable=e1_text).place(relx=0.15, rely=0.07)

e2_text = tk.StringVar()
e2 = tk.Entry(root,width = 40,textvariable=e2_text).place(relx=0.15, rely=0.17)

e3_text = tk.StringVar()
e3 = tk.Entry(root,width = 40,textvariable=e3_text).place(relx=0.15, rely=0.27)

e4_text = tk.StringVar()
e4 = tk.Entry(root,width = 40,textvariable=e4_text).place(relx=0.15, rely=0.37)

e5_text = tk.StringVar()
e5 = tk.Entry(root,width = 40,textvariable=e5_text).place(relx=0.15, rely=0.47)

e6_text = tk.StringVar()
e6 = tk.Entry(root,width = 40,textvariable=e6_text).place(relx=0.15, rely=0.57)

e7_text = tk.StringVar()
e7 = tk.Entry(root,width = 40,textvariable=e7_text).place(relx=0.15, rely=0.67)

e8_text = tk.StringVar()
e8 = tk.Entry(root,width = 40,textvariable=e8_text).place(relx=0.15, rely=0.77)

def shao():
    pyperclip.copy(e1_text.get())
    keyboard.press_and_release('ctrl+v')
keyboard.add_hotkey('1', shao,suppress=True)

def luo():
    pyperclip.copy(e2_text.get())
    keyboard.press_and_release('ctrl+v')
keyboard.add_hotkey('2', luo,suppress=True)

def tian():
    pyperclip.copy(e3_text.get())
    keyboard.press_and_release('ctrl+v')
keyboard.add_hotkey('3', tian,suppress=True)

def xing():
    pyperclip.copy(e4_text.get())
    keyboard.press_and_release('ctrl+v')
keyboard.add_hotkey('4', xing,suppress=True)

def yue():
    pyperclip.copy(e5_text.get())
    keyboard.press_and_release('ctrl+v')
keyboard.add_hotkey('5', yue,suppress=True)

def hang():
    pyperclip.copy(e6_text.get())
    keyboard.press_and_release('ctrl+v')
keyboard.add_hotkey('6', hang,suppress=True)

def dan():
    pyperclip.copy(e7_text.get())
    keyboard.press_and_release('ctrl+v')
keyboard.add_hotkey('7', dan,suppress=True)

def ge():
    pyperclip.copy(e8_text.get())
    keyboard.press_and_release('ctrl+v')
keyboard.add_hotkey('8', ge,suppress=True)

root.mainloop()
