import threading

#当多个线程对共享空间进行处理时需要有锁的参与

#若没有锁操作 job1 和 job2 会同时操作 且数据会混乱

def job1():
    global A, lock   #全局变量A
    lock.acquire()   #获取锁，此时只有job1可以对A进行操作
    for i in range(10):
        A += 1   
        print('job1', A)
    lock.release()

def job2():
    global A, lock
    lock.acquire()
    for i in range(10):
        A += 10
        print('job2', A)
    lock.release()

if __name__ == '__main__':
    lock = threading.Lock()  # 创建一个锁  再分配锁
    A = 0   #共享内存
    t1 = threading.Thread(target=job1)
    t2 = threading.Thread(target=job2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()