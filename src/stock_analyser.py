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

def greeting():
    welcome = pyg.figlet_format("Welcome to stock analysis!")
    print(welcome)

def get_stock_name():
    return input("Enter the name of the stock you would like to analyse: ")

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number!")

def save_results_to_file(analysis_data, valuation, expectations, stock_name):
    try:    
        with open("analysis_results.txt", "a") as file:
            file.write("\n")
            file.write(f"Stock: {stock_name}\n")
            file.write(f"PE Ratio: {analysis_data['pe_ratio']}\n")
            file.write(f"Debt to equity: {analysis_data['debt_to_equity']}\n")
            file.write(f"Free Cash Flow: {analysis_data['free_cash_flow']}\n")
            file.write(f"Valuation: {valuation}\n")
            file.write(f"Expectations: {expectations}\n")
    except IOError as e:
        print(f"Error: {e}")

def stock_data():
    try:
        while True:
            stock_name = get_stock_name()
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
                'pe_ratio': round(pe_ratio, 2),
                'debt_to_equity': round(debt_to_equity, 2),
                'free_cash_flow': round(free_cash_flow, 2)
            }

            print(f"Here are the company's metrics for your stock: {analysis_data}" )

            valuation = "0"
            expectations = "0"

            sector_averages_data = sector_averages(sector)

            if sector_averages_data:
                if pe_ratio > sector_averages_data['pe_ratio']:
                    valuation = "expensive"
                    expectations = "This means that investors expect higher than average growth in the future"
                elif pe_ratio < sector_averages_data['pe_ratio']:
                    valuation = "cheap"
                    expectations = "This means that investors expect lower than average growth in the future"
                else:
                    valuation = "fair"
                    expectations = "This means that the stock is a fair price relative to it's future growth prospects"

            sector_averages_data = sector_averages(sector)

            observation = "0"
            debt_levels = "0"

            if sector_averages_data:
                if debt_to_equity > sector_averages_data['debt_to_equity']:
                    debt_levels = "high"
                    observation = "Careful! This company is highly leveraged compared to its peers."
                elif debt_to_equity < sector_averages_data['debt_to_equity']:
                    debt_levels = "low"
                    observation = "This company does not have much debt compared to its peers."
                else:
                    debt_levels = "average"
                    observation = "This company has a fair amount of debt compared to its peers."

            sector_averages_data = sector_averages(sector)

            cash_flow_levels = "0"
            outlook = "0"

            if sector_averages_data:
                if free_cash_flow < 0:
                    cash_flow_levels = "negative"
                    outlook = "Careful! This company does not produce postive cash flow, meaning it will have to raise capital or increase debt when they run out of cash! "
                elif free_cash_flow >= 0:
                    cash_flow_levels = "positive"
                    outlook = "Great! this company produces enough cash flow to be self sustaining! It can use this cash to invest, expand or pay shareholders!."

                print(f"The stock is considered {valuation} relative to its industry peers. {expectations}. ")
                print(f"Also, this company has {debt_levels} debt levels. {observation} ")
                print(f"Finally, this company has {cash_flow_levels} cash flows. {outlook} ")
        
            save_results_to_file(analysis_data, valuation, expectations, stock_name)

            another_company = input("Do you want to analyze another company? (y/n): ")
            if another_company.upper() != "Y":
                break

        return analysis_data, valuation, expectations,

    except KeyboardInterrupt:
        print("\nAnalysis was interrupted.")
    except Exception as e:
        print(f"An error occurred: {e}")        
