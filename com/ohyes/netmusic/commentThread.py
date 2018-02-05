# -*- coding: UTF-8 -*-

import threading
import time
import getSongId
import getComment

exitFlag = 0
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
        # initdata = getComment.doPrepare("135355")
        acquireHotComment(self.name,  5, 1)
        # print "Exiting " + self.name


def acquireHotComment(threadName, delay, counter):
    preid = 0
    pretime = time.time()
    while counter:
        if exitFlag:
            threading.Thread.exit()
        time.sleep(delay)
        id = getSongId.getId()
        # print "%s: %s" % (getSongId.getId(), time.ctime(time.time()))
        if(id != preid):
            preid = id
            pretime = time.time()
            data = getComment.doPrepare(id)
            hotlist = getComment.commonlist(id, headers, data)
            print ("------------" + str(len(hotlist)) +"-----------")
            for context in hotlist:
                if context!="":
                    print context.replace("\n", "\t");
        else:
            if (time.time() - pretime > 60):
                pretime = time.time()
                print "same as last one!  %s: %s" % (getSongId.getId(), time.ctime(time.time()))



if __name__ == '__main__':
    # 创建新线程
    thread1 = myThread(1, "Thread-getHotComments")

    # 开启线程
    thread1.start()

    print "Exiting Main Thread"
