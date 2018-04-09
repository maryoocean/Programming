# Вариант 2

import re

#Задание 1
def open_file():
    with open('iceland.xml', encoding="utf-8") as f:
        text = f.read()
    return text

def count_lines(text):
    lines = text.split('\n')
    with open('lines.txt', "w", encoding="utf-8") as f:
        f.write(str(len(lines)))

#count_lines(open_file())

#Задание 2
        
def morph(text):
    res = re.findall('<w lemma=".*?" type="(.*?)">', text)
    return res

def making_d(res):
    my_dict = {}
    for element in res:
        if element in my_dict:
            my_dict[element] += 1
        else:
            my_dict[element] = 1
    return my_dict

def morph_keys(my_dict):
    m_keys = my_dict.keys()
    with open('morph_keys.txt', "w", encoding="utf-8") as f:
        for key in m_keys:
            f.write(key+'\n')

#morph_keys(making_d((morph(open_file()))))

#Задание 3.1   
def adj_pl(text):
    res = re.findall('<w lemma=".*?" type="(l.f.{3})">', text)
    adj_dict = making_d(res)
    return adj_dict

def adj_txt(adj_dict):
    adj_keys = adj_dict.keys()
    with open('adjectives_pl.txt', "w", encoding="utf-8") as f:
        for key in adj_keys:
            f.write(key + ' ' + str(adj_dict[key]) +'\n')

#adj_txt(adj_pl(open_file()))
            
#Задание 3.2
def csv_corpus_body(text):
    lines_clear = []
    body = re.findall(r'<body>(.*)</body>', text, flags=re.S)
    body_lines = body[0].split('\n')
    for line in body_lines:
        line_cl = re.sub('</?div1>','',line)
        line_cl2 = re.sub(r'</?[wcsp]>?','',line_cl)
        lines_clear.append(line_cl2)
    return lines_clear

def csv_corpus(lines_clear):
    with open('corpus.csv', "w", encoding="utf-8") as f:
        for line in lines_clear:
            match = re.search('lemma="(.*?)" type="(.*?)">(.*)', line)
            if match:
                f.write(match.group(1)+','+match.group(2)+','+match.group(3)+'\n')

#csv_corpus(csv_corpus_body(open_file()))

def main():
    #Задание 1
    get_file = open_file()
    counting_lines = count_lines(get_file)
    #Задание 2
    morphology = morph(get_file)
    make_d = making_d(morphology)
    morphology_keys = morph_keys(make_d)
    #Задание 3.1
    pl_adj = adj_pl(get_file)
    adj_file = adj_txt(pl_adj)
    #Задание 3.2
    csv_corp_text = csv_corpus_body(get_file)
    csv_corp = csv_corpus(csv_corp_text)

if __name__=='__main__':
    main()
