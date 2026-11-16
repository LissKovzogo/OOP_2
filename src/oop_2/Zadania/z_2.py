"""
Составить программу с использованием классов и объектов для решения задачи.
Во всех заданиях, помимо указанных в задании операций, обязательно должны быть реализованы следующие методы:
метод инициализации __init__ ;
ввод с клавиатуры read;
вывод на экран display.
9. Реализовать класс Account, представляющий собой банковский счет.
В классе должны быть четыре поля: фамилия владельца, номер счета,
процент начисления и сумма в рублях. Открытие нового счета выполняется операцией инициализации.
Необходимо выполнять следующие операции: 
сменить владельца счета, 
снять некоторую сумму денег со счета, 
положить деньги на счет, 
начислить проценты, 
перевести сумму в доллары, 
перевести сумму в евро, 
получить сумму прописью.

"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Account:
    def __init__(self, surname="", account_number="", interest_rate=0.0, balance=0.0):
        if not isinstance(balance, (int, float)) or balance < 0:
            raise ValueError("Сумма на счете не может быть отрицательной.")
        if not isinstance(interest_rate, (int, float)) or interest_rate < 0:
            raise ValueError("Процент начисления не может быть отрицательным.")

        self.surname = surname
        self.account_number = account_number
        self.interest_rate = interest_rate
        self.balance = float(balance)

    def read(self):
        print( "Введите данные счета:")
        self.surname = input("Фамилия владельца: ")
        self.account_number = input("Номер счета: ")
        try:
            self.interest_rate = float(input("Процент начисления: "))
            self.balance = float(input("Сумма в рублях: "))
            if self.balance < 0 or self.interest_rate < 0:
                raise ValueError
        except ValueError:
            print("Ошибка: введены некорректные числовые данные.")
            exit(1)

    def display(self):
        print(f"Владелец: {self.surname}")
        print(f"Номер счета: {self.account_number}")
        print(f"Процент начисления: {self.interest_rate}%")
        print(f"Баланс: {self.balance:.2f} руб.")

    def change_owner(self, new_surname):
        if not new_surname:
            raise ValueError("Фамилия не может быть пустой.")
        self.surname = new_surname
        print(f"Владелец счета изменен на: {self.surname}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной.")
        if amount > self.balance:
            print("Недостаточно средств на счете.")
            return False
        self.balance -= amount
        print(f"Снято {amount:.2f} руб. Остаток: {self.balance:.2f} руб.")
        return True

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной.")
        self.balance += amount
        print(f"Внесено {amount:.2f} руб. Новый баланс: {self.balance:.2f} руб.")

    def accrue_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        print(f"Начислено процентов: {interest:.2f} руб. Новый баланс: {self.balance:.2f} руб.")

    def to_dollars(self, rate=90.0):
        return self.balance / rate

    def to_euros(self, rate=100.0):
        return self.balance / rate

    def amount_in_words(self):
        units = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
        teens = ["десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать",
                 "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
        tens = ["", "", "двадцать", "тридцать", "сорок", "пятьдесят",
                "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
        hundreds = ["", "сто", "двести", "триста", "четыреста",
                    "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]

        def three_digits_to_words(num):
            if num == 0:
                return ""
            result = []
            if num >= 100:
                result.append(hundreds[num // 100])
                num %= 100
            if 10 <= num < 20:
                result.append(teens[num - 10])
            else:
                if num >= 20:
                    result.append(tens[num // 10])
                    num %= 10
                if num > 0:
                    result.append(units[num])
            return " ".join(result)

        def num_to_words(n):
            if n == 0:
                return "ноль"

            result = []
            if n >= 1000000:
                millions = n // 1000000
                n %= 1000000
                m_text = three_digits_to_words(millions)
                if 11 <= millions % 100 <= 19:
                    m_end = "миллионов"
                elif millions % 10 == 1:
                    m_end = "миллион"
                elif 2 <= millions % 10 <= 4:
                    m_end = "миллиона"
                else:
                    m_end = "миллионов"
                result.append(f"{m_text} {m_end}")

            if n >= 1000:
                thousands = n // 1000
                n %= 1000
                th_text = three_digits_to_words(thousands)
                th_text = th_text.replace("один", "одна").replace("два", "две")
                if 11 <= thousands % 100 <= 19:
                    th_end = "тысяч"
                elif thousands % 10 == 1:
                    th_end = "тысяча"
                elif 2 <= thousands % 10 <= 4:
                    th_end = "тысячи"
                else:
                    th_end = "тысяч"
                result.append(f"{th_text} {th_end}")

            if n > 0:
                result.append(three_digits_to_words(n))

            return " ".join(result)

        rubles = int(self.balance)
        kopecks = int(round((self.balance - rubles) * 100))

        rub_text = num_to_words(rubles)
        kop_text = num_to_words(kopecks)

        if 11 <= rubles % 100 <= 19:
            rub_end = "рублей"
        elif rubles % 10 == 1:
            rub_end = "рубль"
        elif 2 <= rubles % 10 <= 4:
            rub_end = "рубля"
        else:
            rub_end = "рублей"

        if 11 <= kopecks % 100 <= 19:
            kop_end = "копеек"
        elif kopecks % 10 == 1:
            kop_end = "копейка"
        elif 2 <= kopecks % 10 <= 4:
            kop_end = "копейки"
        else:
            kop_end = "копеек"

        return f"{rub_text} {rub_end} {kop_text} {kop_end}"


if __name__ == '__main__':

    # Создание счета
    acc = Account("Иванов И.И.", "40817810099910004312", 5.0, 15000.50)
    acc.display()

    #Смена владельца
    acc.change_owner("Петров П.П.")
    acc.display()

    #Пополнение счета
    acc.deposit(5000)
    acc.display()

    #Снятие средств
    acc.withdraw(2000)
    acc.display()

    #Начисление процентов
    acc.accrue_interest()
    acc.display()

    #Перевод в валюту
    print(f"Сумма в долларах: {acc.to_dollars():.2f} USD")
    print(f"Сумма в евро: {acc.to_euros():.2f} EUR")

    #Сумма прописью
    print(acc.amount_in_words())

    #Ввод нового счета с клавиатуры
    new_acc = Account()
    new_acc.read()
    new_acc.display()
    print(f"Сумма прописью: {new_acc.amount_in_words()}")
