#Вариант 6
print('Начало программы. Вариант 6'+'\n')
i = 0 #счетчик для ввода
words = []
with open("hw5_pavlova.txt", "w", encoding="utf-8") as f:
    while i < 7:
        try:
            word = int(input('Введите, пожалуйста, число: '))
            i += 1
            words.append(word)
        except ValueError:
            print('Это не число, введите, пожалуйста, число: ')
    for k in range(len(words)):
        if k < (len(words) - 1):
            my_line = str('x'*(int(words[k]))+'\n')
            f.write(my_line)
        else:
            my_line = str('x'*(int(words[k])))
            f.write(my_line)
print('\n'+'Вот, что у нас теперь в файле:')
print(open("hw5_pavlova.txt").read())

