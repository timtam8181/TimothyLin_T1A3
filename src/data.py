import math
import pyfiglet as pyg

def sector_averages(sector):
    sector_averages = {
        'healthcare': {'pe_ratio': 25, 'debt_to_equity': 0.6},
        'finance': {'pe_ratio': 10, 'debt_to_equity': 0.6},
        'energy': {'pe_ratio': 14, 'debt_to_equity': 0.5},
        'real_estate': {'pe_ratio': 11, 'debt_to_equity': 0.3},
        'retail': {'pe_ratio': 12, 'debt_to_equity': 0.7},
        'tech': {'pe_ratio': 13, 'debt_to_equity': 1},      

    } 

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

    analysis_data = {
        'pe_ratio': pe_ratio,
        'debt_to_equity': debt_to_equity,
        'free_cash_flow': free_cash_flow
    }

    print(f"Here are the company's metrics for your stock: {analysis_data}" )

    valuation = "0"
    expectations = "0"

    if sector_averages:
        if pe_ratio > sector_averages['pe_ratio']:
            valuation = "expensive"
            expectations = ["This means that investors expect higher than average growth in the future"]
        elif pe_ratio < sector_averages['pe_ratio']:
            valuation = "cheap"
            expectations = ["This means that investors expect lower than average growth in the future"]
        else:
            valuation = "fair"
            expectations = ["This means that the stock is a fair price relative to it's future growth prospects"]

    print(f"The stock is considered {valuation} relative to its industry peers. {expectations}. ")

    return analysis_data, valuation, expectations



