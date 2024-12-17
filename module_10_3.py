import  threading
from threading import Thread, Lock
import random
import time


class Bank(Thread):

    def __init__(self):
        super().__init__()
        self.balance = 0
        self.lock = Lock()

# Поток "депозит"
    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            y = random.randint(50, 500)
            self.balance += y
            print(f'Пополнение: {y}. Баланс: {self.balance}')

            # ожидание в 0.001 секунды, имитация скорости выполнения пополнения
            time.sleep(0.001)

# Поток "брать"
    def take(self):
        for i in range(100):
            x = random.randint(50, 500)
            print(f'Запрос на {x}')
            if self.balance >= x:
                self.balance -= x
                print(f'Снятие: {x}. Баланс {self.balance}')
            else:
                print(f'Запрос отклонен, недостаточно средств')
                self.lock.acquire()
            time.sleep(0.001)


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')




