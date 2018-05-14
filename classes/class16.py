#генерация списков (делали циклом через append)

list_again = [i for i in [1, 2, 3, 4]]
print(list_again)

text = [word.title() for word in 'на улице жара'.split()]
print(text)

#создать новый словарь, который монжо итерировать

#если просто IF
new = [i for i in range(1, 5) if i%2 == 0] #добавляем четные числа (1, 5)
print(new)

#если с ELSE, то:
new1 = [word if word.istitle() else '_'+word+'_' for word in 'Алиса & Сnрана чудес'.split()]
print(new1)

#брать на вход предложение, оставлять в списке только слова, длиннее 3х букв
new2 = [word for word in 'Сегодня на улице так тепло'.split() if len(word)>3]
print(new2)

#так же, но оставим слова, если в них есть хотя бы 3 гласных
import re
new3 = [word for word in 'Сегодня на улице так тепло'.split() if len(re.findall('[аоеёиуэюяАОЕЁИУЭЮЯ]', word))>= 3]
print(new3)

#перевернуть словарь
def reverse_dict(old_dict):
    new_dict = {old_dict[k]: k for k in old_dict}
    print(new_dict)

reverse_dict({i: i**2 for i in range(1,5)})
#написать словарь, в котором ключ - слово из предложения, а его значение - длина этого слова

#токенизация, словарь, itmes(можно перевернуть через [::-1])


"""ФОРМАТИРОВАНИЕ СТРОК"""
print('Длина слова "{}" равна {}'.format('чудес', len('чудес')))
#{} - место, куда надо что-т вставить

name = input('Как тебя зовут? ')
print('Привет, {}!'.format(name.title()))

print('Длина слова {1} равна "{0}"'.format('чудес', len('чудес')))
#в скобках можно расставлять индексы, чтобы менять местами то, что мы хотим вставить на их место

#выравнивание
print('{:_<12}'.format('ыло'))
#поставь столько _ слева, чтобы общая длина строки была 12
print('{:_>12}'.format('ыло'))
#поставь столько _ справа, чтобы общая длина строки была 12
print('{:_^12}'.format('ылоылоыло'))
#поставь столько _, чтобы общая длина строки была 12 и заданная мною строка была по центру

#форматирование дробей
print('{:08.3f}'.format(1.2))
#слева от точки указываем цифру, которая обозначает, сколько всего знаков должно быть, включая точку
#справа от точки указываем цифру, которая обозначает, сколько знаков мы хотим оставить после запятой

#посмотреть про даты!!!

#читаем текст из файла, убираем пунктуацию, токенизируем, удаляем слова короче 3х символов, считать частотник
import re

def get_file(fname):
    with open(fname, encoding="utf-8") as f:
        text = f.read()
    return text

def text_cl(text):
    text_clear = re.sub('[,.?!:;]"\'#()]','',text)
    return text_clear

def text_tok(text_clear):
    tokenized = text_clear.split()
    return tokenized

def word_len(tokenized):
    new_text = [word for word in tokenized if len(word) >= 3]
    print(new_text)

word_len(text_tok(text_cl(get_file('text.txt'))))

def get_data(fname):
    raw = ''
    with open(fname, encoding="utf-8") as f:
        raw = f.read()
    print(raw[:50])
    print(len(raw))
    return raw

def tokenize(raw):
    tokens = re.split('[^\w-]+',raw)
    results = [word for word in tokens if len(word) >= 3]
    bigrams = [tokens[i:i+1] for i in range(len(tokens))]
    print(bigrams) #объединить через join
    return results

tokenize(get_data('text.txt'))

                      
    





