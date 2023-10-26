from data import stock_data

stock_data()

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