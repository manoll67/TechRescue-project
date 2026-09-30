pacetable_chemicals = 5.8
pacetable_markers = 7.2
cleaning = 1.2
number_of_chemicals = int(input())
number_of_markers = int(input())
liter_of_cleaning = int(input())
persent_discount = int(input())


total_chemicals_price = number_of_chemicals * pacetable_chemicals
total_markers_price = number_of_markers * pacetable_markers
total_cleaning_price = liter_of_cleaning * cleaning
total_price = total_chemicals_price + total_markers_price + total_cleaning_price
oll_price = total_price - (total_price * (persent_discount / 100))
print(oll_price)
