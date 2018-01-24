import random

sentences = [] # собираю предложения, чтобы потом печатать их в произвольном порядке

def open_file(filename):
    my_list = []
    with open(filename, encoding="utf-8") as f:
        file = f.read().split()
        for element in file:
            my_list.append(element)
    return my_list


def noun():
    #открываем файл с существительными
    nouns = open_file('nouns_articles.txt')
    nouns.append('') # в итальянском языке личные местоимения опускаются
    our_noun = random.choice(nouns)
    #выбираем случайное существительное
    return our_noun


def noun_article(our_noun): 
    #ставим правильный артикль
    if our_noun.endswith('a'):
        np = 'la' + ' ' + our_noun
    elif our_noun.endswith('o'):
        np = 'il' + ' ' + our_noun
    elif our_noun.endswith('i'):
        np = 'i' + ' ' + our_noun
    elif our_noun.endswith('e'):
        np = 'le' + ' ' + our_noun
    else:
        np = ''
    return np


def verb(np):
    # выбираем глагол-связку
    verbs = open_file ('verb_essere.txt')
    if np.endswith('a') or np.endswith('o'):
        vp = np + ' ' + 'è'
    elif np.endswith('i') or np.endswith('e'):
        vp = np + ' ' + 'sono'
    else:
        vp = random.choice(verbs)
    return vp


def predicates(vp):
    #для законченного предложения осталось выбрать только предикат
    predicates = open_file('predicate.txt')
    flex_all = open_file('flex.txt.')
    flex_sg = open_file('flex_sg.txt')
    flex_pl = open_file('flex_pl.txt')
    #собственно, выбираем предикат в зависимости от выбранного выше существительного-подлежащего
    if vp.endswith('ono'): 
        if vp == 'sono': #Я.../Они...
            our_pred = random.choice(predicates) + random.choice(flex_all)
        elif vp.endswith('e sono'): #Они (ж.р.)...
            our_pred = random.choice(predicates) + 'e'
        else: #Они (м.р.)...
            our_pred = random.choice(predicates) + 'i'
    elif vp.endswith('è'): 
        if vp == 'è': #Он/Она...
            our_pred = random.choice(predicates) + random.choice(flex_sg)
        elif vp.endswith('a è'): #Она...
            our_pred = random.choice(predicates) + 'a'
        else: #Он...
            our_pred = random.choice(predicates) + 'o'
    elif vp.endswith('iamo') or vp.endswith('te'): #Мы/Они...
        our_pred = random.choice(predicates) + random.choice(flex_pl)
    else: #Ты...
        our_pred = random.choice(predicates) + random.choice(flex_sg)
    return our_pred

def aff_help():
    """для построения всех остальных предложений буду использовать утвердительное из этой функции"""
    my_np = noun_article(noun())
    my_vp = verb(my_np)
    my_pred = predicates(my_vp)
    the_affirmative = my_vp.capitalize() + ' ' + my_pred + '.'
    return the_affirmative 


def affirmative(the_affirmative):
    """эта функция непосредственно для утвердительного предложения,
    которое добавится в список только 1 раз"""
    sentences.append(the_affirmative)
    return sentences


def interrogative(the_affirmative): # Задается интонацией, поэтому меняем точку на знак вопроса
    the_interrogative = the_affirmative.replace('.','?')
    sentences.append(the_interrogative)
    return the_interrogative


def negation(the_affirmative): # Отрицание - это "non" перед глаголом.
    #the_affirmative = str(the_affirmative)
    """ питон в какой-то момент (когда я запускала код раз в 25-ый) ругался, что the_affirmative - это
    лист, я даже через type проверила это - тоже писал, что лист. перезапустила питон и ошибка исчезла,
    но строчку выше оставлю на всякий случай. причины ошибки, честно, не вижу"""
    words = the_affirmative.lower().split() # Разбиваем его на слова
    neg_sentence = []
    for word in words: # Ищем глагол в предложении
        if word == 'sono' or word == 'è' or word == 'sei' or word == 'siamo' or word == 'siete':
            my_negation = 'non ' + word # добавляем "non" перед ним
            neg_sentence.append(my_negation)
        else:
            neg_sentence.append(word)
    return neg_sentence


def negative(neg_sentence):
    the_negative = ''
    for element in neg_sentence:
        the_negative = the_negative + element + ' ' # снова собираем предложение (уже отрицательное)
    sentences.append(the_negative[:-1].capitalize()) # убираем лишний пробел после точки
    return the_negative[:-1]


def sent(the_negative, the_affirmative): # условное предложение соберем из двух простых (например, отрицательного и утвердительного)
    sent_cond = []
    sent_cond.append(the_negative) # генерируем новое отрицательное предложение
    del sentences[-1] # удаляем последнее предложение, чтобы в списке не было двух отрицательных
    sent_cond.append(the_affirmative) #новое утвердительное
    return sent_cond

def conditional(sent_cond):
    the_conditional = 'Se ' + sent_cond[0].replace('.',', ').lower() + \
                      sent_cond[1].lower() # чтобы предложения не совпадали (а при random.choice такое возможно),
    sentences.append(the_conditional) # я беру их через индексы
    return the_conditional


def imperative(np):
    imp_forms = open_file('imperative_forms.txt')
    """пока представляю, как использовать императив только с опущенными подлежащими-местоимениями,
    поэтому код такой.
    конструкция типа "сделай/приготовь/etc что-то" """
    i = 0
    while i < 1:
        if np != '':
            the_imperative = random.choice(imp_forms).capitalize() + ' ' + np + '!'
            i += 1
            sentences.append(the_imperative)
        else:
            continue
    return the_imperative


def our_sentences():
    affirmative(aff_help())
    interrogative(aff_help())
    negative(negation(aff_help()))
    conditional(sent(negative(negation(aff_help())), aff_help()))
    imperative(noun_article(noun()))
    return sentences


def random_sentences(sentences):
    i = 0
    printed_sentences = []
    while i < 5:
        the_sentence = random.choice(sentences)
        if the_sentence in printed_sentences:
            continue
        else:
            i += 1
            print(the_sentence, end=" ")
            printed_sentences.append(the_sentence)

            
random_sentences(our_sentences())

