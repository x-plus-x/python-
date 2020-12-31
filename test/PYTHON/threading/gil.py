import threading
import Queue
import copy
import time
# 多线程并不一定能提高效率 实际上同一时间还是只有一个线程做运算，只不过是多个线程间的切换罢了
def job(l, q):
    res = sum(l)
    q.put(res)

def multithreading(l):
    q = Queue.Queue() 
    threads = []
    for i in range(4):
        t = threading.Thread(target=job, args=(copy.copy(l), q), name='T%i' % i)
        t.start()
        threads.append(t)
    [t.join() for t in threads]
    total = 0
    for _ in range(4):
        total += q.get()
    print(total)

def normal(l):
    total = sum(l)
    print(total)

if __name__ == '__main__':
    l = list(range(1000000))
    s_t = time.time()
    normal(l*4)
    print('normal: ',time.time()-s_t)
    s_t = time.time()
    multithreading(l)
    print('multithreading: ', time.time()-s_t)
