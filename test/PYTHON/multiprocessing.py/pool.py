#coding:utf-8  
#把所有进程放到池子里 让Python 自己去解决 
import multiprocessing as mp
import time 
# 进程池
def job(x):
    return x*x
#  注意 map 和 apply_async 之间的差别 map可以直接放入多个数据进行进程的迭代计算 而 apply_async一次只能放入一个数据到一个进程里运行
def multicore():
    t1 = time.time()
    pool = mp.Pool(processes=2)  # 输入多少就是用几个核 默认不输入则使用全部
    res = pool.map(job, range(1000))   #把进程和工作map在一起
    print(res)
    print("time = ",time.time() - t1 ) #核用的越多速度越慢？？
    res = pool.apply_async(job, (2,))  #只放入一个盒中 
    print(res.get())
    multi_res =[pool.apply_async(job, (i,)) for i in range(10)]  #迭代器 在列表中进行迭代
    print([res.get() for res in multi_res])

if __name__ == '__main__':
    multicore()