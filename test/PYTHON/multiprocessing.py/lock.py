#coding:utf-8  
# 只能用共享内存来存储数据 方便多个核之间调用数据  用全局变量行不通 
'''
value = mp.value('i')
arrary = mp.arrary('i',[1,2,3]) i 指的是数据的类型 有各种类型的表达方式 具体靠查
'''
import multiprocessing as mp
import time 

def job(v,num,l):
    l.acquire()  #把这个过程上锁
    for _ in range(10):
        time.sleep(0.1)
        v.value += num
        print(v.value)
    l.release()

def multicore():
    l = mp.Lock()
    v = mp.Value('i',0)
    p1 = mp.Process(target=job,args=(v,1,l))
    p2 = mp.Process(target=job,args=(v,3,l))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

if __name__ == "__main__":
    multicore()
