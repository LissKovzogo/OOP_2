import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Zadania')))
# tests/test_z1.py
import pytest
from z_1 import Pair, make_time

def test_pair_init_valid():
    p = Pair(2, 30)
    assert p.minutes() == 150

def test_pair_init_invalid_minutes():
    with pytest.raises(ValueError):
        Pair(1, 60)

def test_pair_read(monkeypatch):
    p = Pair()
    monkeypatch.setattr('builtins.input', lambda: "3 45")
    p.read()
    assert p.minutes() == 225

def test_make_time_error(capsys):
    with pytest.raises(SystemExit) as exc_info:
        make_time(-5, 30)
    assert exc_info.value.code == 1
    captured = capsys.readouterr()
    assert "Аргументы должны быть положительными" in captured.out