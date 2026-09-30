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

def insert_birthday():
    while True:
        try:
            day = int(input("Enter your birth day (1-31): "))
            month = int(input("Enter your birth month (1-12): "))
            year = int(input("Enter your birth year (e.g. 1990): "))

            birth_date = datetime.date(year, month, day)
            return birth_date
        except ValueError:
            print("Invalid date. Please try again.")

today = datetime.date.today()
def calculate_100_years():
    name = get_valid_name()
    birth_date = insert_birthday()

    hundred_birthday = datetime.date(birth_date.year + 100, birth_date.month, birth_date.day)
    time_left = hundred_birthday - today

    if today > hundred_birthday:
        print(f"{name} is already over 100 years old.")
    elif today == hundred_birthday:
        print(f"Congratulations {name}! You are 100 years old today!")
    else:
        print(f"{name} will turn 100 years old on {hundred_birthday}.")
        print(f"That is in {time_left.days} days.")
 
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