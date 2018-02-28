# -*- coding: UTF-8 -*-
from Tkinter import *
import time

text = ("说喜欢李荣浩版本的真的不是在开玩笑吗…不是听一首歌啊",
        "不是听一首歌啊说喜欢李荣浩版本的真的不是在开玩笑吗…",
        "不是听一首歌dsadddddddddxxxxxxxxxxxxxxxxx…")
def marquee(widget):
    global stopflag
    textwidth = 80
    global pos
    global source_str
    strlen = len(source_str.rstrip())
    show_str.set(source_str[pos:pos + textwidth])
    pos += 2
    if pos > strlen + 75:
        pos = 0
        stopflag = False

    if stopflag:
        widget.after(200, marquee, widget)
    else:
        stopflag = True
        source_str = "不是听一首歌啊说喜欢李荣浩版本的真的不是在开玩笑吗…"
        source_str = addprefix(source_str)
        source_str = addsuffix(source_str)
        show_d = Label(root, justify=LEFT, padx=10, bg='#9A32CD', textvariable=source_str)
        show_d.place(x=28, y=70, width=240, height=30)
        marquee(show_d)

def addprefix(source_str):
    for num in range(1, 75):
        source_str = " " + source_str
    return source_str

def addsuffix(source_str):
    for num in range(1, 75):
        source_str = source_str+ " "
    return source_str

if __name__ == '__main__':
    root = Tk()
    root.title("HotComments")
    root.geometry("295x100+25+20")
    show_str = StringVar(root)
    show_str.set("")
    global s
    source_str = "说喜欢李荣浩版本的真的不是在开玩笑吗…不是听一首歌啊"
    # strlen = len(source_str)

    source_str = addprefix(source_str)
    source_str = addsuffix(source_str)

    # source_str = "不是听一首歌啊"
    stopflag = False
    pos = 0

    # show_lb = Label(root, justify=LEFT, padx = 10,  bg='#FF00FF', textvariable=show_str)
    # # show_lb.pack(side="left")
    # show_lb.place(x=28, y=30, width=240, height=30)

    def stopmarquee():
        global stopflag
        stopflag = False


    # marquee(show_lb)
    i = 0
    # while (stopflag == False):
    stopflag = True
    #     global source_str
    # source_str = text[i]
    show_lb = Label(root, justify=LEFT, padx=10, bg='#FF00FF', textvariable=show_str)
    show_lb.place(x=28, y=20, width=240, height=30)
    # show_d = Label(root, justify=LEFT, padx=10, bg='#9A32CD', textvariable=show_str)
    # show_d.place(x=28, y=70, width=240, height=30)
    marquee(show_lb)

    # button1 = Button(root, text="start", command=startmarque)
    # button2 = Button(root, text="stop", command=stopmarquee)
    # button1.place(x=20, y=100, width=50, height=30)
    # button2.place(x=200, y=100, width=50, height=30)
    root.mainloop()
