# Вариант 6 (отряд)

import re

def filename_enter():
    while 1:
        filename = input('Введите название файла (через относительный путь): ')
        if filename != '' and filename.lower().endswith('.html'):
            break
        else:
            continue
    return filename


def open_file(filename):
    with open(filename, encoding="utf-8") as f:
        text = f.read()
    return text


def search(text):
    match = re.search('(Отряд:)[\W\d]*(<[^>]+>){3}([А-Яа-яЁё]+)', text)
    if match:
        res = match.group(1,3)
    else:
        print('Ничего не нашлось')
    return res


def add(res):
    with open('отряд.txt', "w", encoding="utf-8") as f:
        f.write(res[0] + ' ' + res[1])
        

def main():
    name = filename_enter()
    html = open_file(name)
    searching = search(html)
    adding = add(searching)


if __name__=='__main__':
    main()
