alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
vowels = 'аеёиоуыэюя'
while 1:   
    word = input('Введите слово на кириллице: ').lower()
    i = 0
    the_word = ''
    while i < len(word):
        for letter in word:
            if letter in alphabet:
                i += 1
                #continue
            else:
                i = 0
                print('Это не кириллица :(')
                word = input('Введите слово на кириллице: ')
                break
    for letter in word:
        if letter in vowels:
            the_word = the_word + letter + 'с' + letter   
        else:
            the_word = the_word + letter
    print(the_word)

