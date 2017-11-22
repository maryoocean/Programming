#Вариант 6. Адрес в fname - тот, который нам нужен. Кодировка файла - UTF-8 без BOM.
#А еще не знаю, считаем ли мы числа, написанные цифрами, словами. Если не считаем, то в strip нужно добавить цифры 0-9.
fname = "C:\\Users\\pavlo\\Desktop\\text.txt"
with open(fname, encoding="utf-8") as f:
    text = f.read()
#print(text)
words = text.split()
words_el = []
for word in words:
    word = word.strip('.,:;!?—«»-\"@')
    if word != '' and word != ' ':
        #print(word)
        words_el.append(word)
words_upper = 0
for word in words_el:
    if word[0].isupper():
        words_upper += 1
percent_upper = (words_upper/len(words_el))*100
print('Количество слов в тексте: ',len(words_el))
print('Количество слов, начинающихся с большой буквы: ',words_upper)
print('Какой процент эти слова составляют: ',percent_upper)
