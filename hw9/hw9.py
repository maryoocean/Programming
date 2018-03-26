# Вариант 6. Глагол "загрузить".

import re
forms = {}

def filename_enter():
    while 1:
        filename = input('Введите название файла (через относительный путь): ')
        if filename != '' and filename.lower().endswith('.txt'):
            break
        else:
            continue
    return filename


def open_file(filename):
    words = []
    words_clear = []
    with open(filename, encoding="utf-8") as f:
        words = f.read().lower().split()
    return words


def clear_words(words):
    words_clear = []
    for word in words:
        word_clear = re.sub('[\W\d_]', '', word)
        words_clear.append(word_clear)
    return words_clear


def clear_text(words_clear):
    with open('words_clear.txt', "w", encoding="utf-8") as f:
        for word in words_clear:
            f.write(word + ' ')
    with open('words_clear.txt', encoding="utf-8")as f:
        text_clear = f.read()
    return text_clear


def making_dict(cur_forms, forms):
    for word in cur_forms:
        if word in forms:
            forms[word] += 1
        else:
            forms[word] = 1
    return forms


def searching(text_clear):

    " поиск инфинитивов "

    inf = re.findall('загрузитьс?я?\s', text_clear)
    making_dict(inf, forms)

    " поиск кратких причастий и страдательных причастий прошедшего времени "

    part_forms = re.findall('загруженн?[ыаоу]?[йяехгмю]?[оу]?\s', text_clear)
    making_dict(part_forms, forms)

    " поиск форм будущего времени, прошедшего времени, императива, действительных причастий прошедшего времени, деепричастий "

    part2_forms = re.findall('загру[зж][уия]л?[аои]?[вмт]?ш?[ьиае]?[йяе]?с?[ья]?\s', text_clear) 
    making_dict(part2_forms, forms)
    return forms


def results(forms):
    i = 1
    res = forms.keys()
    if len(res) != 0:
        print('\nНайденные формы глагола "загрузить":\n')
        for key in res:
            print(i, key)
            i += 1
    else:
        print('\nФормы глагола "загрузить" не найдены.')


def main():
    name = filename_enter()
    open_f = open_file(name)
    cleanse_w = clear_words(open_f)
    cleanse_t = clear_text(cleanse_w)
    search = searching(cleanse_t)
    result = results(search)


if __name__=='__main__':
    main()
