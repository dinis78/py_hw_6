import module_data

date = input('Введите дату в формате DD.MM.YYYY: ')
valid = module_data.val_data(date)
print(valid)