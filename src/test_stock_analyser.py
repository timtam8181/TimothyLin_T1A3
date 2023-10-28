import pytest

from stock_analyser import get_float_input, sector_averages

def test_sector_averages():
    assert sector_averages('tech') == {'pe_ratio': 13, 'debt_to_equity': 1} 
    assert sector_averages('not_a_sector') == {}

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number!")

if __name__ == "__main__":
    get_float_input("Enter a number: ")

# TEST

def test_get_float_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "10")
    prompt = get_float_input("Enter a number: ")
    assert prompt == 10.0