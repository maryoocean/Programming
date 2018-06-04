#Вариант 6
import re
import sys

def open_text(filename):
    try:
        with open(filename, encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError as error:
        print('Файла {} не существует'.format(filename))
        sys.exit()
    except UnicodeDecodeError as error:
        print('Не могу прочитать файл {}'.format(filename))
        sys.exit()
    text_split = re.split('[.?!]', text)
    sentences = [sent for sent in text_split]
    return sentences

def clear_punct(sentences):
    sentences_cl = []
    for sent in sentences:
        sent_cl = re.sub('[\\n.!?,:;"-]','', sent)
        sentences_cl.append(sent_cl)
    return sentences_cl

def count_words(sentences_cl):
    for sent in sentences_cl:
        words = sent.split()
        i = len(words)
        if i != 0 and i > 10:
            sent_letters = re.sub(' ','',sent)
            k = len(sent_letters)/len(words)
            print('Это предложение со словами длины {:.1f}'.format(k))

def main():
    my_text = open_text('chekhov.txt')
    text_clear = clear_punct(my_text)
    print('Средняя длина слов в предложениях, длиной более чем в 10 слов')
    count_length = count_words(text_clear)
    
if __name__=='__main__':
    main()
