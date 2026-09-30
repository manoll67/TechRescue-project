nylon_sqaer = 1.5
paint_liters = 14.5
thinner_liter = 5


nylon = int (input())
paynt = int (input()) 
thenner = int(input())
hours = int(input())

total_nylon = (nylon + 2) * nylon_sqaer
total_paint = (paynt * 1.1) * paint_liters
total_thinner = thenner * thinner_liter
total_materials = total_nylon + total_paint + total_thinner + 0.40
total_pay = (total_materials * 0.30) * hours
total_sum = total_materials + total_pay
print(total_sum)