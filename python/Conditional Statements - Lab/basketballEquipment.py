#fee_for_one_year = int(input())

#basketball_sneakers = fee_for_one_year - (fee_for_one_year * 0.40)
#basketball_team = basketball_sneakers - (basketball_sneakers * 0.20)
#basketball_ball = basketball_team / 4
#basketball_accessories = basketball_ball / 5
#total_fee = fee_for_one_year + basketball_sneakers + basketball_team + basketball_ball + basketball_accessories
#print(round(total_fee, 2))

#Invalid Number
#number = int(input())
#valid_number = [i for i in range(100, 201)] + [0]
#if number not in valid_number:
#    print("invalid")

#Fruit Shop
fruid = input()
deyOfWeek = input()
quantity = float(input())
work_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday",]
weekend = ["Saturday", "Sunday"]

if fruid == "banana" and deyOfWeek in work_days:
    print(f"{2.50 * quantity:.2f}")
elif fruid == "banana" and deyOfWeek in weekend:
    print(f"{2.70 * quantity:.2f}")
elif fruid == "apple" and deyOfWeek in work_days:
    print(f"{1.20 * quantity:.2f}")
elif fruid == "apple" and deyOfWeek in weekend:
    print(f"{1.25 * quantity:.2f}")
elif fruid == "orange" and deyOfWeek in work_days:
    print(f"{0.85 * quantity:.2f}")
elif fruid == "orange" and deyOfWeek in weekend:
    print(f"{0.90 * quantity:.2f}")
elif fruid == "grapefruit" and deyOfWeek in work_days:
    print(f"{1.45 * quantity:.2f}")
elif fruid == "grapefruit" and deyOfWeek in weekend:
    print(f"{1.60 * quantity:.2f}")
elif fruid == "kiwi" and deyOfWeek in work_days:
    print(f"{2.70 * quantity:.2f}")
elif fruid == "kiwi" and deyOfWeek in weekend:
    print(f"{3.00 * quantity:.2f}")
elif fruid == "pineapple" and deyOfWeek in work_days:
    print(f"{5.50 * quantity:.2f}")
elif fruid == "pineapple" and deyOfWeek in weekend:
    print(f"{5.60 * quantity:.2f}")
elif fruid == "grapes" and deyOfWeek in work_days:
    print(f"{3.85 * quantity:.2f}" )
elif fruid == "grapes" and deyOfWeek in weekend:
    print(f"{4.20 * quantity:.2f}")
else:
    print("error")


#Fruit Shop - new version

fruit = input()
day = input()
quantity = float(input())

work_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekend = ["Saturday", "Sunday"]

prices = {
    "work": {
        "banana": 2.50,
        "apple": 1.20,
        "orange": 0.85,
        "grapefruit": 1.45,
        "kiwi": 2.70,
        "pineapple": 5.50,
        "grapes": 3.85
    },
    "weekend": {
        "banana": 2.70,
        "apple": 1.25,
        "orange": 0.90,
        "grapefruit": 1.60,
        "kiwi": 3.00,
        "pineapple": 5.60,
        "grapes": 4.20
    }
}

# Определяме типа ден
if day in work_days:
    day_type = "work"
elif day in weekend:
    day_type = "weekend"
else:
    print("error")
    exit()

# Проверка за валиден плод
if fruit not in prices[day_type]:
    print("error")
else:
    price = prices[day_type][fruit] * quantity
    print(f"{price:.2f}")


