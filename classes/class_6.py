#def hello(user1, user2, user3):
    #print('Hello, ' + user1 +'!')
    #print(user2.title())
    #print(user3.title())

"""
def hello(user1, age):
    print('hello, ' + user1 + '!')
    if age > 10:
        print('>10')
    else:
        print(age)


hello('name', 15)


def hello(user1, age):
    print('hello, ' + user1 + '!')
    if age > 10:
        print('>10')
    else:
        print(age)
    sum_ = 0
    for i in range(16):
        sum_ += 1
    print(sum_)
    print(gl)

gl = 100

hello('name', 15)
print(sum_)

def hello(user1, age):
    print('hello, ' + user1 + '!')
    if age > 10:
        print('>10')
    else:
        print(age)
    new_name = user1.title()
    return new_name

user_title = hello('name', 10)
print(user_title)

hello('name', 15)


def hello(user1):
    
    print('hello, ' + user1 + '!')
    return user1.title() #задаем, какой аргумент и как возвращает функция

user_title = hello('name')
print (user_title)
"""

#по букве на строчке, а потом количество символов

#def elemenets(word):
#    """ """
#    for i in word:
#        print(i)
#    print(len(word))


#sent = 'мне холодно'
#els = sent.split()
"""
def tokenize(sentence): #примитивная токенизация
    words = sentence.split()
    return words

sent = 'functions are useful'

tok_results = tokenize(sent)
print(tok_results)

for w in tok_results:
    print(w.upper())
"""

#берет на вход имя файла, открывает и читает его по строкам, возвращает список строк

def lines_div_length(fname): #задаем функцию, кот берет на вход имя файла
    with open(fname, encoding = "utf-8") as f: #открывает его и читает пострчоно
        lines_raw = f.readlines()
    lines_lengths = [] #задаем список, в который будем складывать длины строк
    for line in lines_raw: # каждую строчку очищаем
        clear_line = line.strip()
        if clear_line: #считаем длину очищенной строки
            lines_lengths.append(len(clear_line)) #считаем длины строк

    return min(lines_lengths) #функция возвращает минимальное значение списка 

min_1 = lines_div_length('text.txt')
print(min_1)
