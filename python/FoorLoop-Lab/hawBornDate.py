import datetime

# --- Въвеждане на име ---
while True:
    name = input("What is your name? ").strip()
    if name.replace(" ", "").isalpha():
        break
    else:
        print("Please enter a valid name (letters only).")

# --- Въвеждане на рожденна дата ---
while True:
    try:
        day = int(input("Enter your birth day (1-31): "))
        month = int(input("Enter your birth month (1-12): "))
        year = int(input("Enter your birth year (e.g. 1990): "))

        birth_date = datetime.date(year, month, day)
        break
    except ValueError:
        print("Invalid date. Please try again.")

# --- Текуща дата ---
today = datetime.date.today()

# --- Дата, когато става на 100 ---
hundred_birthday = datetime.date(year + 100, month, day)

# --- Разлика ---
time_left = hundred_birthday - today

# --- Логика ---
if today > hundred_birthday:
    print(f"{name} is already over 100 years old.")
elif today == hundred_birthday:
    print(f"Congratulations {name}! You are 100 years old today!")
else:
    print(f"{name} will turn 100 years old on {hundred_birthday}.")
    print(f"That is in {time_left.days} days.")
