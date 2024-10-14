# Створюємо salary_file.txt в який записуємо дані для перевірки роботи функції 
with open('salary_file.txt', 'w', encoding='utf-8') as file:
    file.write('Alex Korp,3000\nNikita Borisenko,2000\nSitarama Raju,1000')


def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            # Створюємо пустий список до якого будемо заносити дані про заплату
            salaries = []
            
            # Проходимо по кожному рядку файлу
            for line in file:
                # Розділяємо рядок на ім'я та зарплату методом split(',')
                name, salary = line.strip().split(',')
                # Додаємо зарплату до списку, конвертував у ціле число
                salaries.append(int(salary))
            
            # Обчислюємо загальну суму та середню зарплату
            total = sum(salaries)
            average = total / len(salaries)            
            return total, average
    
    # Обробляємо помилки
    except FileNotFoundError:
        raise FileNotFoundError(f'Файлу за шляхом {path} немає.')
    except Exception:
        raise Exception('Сталася помилка')
        
# Приклад використання функції 
total, average = total_salary('salary_file.txt')
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")