type_flauars = input()
number_flauars = int(input())
budget = float(input())
praise_flauars = 0

if type_flauars == "Roses":
    praise_flauars = number_flauars * 5
    if number_flauars > 80:
        praise_flauars *= 0.90
elif type_flauars == "Dahlias":
    praise_flauars = number_flauars * 3.80
    if number_flauars > 90:
        praise_flauars *= 0.85
elif type_flauars == "Tulips":
    praise_flauars = number_flauars * 2.80
    if number_flauars > 80:
        praise_flauars *= 0.85
elif type_flauars == "Narcissus":
    praise_flauars = number_flauars * 3
    if number_flauars < 120:
        praise_flauars *= 1.15
elif type_flauars == "Gladiolus":
    praise_flauars = number_flauars * 2.50
    if number_flauars < 80:
        praise_flauars *= 1.20


if budget >= praise_flauars:
    print(f"Hey, you have a great garden with {number_flauars} {type_flauars} and {budget - praise_flauars:.2f} leva left.")
else:
    print(f"Not enough money, you need {praise_flauars - budget:.2f} leva more.")   

#Да се отпечата на конзолата на един ред:
#• Ако бюджетът им е достатъчен - "Hey, you have a great garden with {броя цвета} {вид цветя} and {останалата сума} leva left.";
#• Ако бюджета им е НЕ достатъчен - "Not enough money, you need {нужната сума} leva more."
# 
#

#newHouse.py -newVersion1
type_flauars = input()
number_flauars = int(input())
budget = float(input())

prices = {
    "Roses": 5,
    "Dahlias": 3.80,
    "Tulips": 2.80,
    "Narcissus": 3,
    "Gladiolus": 2.50
}

price = number_flauars * prices[type_flauars]

# Отстъпки / надценки
if type_flauars == "Roses" and number_flauars > 80:
    price *= 0.90
elif type_flauars == "Dahlias" and number_flauars > 90:
    price *= 0.85
elif type_flauars == "Tulips" and number_flauars > 80:
    price *= 0.85
elif type_flauars == "Narcissus" and number_flauars < 120:
    price *= 1.15
elif type_flauars == "Gladiolus" and number_flauars < 80:
    price *= 1.20

diff = budget - price

if diff >= 0:
    print(f"Hey, you have a great garden with {number_flauars} {type_flauars} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {-diff:.2f} leva more.")

