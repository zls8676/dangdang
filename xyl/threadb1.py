import time
import threading

def deadCircle():
    while True:
        print(1)
        time.sleep(1)

if __name__=="__main__":
    t = threading.Thread(target=deadCircle)
    t.start()
    print("aaa")