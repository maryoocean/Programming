"""
import re
s = 'abracadabra'
results = re.findall('точное вхождение',s)
results = re.findall('a.',s)
results = re.finall('ab?',s)
results = re.findall('ab+',s)
results = re.finall('(ab)+',s)
results = re.findall('[bmny]',s)
results = re.findall(' s[^ ]+ ', s)
[] - любой символ их тех, что находятся в скобках
внутри квадратных скобок все воспринимается буквально, кроме дефиса
() - если поместить внутри них какое-то выражение, то операто применится ко всему выражению
{} - от скольки раз и до скольки раз должен повторяться символ, стоящий перед скобками
. - любой символ, кроме переноса строки
? - последний символ перед ним может быть, а может и не быть
+ - последний символ перед ним должен встретиться один раз или больше
\d соответствует цифре
\D соответствует не цифре
\s соответствует пустому полю (пробел)
\S соответствует заполненному полю
\w соответствует алфавитно-цифровому значению
\W соответствует не алфавитно-цифровому значению
«»
"""
import re
"""
with open ('cosmos.txt', encoding="utf-8") as f:
    text = f.read()

results = re.findall('«[а-яА-ЯёЁ\d\w-]+»',text)
print(results)

#dates = re.findall('\d{1,2} [а-я]+ \d{4})', text)
#print(dates)

match = re.search('\d{1,2} [а-я]+ \d{4}', text)
if match:
    print(match)
else:
    print('oops')
print(match.group())

#Группы
"""

with open ('wiki.html', encoding="utf-8") as f:
    text  = f.read()
res = re.findall('<title>(.*?)</title>', text)
print(res)

with open ('wiki.html', encoding="utf-8") as f:
    text  = f.read()
links = re.findall('<a href=("https.+?")>', text) #только внешние ссылки
print(links)

with open ('wiki.html', encoding="utf-8") as f:
    text = f.read()
biblio = re.findall('<span class="reference-text">(.*?)<\', text)
print(biblio)
        
