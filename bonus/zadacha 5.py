alphabet = 'abcdefghiklmnopqrstvxyz '
consonants = 'bcdfghjklmnpqrstvwxz'
while 1:
    word = input('Введите слово/фразу на латинице: ').lower()
    i = 0
    the_word = ''
    while i < len(word):
        for letter in word:
            if letter in alphabet:
                i += 1
            else:
                print('Это не латиница :(')
                word = input('Введите слово на латинице: ').lower()
                break
    for letter in word:
        if letter in consonants:
            the_word += letter + 'aig'
        else:
            the_word += letter
    print(the_word)


