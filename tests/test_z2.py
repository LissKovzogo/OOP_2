import sys
import os

# tests/test_z2.py
import pytest
from oop_2.Zadania.z_2 import Account

def test_account_init_invalid():
    with pytest.raises(ValueError):
        Account("Иванов", "123", balance=-100)

def test_deposit(capsys):
    acc = Account("Иванов", "123", 5.0, 100.0)
    acc.deposit(50.0)
    assert acc.balance == 150.0
    captured = capsys.readouterr()
    assert "Внесено 50.00 руб." in captured.out

def test_withdraw_insufficient_funds(capsys):
    acc = Account("Иванов", "123", 5.0, 100.0)
    result = acc.withdraw(150.0)
    assert not result 
    assert acc.balance == 100.0
    captured = capsys.readouterr()
    assert "Недостаточно средств" in captured.out

def test_accrue_interest():
    acc = Account("Иванов", "123", 10.0, 1000.0)
    acc.accrue_interest()
    assert acc.balance == 1100.0

def test_amount_in_words():
    acc = Account(balance=1234.56)
    words = acc.amount_in_words()
    assert "одна тысяча двести тридцать четыре рубля" in words
    assert "пятьдесят шесть копеек" in words
