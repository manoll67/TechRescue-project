import secrets
import string


def show_menu():
    print("\n=== Password Generator ===")
    print("1. Generate Password")
    print("2. Save Password")  # --- IGNORE ---
    print("3. Exit")


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(characters) for _ in range(length))
    return password


while True:
    show_menu()
    choice = input("Enter your choice (1-3): ").strip()

    if choice == "1":
        # Цикъл за валидация на дължината
        while True:
            try:
                length = int(
                    input("Enter the desired password length (8-20): ")
                )
                if 8 <= length <= 20:
                    break  # Излиза от цикъла за дължина, Продължава надолу
                else:
                    print("Please enter a number between 8 and 20.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Генериране и показване
        password = generate_password(length)
        print(f"\n🔑 Generated password: {password}")
        # Забележка: Тук НЯМА break, за да може менюто да се покаже пак.

    elif choice == "2":
        # Логика за запазване на паролата (може да се разшири)
        print("Saving password...")
        password_to_save = input("Enter the password you want to save: ").strip()
        # Тук можеш да добавиш валидация за паролата, ако   
        # Тук можеш да добавиш логика за запазване на паролата в файл или база данни

    elif choice == "3":
        print("Exiting the password generator. Goodbye!")
        break  # Излиза от главния while цикъл и затваря програмата

    else:
        print("Invalid choice. Please select a valid option (1-3).")