from colorama import Fore, init
init()

print(Fore.RED + "Simple Calculator")

print(Fore.GREEN + "===CALCULATOR===")
print(Fore.LIGHTBLACK_EX + "1. Addition")
print(Fore.LIGHTBLACK_EX + "2. Subtraction") 
print(Fore.LIGHTBLACK_EX + "3. Multiplication")
print(Fore.LIGHTBLACK_EX + "4. Division")
print(Fore.LIGHTBLACK_EX + "5. Exit")

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Try again.")


def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero is not allowed."

while True:
    choice = input("Choose an operation (1-5): ")

    if choice == '5':
        print("Exiting the calculator. Goodbye!")
        break

    if choice in ['1', '2', '3', '4']:
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")

        if choice == '1':
            result = addition(num1, num2)
            print(f"The result of {num1} + {num2} is: {result}")
        elif choice == '2':
            result = subtraction(num1, num2)
            print(f"The result of {num1} - {num2} is: {result}")
        elif choice == '3':
            result = multiplication(num1, num2)
            print(f"The result of {num1} * {num2} is: {result}")
        elif choice == '4':
            result = division(num1, num2)
            print(f"The result of {num1} / {num2} is: {result}")
    else:
        print("Invalid choice. Please select a valid operation (1-5).")


