
from time import sleep
import threading
from random import randint
from threading import Thread, Lock



class Bank:
    def __init__(self, balance: int = 0, lock: Lock = Lock()):
         self.balance = balance  # баланс банка
         self.lock = lock


    def deposit(self):
        for i in range(100):
            refill = randint(50, 500)  # Пополнение - это увеличение баланса на случайное целое число от 50 до 500.
            self.balance += refill
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {refill}. Баланс: {self.balance}\n')
            sleep(0.001)

    def take(self):
        for i in range(100):
            Withdrawal = randint(50, 500)  #Снятие - это уменьшение баланса на случайное целое число от 50 до 500.
            print(f'Запрос на {Withdrawal}\n')
            if self.balance >= Withdrawal:
                self.balance -= Withdrawal
                print(f'Снятие: {Withdrawal}. Баланс: {self.balance}\n')
            else:
                print('Запрос отклонён, недостаточно средств\n')
                self.lock.acquire()
                sleep(0.001)

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()


th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
