import threading
import time
import random

class BankAccount(threading.Thread):
    acc_balance=1000
    def __init__(self,name,money_request):
        threading.Thread.__init__(self)
        self.name=name
        self.money_request=money_request

    def run(self):
        thread_lock.acquire()
        BankAccount.get_money(self)
        thread_lock.release()

    @staticmethod
    def get_money(customer):
        print("{} tries to withdraw ${} at {}".format(customer.name,customer.money_request,time.strftime("%H:%M:%S",time.gmtime())))
        if BankAccount.acc_balance-customer.money_request>0:
            BankAccount.acc_balance-=customer.money_request
            print("New Account Balnace is : ${}".format(BankAccount.acc_balance))
        else:
            print("Not Enough money")
            print("Current Balance is : ${}".format(BankAccount.acc_balance))
        time.sleep(3)

thread_lock=threading.Lock()
yash=BankAccount("Yash",56)
preeti=BankAccount("Preeti",100)
sudhir=BankAccount("Sudhir",90)

yash.start()
preeti.start()
sudhir.start()

yash.join()
preeti.join()
sudhir.join()
