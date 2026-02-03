def take_and_check_input():
    user_input = input('Введите целое положительное число:\n')
    if user_input.isdigit() and int(user_input) > 0:
        return int(user_input)
    else:
        print('Некорректный ввод')

def countdown(counter):
    if counter:
        while counter + 1:
            print(counter)
            counter -= 1
        else:
            print('Программа завершена')

if __name__ == '__main__':
    countdown(take_and_check_input())