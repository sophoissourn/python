from tabulate import tabulate
def currency_converter():
  result = 0
  riel_rate = 4100.0

  exchange_rates = [
    ["usd", 4004.00, 4016.00],
    ["eur", 4610.30, 4777.03],
    ["aud", 2540.47, 2710.00],
    ["cad", 2505.65, 2940.11]
  ]
  
  print(f"====Daily Exchange Rates for KHM Riel=====")
  
  
  headers = ["Currency", "Buy", "Sell"]
  print(tabulate(exchange_rates, headers=headers, tablefmt="grid", colalign=("center", "left", "left")))
  
  print("*" * 40)
  # print("-" * 28)
  # print(f"{'Currency':<10}{'Buy':<10}{'Sell':<10}")
  # print("-" * 28)
  # for rate in exchange_rates:
  #   print(f"{rate[0].upper():<10}{rate[1]:<10}{rate[2]:<10}")
    
  exchanged_amount = 0
  flag = False
  buy_rate = 0
  str_rate = input("What currency do you want to buy? (USD, EUR, AUD, CAD): ").lower()
  for rate in exchange_rates:
    if str_rate in rate:
      flag = True
      buy_rate = rate[1]
      break
  
  if flag:  
    amount = float(input("How much do you want to buy RIEL ? : "))
    exchanged_amount = amount * buy_rate
    print(f"You bought KH Riel ៛{exchanged_amount:,.2f} Thank you")
      # break
  else:
    print("Please type currency correctly :(USD, EUR, AUD, CAD)")
      # break
  
  
def main():
  print("=====Welcome to Currency Converter with Python=====")
  while True:
    currency_converter()
    confirm = input("Type x to exit the program : ")
    if confirm.lower() == "x": break
  
main()