alphabet = 'abcdefghijklmnopqrstvxyz'
vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxz'
while 1:
    word = input('Введите слово на латинице: ').lower()
    i = 0
    while i < len(word):
        for letter in word:
            if letter in alphabet:
                i += 1
            else:
                print('Это не латиница :(')
                word = input('Введите слово на латинице: ').lower()
                break
    if word[0] in vowels:    
        piglatin_word = word + 'way'
        print(piglatin_word)
    elif word[0] in consonants and word[1] in consonants:
        piglatin_word = word[2:] + word[0:2] + 'ay'
        print(piglatin_word)
    else:
        piglatin_word = word[1:] + word[0] + 'ay'
        print(piglatin_word)
