chicken_menu = 10.35
fish_menu = 12.40
vegan_menu = 8.15
delivery = 2.50


number_chicken = int(input())
number_fish = int(input())
number_vegan = int(input())
prays_for_chicken = number_chicken * chicken_menu
prays_for_fish = number_fish * fish_menu
prays_for_vegan = number_vegan * vegan_menu


total_price = prays_for_chicken + prays_for_fish + prays_for_vegan 
desert = 0.20 * total_price
total_sum = total_price + desert + delivery
print(round(total_sum, 2))
