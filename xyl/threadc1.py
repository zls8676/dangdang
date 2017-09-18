import threading
import time

class MyThreadC(threading.Thread):

    def __init__(self):
        super(MyThreadC, self).__init__()

    def run(self):
        while True:
            print(1)
            time.sleep((1))
if __name__=="__main__":
    t = MyThreadC()
    t.start()
    print("aaa")