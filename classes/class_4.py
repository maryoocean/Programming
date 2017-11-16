"""
16.11.2017
>>> sent = 'Какая хорошая погода'
>>> sent.split()
['Какая', 'хорошая', 'погода']
>>> sent = 'Какая хорошая погода. Доброе утро.'
>>> sent.split()
['Какая', 'хорошая', 'погода.', 'Доброе', 'утро.']
>>> sent.split('.')
['Какая хорошая погода', ' Доброе утро', '']
>>> sent = 'Какая хорошая погода. Доброе утро.   .'
>>> sent.split('. ')
['Какая хорошая погода', 'Доброе утро', '  .']
>>> 
"""
#frame = r'C:\Users\student\Desktop\texts.txt'
#print(frame)
#r - "raw" - понимай бэкслэш просто как символ
"""
fname = "C:\\Users\\student\\Desktop\\texts.txt"
print(fname)
with open(fname) as f:
    text = f.read() #файл открыт, пока мы внутри with open
print(type(text))

text = ""
f = open(fname)
text = f.read()
lines = text.split('\n')
print(text[:100])
print(lines[:5])
f.close() #файл открыт, пока мы не закроем его этим оператором

#encoding = 'кодировка' - указываем кодировку
"""
"""
fname = "C:\\Users\\student\\Desktop\\texts.txt"
print(fname)
with open(fname) as f:
    text = f.read() #файл открыт, пока мы внутри with open
print(type(text))

text = ""
f = open(fname)
text = f.read()
lines = text.split('\n')
text_elements = [] #задаем список 
for line in lines:
    words = line.split() #если указать пробел как разделитель, то каждый пробел будет считаться разделителем и тогда появятся пустые строки
    text_elements.append(words) #добавляем слова в список, где одно слово - один элемент списка
    #for word in words:
        #print(word)
    print()
print(text_elements[:2]) #печатаем до второй строчки, не включая ее
print(len(text_elements)) #печатаем количество строчек списка (= кол-ву строк в файле)
f.close()

words = 'мама папа я  счастливая семья'
print(words.split(' '))

>>> "hello".strip()
'hello'
>>> "hello\n".strip()
'hello'
>>> "	 hello\n	".strip()
'hello'
>>> 
"""
fname = "C:\\Users\\student\\Desktop\\texts.txt"
print(fname)
with open(fname) as f:
    lines = f.readlines() #читаем построчно, элемент - строка. остаются разделители строк!!!
print(lines)
print(len(lines))
"""
>>> "hello".isupper()
False
>>> "HELLO".isupper()
True
>>> "hELLo".isupper()
False
>>> "hello".islower()
True
>>> 
"""


