# Вариант 6. Я считала количество вхождений

def filename_enter():
    while 1:
        filename = input('Введите название файла (через относительный путь): ')
        if filename != '' and filename.lower().endswith('.txt'):
            break
        else:
            continue
    return filename


def read_text(filename): # делим текст на слова
    words_split = []
    with open(filename, encoding="utf-8") as f:
        words_split = f.read().split()
    return words_split


def words_clear(words_split): #убираем "прилипшие" знаки препинания
    words = []
    for word in words_split:
        word = word.strip('.,:;!?—«»-\"@')
        words.append(word)
    return words


def search_omni(words): #ищем слова с приставкой omni, считаем их и добавляем в словарь
    omni = {}
    for word in words:
        if word.startswith('omni'):
            if word in omni:
                omni[word] += 1
            else:
                omni[word] = 1
    if len(omni) == 0:
        print('Таких слов нет')
    return omni


def wo_omni(omni): 
    wo_omni_words = []
    keys_omni = list(omni.keys()) # собираем в список слова с приставкой omni из словаря
    for word in keys_omni:
        wo_omni_words.append(word[4:]) # в список соибраем те же слова без  приставки
    return wo_omni_words


def search_wo_omni(wo_omni_words, words):
    wo_omni = {}
    for word in wo_omni_words: 
        if word in words: 
            n = words.count(word) # считаем, есть ли такие слова в тексте
            wo_omni[word] = n
        """если таки требуется выводить 0, то нужны закомменитрованные строчки"""
        #else: 
            #wo_omni[word] = 0
    if len(wo_omni) == 0:
        print('Таких слов тоже нет')
    return wo_omni

    
def main():
    my_filename = filename_enter()
    print('\nOMNI- words\n')
    my_words_split = read_text(my_filename)
    my_words = words_clear(my_words_split)
    stats_omni = search_omni(my_words)
    for element in sorted(stats_omni, key=stats_omni.get, reverse=True):
        print(element, ' - ', stats_omni[element])
    my_wo_omni_words = wo_omni(stats_omni)
    print('\nwithout OMNI- words\n')
    stats_wo_omni = search_wo_omni(my_wo_omni_words, my_words)
    for element in sorted(stats_wo_omni, key=stats_wo_omni.get, reverse=True):
        print(element, ' - ', stats_wo_omni[element])


if __name__=='__main__':
    main()

