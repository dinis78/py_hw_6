# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину ели дата может существовать или ложь елси такая дата не возможна.
# Для простоты договоримся что год может быть в диапазоне [1, 9999]
# Весь период (1 янворя 1 года, 31 декобря 9999 года) действует григорианский календрь.
# Проверку года на высокостность вынести в отдельную защищённую функцию.

def leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
    
def val_data(data):
    day, month, year = map(int, data.split('.'))
    if year < 1 or year > 9999:
        return False
    if month < 1 > 12:
        return False
    days_in_month = [31, 28 if not leap_year(year) else 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if day < 1 or day > days_in_month[month-1]:
        return False
    return True




































