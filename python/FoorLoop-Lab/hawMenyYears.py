import datetime

def menu():
    print("\n=== MAIN MENU ===")
    print("1. Calculate when you will turn 100")
    print("2. Show current date and time")
    print("3. Exit")

def get_valid_name():
    while True:
        name = input("Enter your name: ").strip()
        if name.replace(" ", "").isalpha():
            return name
        else:
            print("Invalid name. Use letters only.")

def get_valid_age():
    while True:
        try:
            age = int(input("Enter your age: "))
            return age
        except ValueError:
            print("Please enter a number.")

def calculate_100_years():
    name = get_valid_name()
    age = get_valid_age()

    now = datetime.datetime.now()
    year_100 = now.year + (100 - age)

    if age <= 0:
        print("You are not born yet.")
    elif age == 100:
        print(f"{name} is already 100 years old.")
    elif age > 100:
        print(f"{name} is already over 100 years old.")
    else:
        print(f"{name} will turn 100 years old in the year {year_100}.")

def show_datetime():
    now = datetime.datetime.now()
    print(f"Current date and time: {now}")

# --- MAIN PROGRAM LOOP ---
while True:
    menu()
    choice = input("Choose an option (1-3): ")

    if choice == "1":
        calculate_100_years()
    elif choice == "2":
        show_datetime()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again.")

    input("Press Enter to continue...")