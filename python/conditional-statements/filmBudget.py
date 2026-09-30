# budget for the film
film_budget = float(input())   
# number of extras
number_of_extras = int(input()) 
# price of clothing per extra
clothing_price_per_extra = float(input()) 
# price of decor is 10% of the film budget
decor_price = film_budget * 0.10 
# total price of clothing for all extras
clothing_price = number_of_extras * clothing_price_per_extra 

if number_of_extras > 150:
    clothing_price *= 0.90   
total_expenses = decor_price + clothing_price        # total expenses for the film

if total_expenses > film_budget:
 print("Not enough money!")
 print(f"Wingard needs {total_expenses - film_budget:.2f} leva more.")
else:
 print("Action!")
 print(f"Wingard starts filming with {film_budget - total_expenses:.2f} leva left.")
