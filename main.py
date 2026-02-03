user_input = input('Введите целое положительное число:\n')

if user_input.isdigit() and int(user_input) > 0:
    counter = int(user_input)
    while counter + 1:
        print(counter)
        counter -= 1
    else:
        print('Программа завершена')
else:
    print('Некорректный ввод')