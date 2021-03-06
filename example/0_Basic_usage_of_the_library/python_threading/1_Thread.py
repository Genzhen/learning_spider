#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   1_Thread.py
@Time    :   2020-11-06
@Author  :   EvilRecluse
@Contact :   https://github.com/RecluseXU
@Desc    :   
    1. 编写一个自定义类继承 Thread
    2. 复写 run() 方法, 在 run() 方法中编写任务处理代码
    3. 创建这个 Thread 的子类的实例使用
'''

# here put the import lib
import threading
import time

class MyThread(threading.Thread):
    def __init__(self, func):
        threading.Thread.__init__(self)
        self.func = func
    def run(self):
        self.func()


def helloworld():
    for i in range(5):
        print('HelloWorld x {}'.format(i))
        time.sleep(1)



if __name__ == '__main__':
    t = MyThread(helloworld)
    t.run()
