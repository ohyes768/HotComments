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
    if pos > strlen - 10:
        pos = 0
        stopflag = False

    if stopflag:
        widget.after(200, marquee, widget)
    else:
        stopflag = True
        source_str = "不是听一首歌啊说喜欢李荣浩版本的真的不是在开玩笑吗…"
        source_str = addprefix(source_str)
        source_str = addsuffix(source_str)
        show_d = Label(root, justify=LEFT, padx=10, bg='#9A32CD', textvariable=show_str2)
        show_d.place(x=28, y=60, width=240, height=30)
        marquee2(show_d)

def marquee2(downlable):
    global stopflag
    textwidth = 80
    global pos
    global source_str
    strlen = len(source_str.rstrip())
    show_str2.set(source_str[pos:pos + textwidth])
    pos += 2
    if pos > strlen -10:
        pos = 0
        stopflag = False

    if stopflag:
        downlable.after(200, marquee2, downlable)
    else:
        stopflag = True
        source_str = "说喜欢李荣浩版本的真的不是在开玩笑吗…不是听一首歌啊"
        source_str = addprefix(source_str)
        source_str = addsuffix(source_str)
        marquee(show_lb)

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
    root.geometry("295x110+25+20")
    show_str = StringVar(root)
    show_str.set("")
    show_str2 = StringVar(root)
    show_str2.set("")
    source_str = "说喜欢李荣浩版本的真的不是在开玩笑吗…不是听一首歌啊"
    source_str = addprefix(source_str)
    source_str = addsuffix(source_str)
    stopflag = False
    pos = 0

    def stopmarquee():
        global stopflag
        stopflag = False

    stopflag = True
    show_lb = Label(root, justify=LEFT, padx=10, bg='#FF00FF', textvariable=show_str)
    show_lb.place(x=28, y=20, width=240, height=30)
    marquee(show_lb)

    root.mainloop()
