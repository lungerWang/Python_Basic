import threading
import time

glo_num = 100

class MyThread(threading.Thread):

    def run(self):
        for i in range(5):
            print("MyThread %d" % i)


def sing():
    global glo_num
    glo_num += 1
    for i in range(5):
        print("sing %d" % i)


def dance():
    global glo_num
    glo_num += 1
    print("dance glo_num = %d" % glo_num)
    for i in range(5):
        print("dance" + str(i))


def main():
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    time.sleep(1)
    t2.start()
    t3 = MyThread()
    t3.start()
    print(threading.enumerate())


if __name__ == "__main__":
    main()