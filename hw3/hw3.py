"""
Вариант 6.
Я тут попыталась проверить, слово ли вводит пользователь.
"""

print ('Начало программы')
print('')
word = input('Введите слово: ')
print('')
if word.isdigit():
    print('Ошибка: введите слово, а не число')
elif word == '':
    print('Ошибка: пустая строка')
else:
    try:
        float(word)
        print('Ошибка: введите слово, а не число')
    except ValueError:
        print(word)
        while len(word) > 1:
            word = word[1:]
            print(word)
print('')
print('Конец программы')
