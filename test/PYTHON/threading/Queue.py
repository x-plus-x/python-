import threading
import time
import Queue

#队列和线程之间搭配

def job(l,q):
    for i in range(len(l)):
        l[i] = l[i]**2
    q.put(l)

def multithreading():
    q = Queue.Queue()
    threads = []
    data = [[1,2,3],[3,4,5],[4,4,4],[5,5,5]]
    for i in range(4):  
        t = threading.Thread(target=job, args=(data[i], q))   # 运行每一个线程
        t.start()
        threads.append(t)  #将线程添加到列表中
    for thread in threads:
        thread.join()  #在一起join
    results = []
    for _ in range(4):
          results.append(q.get())
    print(results)

if __name__ == '__main__':
    multithreading()