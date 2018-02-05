# coding:utf-8

import os, datetime

namechache = ""
base_dir = 'C://Users//tangl//AppData//Local//Netease//CloudMusic//Cache//Cache'
def compare(x, y):
    stat_x = os.stat(base_dir + "/" + x)
    stat_y = os.stat(base_dir + "/" + y)
    if stat_x.st_ctime > stat_y.st_ctime:
        return -1
    elif stat_x.st_ctime < stat_y.st_ctime:
        return 1
    else:
        return 0

def main():
    list = os.listdir(base_dir)
    filelist = []
    for i in range(0, len(list)):
        if list[i].endswith(".uc"):
            path = os.path.join(base_dir, list[i])
            if os.path.isfile(path):
                filelist.append(list[i])
    filelist.sort(compare)
    songid = filelist[0].split("-")[0]
    path = os.path.join(base_dir, filelist[0])
    timestamp = os.path.getmtime(path)
    date = datetime.datetime.fromtimestamp(timestamp)
    print filelist[0], ' 最近修改时间是: ', date.strftime('%Y-%m-%d %H:%M:%S')

def getId():
    list = os.listdir(base_dir)
    namechache = getIdAgain(list)
    songid = namechache.split("-")[0]
    return songid
    # path = os.path.join(base_dir, filelist[0])
    # timestamp = os.path.getmtime(path)
    # date = datetime.datetime.fromtimestamp(timestamp)
    # print filelist[0], ' 最近修改时间是: ', date.strftime('%Y-%m-%d %H:%M:%S')

def getIdAgain(list):
    filelist = []
    for i in range(0, len(list)):
        if list[i].endswith(".uc"):
            path = os.path.join(base_dir, list[i])
            if os.path.isfile(path):
                filelist.append(list[i])
    filelist.sort(compare)
    return filelist[0]

if __name__ == '__main__':
    main()