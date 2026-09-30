n1 = int(input())
n2 = int(input())
operator = input()
result = 0  

if operator == "+":
    result = n1 + n2
elif operator == "-":
    result = n1 - n2
elif operator == "*":
    result = n1 * n2
elif operator == "/":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
        exit()
    result = n1 / n2
elif operator == "%":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
        exit()
    result = n1 % n2
else:
    print("Invalid operator")
    exit()

if operator in ["+", "-", "*"]:
    if result % 2 == 0:
        print(f"{n1} {operator} {n2} = {result} - even")
    else:
        print(f"{n1} {operator} {n2} = {result} - odd")
elif operator == "/":
    print(f"{n1} {operator} {n2} = {result:.2f}")
else:  # operator == "%"
    print(f"{n1} {operator} {n2} = {result}")

