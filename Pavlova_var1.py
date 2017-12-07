# Вариант 1.
with open('quotes.txt', encoding="utf-8") as f:
    text = f.read()
lines = text.split('\n')
words = []
for line in lines:
    word = line.split()
    words.append(word)
print(words)
for element in words:
    if len(element[0]) < 5:
        print(word)
#№2
for line in lines:
    if line.count('разум') > 0 or line.count('Разум') > 0:
        line = line.split()
        line.reverse()
        for i in line:
            if i != '—':
                print(i, end=' ')
            else:
                print('.')
                break
#№3
word = input('Введите слово: ')
words_input = []
while word != '':
    word = input('Введите слово: ')
    words_input.append(word)
for word in words_input:
    if words.count(word) > 0:
        print(word)

      
