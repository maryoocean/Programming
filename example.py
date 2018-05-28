import re

def open_file():
    with open('corpus-xml-example.xml', encoding="utf-8") as f:
        text = f.read()
    return text

#Задание 2
def search_pos(text):
    res = re.findall('<w><ana lex=".*?" gr="(.[^,="]{0,4})', text)
    return res

def pos_dict(res):
    pos_d = {}
    for element in res:
        if element in pos_d:
            pos_d[element] += 1
        else:
            pos_d[element] = 1
    return pos_d

def pos_file(pos_d):
    pos_keys = pos_d.keys()
    with open('POS.txt', 'w', encoding="utf-8") as f:
        for key in pos_keys:
            f.write(key + '\t' + str(pos_d[key]) + '\n')

pos_file(pos_dict(search_pos(open_file())))

#Задание 3
def search_ins(text):
    res_ins = re.findall('<w><ana lex=".*?" gr="S.*?ins"></ana>(.*)</w>', text)
    print(type(res_ins))
    return res_ins

def words(text, res_ins):
    res_words = re.findall('<w><ana lex=".*?" gr=".*?"></ana>(.*?)</w>', text)
    for word in res_ins:
        i = res_words.index(word)
        with open('ins.txt', 'a', encoding="utf-8") as f:
            f.write(res_words[i-3]+ ' ' + res_words[i-2]+ ' ' +res_words[i-1] + '\t' + word + '\t' + res_words[i+1] + ' ' + res_words[i+2] + ' ' + res_words[i+3] + '\n')
           

search_ins(open_file())
words(open_file(), search_ins(open_file()))
    

