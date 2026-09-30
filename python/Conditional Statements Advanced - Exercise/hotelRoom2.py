mount = input().title() 
days = int(input()) 

if mount == "May" or mount == "October":
    price_studio = 50
    price_apartment = 65
    if days > 14:
        price_studio *= 0.7  # 30% намаление
        price_apartment *= 0.9
    elif days > 7:
        price_studio *= 0.95  # 5% намаление

elif mount == "June" or mount == "September":
    price_studio = 75.20
    price_apartment = 68.70
    if days > 14:
        price_studio *= 0.8   # 20% намаление
        price_apartment *= 0.9  # 10% намаление

elif mount == "July" or mount == "August":
    price_studio = 76
    price_apartment = 77
    if days > 14:
        price_apartment *= 0.9  # 10% намаление

# Печата демо цените
print(f"Apartment: {price_apartment * days:.2f} lv.")
print(f"Studio: {price_studio * days:.2f} lv.")