"""В.6. Загадывает слово, выдает подсказку, у пользователя 3 попытки, печатает, сколько попыток осталось"""
import random


def open_file(filename):
    vocabulary = []
    with open(filename, encoding="utf-8") as f:
        vocabulary = f.read().strip('\n').split('\n')
    return vocabulary


def words(vocabulary):
    """делим файл на 2 разных списка: на слова и подсказки к ним"""
    line_words = []
    words = []
    hints = []
    for line in vocabulary:
        line_words = line.split(',', maxsplit=1)
        i = 0
        for word in line_words:
            if i == 0:
                words.append(word)
                i += 1
            else:
                hints.append(word)
    return words, hints


def the_dict(words, hints):
    words_dict = {}
    i = -1
    for word in words:
        i +=1 
        #word = str(word) #у меня снова временами вылезает непонятная ошибка, мол, слово не того типа
        words_dict.setdefault(word, hints[i].split(','))
    return words_dict


def puzzle(words_dict):
    i = 0
    tips_printed = []
    tip = ''
    for key in words_dict:
        tips = words_dict[key]
        tip = random.choice(tips)
        tips_printed.append(tip)
        print(tip)
        answer = input('Отгадка - ').lower()
        while 1:
            i += 1
            if answer == key:
                print('Правильно!')
                i = 0
                break
            else:
                attempts = 3 - i
                if attempts != 0:
                    while 1:
                        tip = random.choice(tips)
                        if tip in tips_printed:
                            continue
                        else:
                            tips_printed.append(tip)
                            print('Неправильно! Осталось попыток: ', attempts, '. Еще одна подсказка:', tip)
                            answer = input('Отгадка - ').lower()
                            break
                else:
                    i = 0
                    print('Попыток не осталось. Ответ: ', key)
                    break
            
                
def main():
    my_voc = open_file('words.csv')
    my_words, my_hints = words(my_voc)
    my_dict = the_dict(my_words, my_hints)
    my_puzzle = puzzle(my_dict)


if __name__=='__main__':
    main()
