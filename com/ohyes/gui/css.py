# -*- coding: UTF-8 -*-
from Tkinter import *
import time

if __name__ == '__main__':
    root = Tk()
    root.title("HotComments")
    root.geometry("295x110+25+20")
    show_str = StringVar(root)
    show_str.set("")
    source_str = "说喜欢李荣浩版本的真的不是在开玩笑吗…不是听一首歌啊"

    stopflag = False
    pos = 0


    show_lb = Label(root, justify=LEFT, padx=10, bg='#FF00FF', textvariable=show_str)
    show_lb.place(x=28, y=20, width=240, height=30)
    show_d = Label(root, justify=LEFT, padx=10, bg='#9A32CD', textvariable=show_str)
    show_d.place(x=28, y=60, width=240, height=30)

    root.mainloop()
