#Вариант 6

num = int(input('Пожалуйста, введите число: '))
print('Таблица умножения для числа',num)
k = 0
while k <= 9:
    k += 1
    num_1 = k*num
    print(k,'*', num,'=', num_1)
print('The end')
