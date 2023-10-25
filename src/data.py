import math
import pyfiglet as pyg

def greeting():
    welcome = pyg.figlet_format("Welcome to stock analysis!")
    print(welcome)
    stock = input('Choose a stock you would like to analyse!: ')
    print(f'Great!, today we will analyse {stock}')

def stock_data():
    sector = input("Enter the sector of the company: ")
    revenue = float(input("Enter the company's revenue: "))
    expenses = float(input("Enter the company's expense: "))
    operating_cash_flow = float(input("Enter the company's operating cash flow: "))
    capital_expenditure = float(input("Enter the company's capital_expenditure: "))
    assets = float(input("Enter the company's assets: "))
    liabilities = float(input("Enter the company's liabilities: "))
    market_capitalisation = float(input("Enter the company's market cap: "))

    profit = revenue - expenses
    pe_ratio = market_capitalisation / profit if profit != 0 else 0
    debt_to_equity = liabilities / (assets - liabilities) if assets != 0 else 0
    free_cash_flow = operating_cash_flow - capital_expenditure


def stock_analysis():
    pass

greeting()
stock_data()