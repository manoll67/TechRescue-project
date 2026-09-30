mount = input().title()
days = int(input())

if mount == "May" or mount == "October":
    price_studio = 50
    price_apartment = 65
    if days > 14:
        price_studio *= 0.7
        price_apartment *= 0.9
    elif days > 7:
        price_studio *= 0.95
elif mount == "June" or mount == "September":
    price_studio = 75.20
    price_apartment = 68.70
    if days > 14:
        price_studio *= 0.8
        price_apartment *= 0.9
elif mount == "July" or mount == "August":
    price_studio = 76
    price_apartment = 77
    if days > 14:
        price_apartment *= 0.90

print(f"Apartment: {price_apartment * days:.2f} lv.\nStudio: {price_studio * days:.2f} lv.")



