price_excursion = float(input()) # price of excursion
price_puzzle = float(input()) #* 2.60 # price of puzzle
price_doll = float(input()) #* 3.00 # price of doll
price_bear = float(input()) #* 4.10 # price of bear
price_minion = float(input()) #* 8.20 # price of minion
price_truck = float(input()) #* 2.00 # price of truck

total_price =  (price_puzzle * 2.60)+ (price_doll * 3.00)+ (price_bear * 4.10)+ (price_minion * 8.20)+ (price_truck * 2.00) # total price of toys
total_toys = price_puzzle + price_doll + price_bear + price_minion + price_truck
if total_toys >= 50:
    total_price = total_price - (total_price * 0.25) # discount
total_price = total_price - (total_price * 0.10) # rent
if total_price >= price_excursion:
    print(f"Yes! {total_price - price_excursion:.2f} lv left.")
else:
    print(f"Not enough money! {price_excursion - total_price:.2f} lv needed.")


