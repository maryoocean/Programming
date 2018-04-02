import re
"""
#замена подстрок: .replace('.', '_')
text = 'Привет. Пока.'
#print(text.replace('.', '_'))

emails = 'blabla@mail.ru hi there i am almost done pavlova@gmail.com '
result = re.sub('[\w.-]+@[\w.-]+\.?\s','<email> ',emails)
#print(result)

emails = 'blabla@mail.ru hi there i am almost done pavlova@gmail.com livingthing@hotmail.com по-русски'
result = re.sub('@[\w.-]+\.?\s', '@hse.ru ', emails)
#print(result)

#sub используется для чистки текстов
result = re.sub('\W','',emails) #заменяет все не цифры, не буквы и не _ на ничего
#print(result)

#re.split('все, что хотим считать за разделитель','строка, которую делим')
#print(re.split('\W',emails)) #но так он делит email на несколько токенов

#result = re.split('[^-\'\w@]', emails)
#print(result)

#result = re.findall('\w+[-\']?.*\s', 'Бр, друг... по-русски!!!')
#print(result)

#\b - граница между буквенными небуквенным символом

#для поиска чего-нибудь с бэкслэшэм - префикс

"""
"""
while 1:
    email = input('Введите свой email: ')
    res = re.match('[\w.-]+@[a-zA-Z]+\.+[a-zA-Z]+', email)
    if res != None:
        print('Спасибо!')
        break
    else:
        print('Введите еще раз')
print(res)

#проверка номера телефона

number = input('Введите свой номер телефона: ')
res = re.match('(\+7)|(8)(\d{10})', number)
if res != None:
    print('Спасибо!')
else:
    print('Введите еще раз')
print(res.group())
"""

#проверить начинается ли слово с гласной

word = input('Введите слово: ')
res = re.match('([аеёиоуыэюяАЕЁИОУЫЭЮЯ])(\w+)', word)
if res != None:
    print('Спасибо!')
else:
    print('Введите еще раз')
print(res.group())

#флаги в документации с флагом . будет включать все символы, включая перенос строки
#во флагах есть и ignore case
#как вытащить первое слово (до \b, чтобы не захватывать пробел)
