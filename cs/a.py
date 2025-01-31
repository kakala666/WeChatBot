from hashlib import md5
from string import ascii_letters, digits
from itertools import permutations
import threading
import multiprocessing
import time
import os

all_letters = ascii_letters + digits + '.,;*@#'

# md5码
md5_value = '23C5E803722019E0731B1B01F5513EA3'
# 最小长度
min_len = 20
# 最大长度
max_len = 21
# 使用CPU核数，由于有主进程，实际上有n+1个进程
worker_num = 24
# 线程数，只有验证md5的部分使用了单核多线程
thread_num = 32
# 枚举队列
taskq = multiprocessing.Queue()
# 结果队列，若有数据传入，则终止所有进程
resultq = multiprocessing.Queue()
# 枚举长度，为了多线程运行，使用了multiprocessing的队列
len_q = multiprocessing.Queue()
# 记录所有的进程信息，本项目没有使用python已有的进程管理工具
record = []


class Decrypt(threading.Thread):
    def __init__(self, name, taskq):
        threading.Thread.__init__(self)
        self.name = name
        self.taskq = taskq

    def run(self):
        while True:
            text = self.taskq.get()
            print("Get ==> " + str(text), end="\t")
            if md5(text.encode()).hexdigest() == md5_value:
                print(text)
                resultq.put((True, text))
                return True, text
            else:
                print("False")


def do_task(taskq):
    thread_list = []
    for i in range(thread_num):
        name = str(os.getpid()) + "_" + str(i)
        thread = Decrypt(name, taskq)
        # thread.setDaemon(True)
        thread.start()
        thread_list.append(thread)
    while taskq.empty():
        return
    # for t in thread_list:
    #     t.join()


def put_task(taskq, len_q):
    while True:
        k = len_q.get()
        for item in permutations(all_letters, k):
            item = ''.join(item)
            # print("Put ==> " + str(item))
            taskq.put(item)
        # time.sleep(1000)
        # exit(0)


if __name__ == '__main__':
    if len(md5_value) != 32:
        print('error')
        exit(0)
    for i in range(min_len, max_len):
        len_q.put(i)

    md5_value = md5_value.lower()
    multiprocessing.freeze_support()
    for i in range(int(worker_num / 2)+1):
        multiprocessing.freeze_support()
        process = multiprocessing.Process(target=put_task, args=(taskq, len_q,))
        process.start()
        record.append(process)

    for i in range(int(worker_num / 2)-1):
        name = "pro_" + str(i)
        process = multiprocessing.Process(target=do_task, name=name, args=(taskq,))
        process.start()
        record.append(process)
    result = resultq.get()
    for process in record:
        process.join()
    print(result)