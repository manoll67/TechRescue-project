days = int(input())
room = input()
rating = input()

nights = days - 1
price = 0

# Базови цени
if room == "room for one person":
    price = nights * 18

elif room == "apartment":
    price = nights * 25
    if days < 10:
        price *= 0.70
    elif 10 <= days <= 15:
        price *= 0.65
    else:
        price *= 0.50

elif room == "president apartment":
    price = nights * 35
    if days < 10:
        price *= 0.90
    elif 10 <= days <= 15:
        price *= 0.85
    else:
        price *= 0.80

# Рейтинг
if rating == "positive":
    price *= 1.25
else:
    price *= 0.90

print(f"{price:.2f}")
