# -*- coding: UTF-8 -*-

import threading
import time
import getSongId
import getComment
import Queue
from Tkinter import *

exitFlag = 0
q = Queue.Queue()
headers = {
        'Host': 'music.163.com',
        'Proxy-Connection': 'keep-alive',
        'Origin': 'http://music.163.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8'
    }

class myThread(threading.Thread):  # 继承父类threading.Thread
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        print "Starting " + self.name
        acquireHotComment(5, 1)

def acquireHotComment(delay, counter):
    preid = 0
    pretime = time.time()
    while counter:
        if exitFlag:
            threading.Thread.exit()
        time.sleep(delay)
        id = getSongId.getId()
        if(id != preid):
            while not q.empty():
                q.get()
            preid = id
            pretime = time.time()
            data = getComment.doPrepare(id)
            hotlist = getComment.commonlist(id, headers, data)
            name = getComment.songname(id, headers)
            print ("------------" + name + " && " + str(len(hotlist)) +"-----------")
            for context in hotlist:
                if context!="":
                    singlecontext = context.replace("\n", "\t")
                    print context.replace("\n", "\t");
                    q.put(singlecontext)
        else:
            if (time.time() - pretime > 60):
                pretime = time.time()
                print "same as last one!  %s: %s" % (getSongId.getId(), time.ctime(time.time()))

class ThreadQueue(threading.Thread):  # 继承父类threading.Thread
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        print "Starting " + self.name
        acquireQueue(6, 1)

def acquireQueue(delay, counter):
    while counter:
        time.sleep(delay)
        print("------------#############-----------")
        if(~q.empty()):
            print q.get()


def marquee(widget):
    global stopflag
    textwidth = 80
    global pos
    global source_str
    strlen = len(source_str.rstrip())
    show_str.set(source_str[pos:pos + textwidth])
    pos += 2
    if pos > strlen - 8:
        pos = 0
        stopflag = False

    if stopflag:
        widget.after(200, marquee, widget)
    else:
        stopflag = True
        source_str = q.get()
        q.put(source_str)
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
        source_str = q.get()
        q.put(source_str)
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
    # q = Queue.Queue()
    # 创建新线程
    thread1 = myThread(1, "Thread-getHotComments")

    # 开启线程
    thread1.start()

    # thread2 = ThreadQueue(2, "Thread-queue")
    # thread2.start()

    if(~q.empty()):
        root = Tk()
        root.wm_attributes('-topmost', 1)
        root.title("HotComments")
        root.geometry("295x110+25+20")
        show_str = StringVar(root)
        show_str.set("")
        show_str2 = StringVar(root)
        show_str2.set("")
        source_str = q.get()
        source_str = addprefix(source_str)
        source_str = addsuffix(source_str)
        stopflag = False
        pos = 0

        stopflag = True
        show_lb = Label(root, justify=LEFT, padx=10, bg='#FF00FF', textvariable=show_str)
        show_lb.place(x=28, y=20, width=240, height=30)
        marquee(show_lb)

    root.mainloop()

    print "Exiting Main Thread"
