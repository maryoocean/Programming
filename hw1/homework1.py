print ('Начало программы')
a = int (input ('Введите число a = '))
b = int (input ('Введите число b = '))
c = int (input ('Введите число c = '))
if a % b == c and a / b == c:
    print('a =', a, 'дает остаток c =', c, 'при делении на b =', b, 'и деление a =', a, ' на b =', b, ' дает значение с =', c)
elif a % b == c:
    print ('a =', a, 'дает остаток c =', c, 'при делении на b =', b, 'и деление a =', a, ' на b =', b, ' НЕ дает значение с =', c)
elif a / b == c:
    print ('Деление a =', a, ' на b =', b, ' дает значение с =', c, 'и a =', a, 'НЕ дает остаток c =', c, 'при делении на b =', b)
else: 
    print ('a =', a, 'НЕ дает остаток c =', c, 'при делении на b =', b, 'и деление a =', a, ' на b =', b, ' НЕ дает значение с =', c)
print ('Конец программы')
