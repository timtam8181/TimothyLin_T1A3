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
    return sector_averages.get(sector, {})

# def greeting():
#     welcome = pyg.figlet_format("Welcome to stock analysis!")
#     print(welcome)
#     stock = input('Choose a stock you would like to analyse!: ')
#     print(f'Great!, today we will analyse {stock}')

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number!")

def stock_data():
    sector = None
    while sector not in {'healthcare', 'finance', 'energy', 'real_estate', 'retail', 'tech'}:
        sector = input("Enter the sector of your company (healthcare, finance, energy, real_estate, retail, tech): ")
        
        if sector not in ['healthcare', 'finance', 'energy', 'real_estate', 'retail', 'tech']:
            print("The sector of your company needs to be from (healthcare, finance, energy, real_estate, retail)")

    revenue = get_float_input("Enter the company's revenue: ")
    expenses = get_float_input("Enter the company's expense: ")
    operating_cash_flow = get_float_input("Enter the company's operating cash flow: ")
    capital_expenditure = get_float_input("Enter the company's capital_expenditure: ")
    assets = get_float_input("Enter the company's assets: ")
    liabilities = get_float_input("Enter the company's liabilities: ")
    market_capitalisation = get_float_input("Enter the company's market cap: ")

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

    sector_averages_data = sector_averages(sector)

    if sector_averages_data:
        if pe_ratio > sector_averages_data['pe_ratio']:
            valuation = "expensive"
            expectations = ["This means that investors expect higher than average growth in the future"]
        elif pe_ratio < sector_averages_data['pe_ratio']:
            valuation = "cheap"
            expectations = ["This means that investors expect lower than average growth in the future"]
        else:
            valuation = "fair"
            expectations = ["This means that the stock is a fair price relative to it's future growth prospects"]

    print(f"The stock is considered {valuation} relative to its industry peers. {expectations}. ")

    return analysis_data, valuation, expectations

# def main():
#     all_results = []
#     while True:
#         result= stock_data()
#         all_results.append(result)

#         another = input("Would you like to analyse another stock? (yes/nno): ")
#         if another.lower() != "yes":
#             break

#     print("Here is a summary of the results")
#     for i, result in enumerate(all_results, 1):
#         metrics, valuation, Exception = result
#         print(f"{i}. Metrics: {metrics}, Valuation: {valuation}, Expectations: {expectations}")

# main()

