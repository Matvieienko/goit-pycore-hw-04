from colorama import Fore, init

init(autoreset=True) # Автоматично скидається стиль до стандартного

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()  # Приведення команди до нижнього регістру
    return cmd, args

# Функція для створення контакту
def add_contact(args, contacts):
    # Перевірка кількості аргументів
    if len(args) != 2:
        return Fore.RED + "Invalid input. Use format: add [name] [phone]"
    
    name, phone = args
    contacts[name] = phone
    return Fore.GREEN + f"Contact '{name}' added."

# Функція для зміни контакту
def change_contact(args, contacts):
    if len(args) != 2:
        return Fore.RED + "Invalid input. Use format: change [name] [new_phone]"
    
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return Fore.GREEN + f"Contact '{name}' updated."
    else:
        return Fore.RED + f"Contact '{name}' not found."

# Функція виведення номеру телефону для зазначеного контакту
def show_phone(args, contacts):
    if len(args) != 1:
        return Fore.RED + "Invalid input. Use format: phone [name]"
    
    name = args[0]
    if name in contacts:
        return Fore.GREEN + f"👨 {name} ☎️  {contacts[name]}"
    else:
        return Fore.RED + f"Contact '{name}' not found."

# Функція, що виводить всі збереженні контакти з номерами телефонів
def show_all(contacts):
    if contacts:
        return Fore.GREEN + "\n".join([f"👨 {name} ☎️  {phone}" for name, phone in contacts.items()])
    else:
        return Fore.RED + "No contacts available."


def main():
    contacts = {}  # Словник для зберігання контактів
    print(Fore.BLUE + "Welcome to the assistant bot!")

    while True:
        user_input = input(Fore.BLUE + "Enter a command: ").strip()
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print(Fore.BLUE + "Good bye!")
            break
        elif command == "hello":
            print(Fore.BLUE + "How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print(Fore.RED + "Invalid command.")


if __name__ == "__main__":
    main()
