from pathlib import Path
from colorama import Fore, init
import sys

init(autoreset=True)

def print_directory_structure(path, indent_level=0):
    if indent_level == 0:
        # Виводимо назву головної папки синім кольором
        print(f"{Fore.BLUE}📦 {path.name}/")

    for item in path.iterdir():
        if item.is_dir():
            # Виводимо назву папки синім кольором
            print(f"{' ' * indent_level}  {Fore.BLUE}📂 {item.name}/")
            # Рекурсивно виводимо вміст піддиректорії
            print_directory_structure(item, indent_level + 2)
        else:
            # Виводимо назву файлу зеленим кольором
            print(f"{' ' * indent_level}  {Fore.GREEN}📜 {item.name}")

def main():
    # Отримуємо шлях до директорії з аргументу командного рядка
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Вкажіть шлях до директорії як аргумент!")
        return

    directory = Path(sys.argv[1])

    # Перевіряємо, чи існує директорія
    if not directory.exists() or not directory.is_dir():
        print(f"{Fore.RED}Вказаний шлях не існує або це не директорія!")
        return

    # Виводимо структуру директорії
    print_directory_structure(directory)

if __name__ == "__main__":
    main()
