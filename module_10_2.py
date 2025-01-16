import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power


    def run(self):
        enemy = 100
        days = 0
        print(f'{self.name}, на нас напали!')
        while enemy > 0:
            enemy -= self.power
            days += 1
            print(f'{self.name}, сражается {days} день(дня), осталось количество воинов {max(0, enemy)}\n')
            time.sleep(1)


        print(f'{self.name}, одержал победу спустя {days} дней(дня)!\n')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

thread1 = threading.Thread(target=first_knight.run)
thread2 = threading.Thread(target=second_knight.run)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print(f'Все битвы закончились!')
