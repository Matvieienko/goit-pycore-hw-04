# В разі потреби створюємо cats_file.txt в який записуємо дані для перевірки роботи функції 
# with open("cats_file.txt", "w", encoding='utf-8') as file:
#     file.write("""60b90c1c13067a15887e1ae1,Tayson,3
# 60b90c2413067a15887e1ae2,Vika,1
# 60b90c2e13067a15887e1ae3,Barsik,2
# 60b90c3b13067a15887e1ae4,Simon,12
# 60b90c4613067a15887e1ae5,Tessi,5""")
    

def get_cats_info(path: str) -> list[dict[str, str | int]]:

    try:

        with open(path, "r", encoding='utf-8') as file:
            # Створюємо пустий список до якого будемо заносити дані про котів
            cats = []
            # Проходимо по кожному рядку файлу
            for line in file:
                # Розділяємо рядок на id, ім'я та вік методом split(',')
                id, name, age = line.strip().split(',')
                # Cтворюємо словник з даними котів ключ:значення
                cats_info = {
                    "id": id,
                    "name": name,
                    "age": int(age) # Може хтось захоче порахувати середній вік котів
                    }
                # Додаємо словник до списку
                cats.append(cats_info)
            # Повертаємо список словників з даними про котів
            return cats 
            
    except FileNotFoundError:
        raise FileNotFoundError(f"Файлу за шляхом {path} немає.")
    except Exception:
        raise Exception("Сталася помилка")

# Приклад використання функції     
cats_info = get_cats_info("Task_2/cats_file.txt")
print(cats_info)
# Або так :)
for cat in cats_info:
    print(cat)