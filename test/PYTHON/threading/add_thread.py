import threading
from time import sleep

def thread_job():
    print("hello")
    for i in range(10):
        sleep(0.1)
    print("bye")

def main():
    added_thread = threading.Thread(target=thread_job)  #添加一个线程
    print(threading.active_count())# 算出当前几个激活的线程
    print(threading.enumerate()) #查看当前的是哪几个线程
    print(threading.current_thread())

    added_thread.start()#开始线程
    added_thread.join()#同步
    print("all done")
 
if __name__ == "__main__":
    main()