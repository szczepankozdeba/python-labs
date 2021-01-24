import threading
import random
import time


class filozof(threading.Thread):
    go = True

    def __init__(self, name, fork1, fork2):
        threading.Thread.__init__(self)
        self.name = name
        self.fork1 = fork1
        self.fork2 = fork2

    def run(self):
        while self.go:
            time.sleep(random.random())
            print(self.name, " czeka ")
            self.dine()

    def dine(self):
        while self.go:
            self.fork1.acquire(True)
            stuck = self.fork2.acquire(False)
            if stuck:
                break
            self.fork1.release()
            print(self.name, " zmienia sprzet")
            self.fork1, self.fork2 = self.fork2, self.fork1
        else:
            return

        self.dining()
        self.fork2.release()
        self.fork1.release()

    def dining(self):
        print(self.name, " je")
        time.sleep(random.random() * 5)
        print(self.name, " odklada sprzet")


forks = []
philosophers = []

for i in range(0, 5):
    forks.append(threading.Lock())

for i in range(0, 5):
    philosophers.append(filozof("Filozof " + str(i), forks[i % 5], forks[(i + 1) % 5]))

filozof.go = True
random.seed()

for i in range(0, 5):
    philosophers[i].start()

time.sleep(30)
filozof.go = False
print("koniec kolacji")