# 1
with open('text.txt', 'r+') as my_file:
    text = input('>>>')
    my_file.write(text)
    if text .isalpha():
        print(text, 'not a number')
    else:
        print(text, 'number')
# 2
text = input('Введите текст:')
my_file = open('DATA.txt', 'w')
my_file.write(text)
res = len(text.split())
print("The number of words in string are : ", len(text))
my_file.close()
# 3



# 4
class Bank_account:
    def __init__(self):
        print('1. просмотр баланса 2.внесение денег 3. снятие денег 4. отправка денег 0. Завершить оперпцию')
        int(input('Выберите операцию которую вы хотите сделать: '))
        self.balance = 0

    def deposit(self):
        amount = int(input("Введите сумму для депозита: "))
        self.balance += amount
        print("\n Внесенная сумма:", amount)

    def withdraw(self):
        int(input('Выберите операцию которую вы хотите сделать:'))
        amount = int(input("Введите сумму вывода: "))
        check_amount = self.balance - amount * 1.1
        if self.balance >= amount:
            self.balance -= amount
            print("\n Вы сняли:", amount)
        else:
            print("\n Недостаточно средств: "),
        my_file = open('withdraw_check.txt', 'w')
        my_file.write(
            'Your checklist:''\n' 'Money withdraw:' + ' ' + str(amount) + '\n' 'Your balance - 1%:'
            + ' ' + str(check_amount) + '\n')
        my_file.close()

    def check_balance(self):
        print('1. просмотр баланса 2.внесение денег 3. снятие денег 4. отправка денег 0. Завершить оперпцию')
        int(input('Выберите операцию который вы хотите сделать:'))
        print("\n Ваш баланс =", self.balance)

    def send_money(self):
        print('1. просмотр баланса 2.внесение денег 3. снятие денег 4. отправка денег 0. Завершить оперпцию')
        int(input('Выберите операцию который вы хотите сделать:'))
        card = int(input('Введите номер банкосвокой карты:'))
        amount = int(input('Введите колличетсво денег чтобы выслать:'))
        check_amount = self.balance - amount * 1.1
        if self.balance >= amount:
            self.balance -= amount
            print("\n Вы Отправили:", amount)
        else:
            print("\n Недостаточно средств: ")
        print("\n Ваш баланс =", self.balance)
        my_file = open('send_money_check.txt', 'w')
        my_file.write(
            'Your checklist:''\n' 'Your card ID:' + ' ' + str(card) + '\n''Money sent:' + ' ' + str(amount) + '\n' 
            'Your balance - 1%:' + ' ' + str(check_amount) + '\n')
        my_file.close()

    def stop(self):
        amount = int(input("Введите ноль чтобы завершить операцию:"))
        if amount == 0:
            print('Спасибо за выбор банкомата Академии!!!')








s = Bank_account()
s.deposit()
s.withdraw()
s.check_balance()
s.send_money()
s.stop()

# Exceptions
# 1
try:
    num = int(input("enter number: "))
except ValueError:
    print("you must enter an integer")

# 2
try:
    a = int(input('enter a:'))
    b = int(input('enter b:'))
    print(a / b)
except ZeroDivisionError:
    print('You cant divide by zero!!')
