import datetime
while True:
     name = input("What is your name? ").strip()
 # Премахваме интервалите и проверяваме дали останалото са само букви
     if name.replace(" ", "").isalpha():
        break
     else:
        print("Please enter a valid name (letters only).")

# --- Проверка на възраст ---
while True:
    try:
        age = int(input("How old are you? "))
        break
    except ValueError:
        print("Please enter a number.")
    
x = datetime.datetime.now()
year = x.year + 100 - age
how_many_years = 100 - age 

if age <=0:
    print("You are not born yet.")
elif age == 100:
    print(f"{name} is already 100 years old.")
elif age > 100:
    print(f"{name} is already over 100 years old.")
else:
    print(f"{name} will be 100 years old in {how_many_years} years in {year}.")

