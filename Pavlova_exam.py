"""Для работы скачайте файл news.zip, содержащий новостные статьи с разметкой в формате НКРЯ. Обратите внимание на кодировку файлов.
  
1 (5 баллов). Создайте csv-таблицу с полями "doc_id", "title", "author", "created", "topic", "tagging" с информацией о всех статьях (см. тег meta).
  
2 (8 баллов). Во всех файлах найдите все аббревиатуры (их леммы должны быть написаны заглавными буквами) и подсчитайте,
сколько раз каждая из них встретилась во всей текстовой коллекции. Результаты запишите в таблицу со столбцами: аббревиатура, количество вхождений.
В качестве разделителя надо использовать табуляцию. 
  
3 (10 баллов). Найдите в текстах все биграммы вида "сущ. + существительное в родит. падеже (gen)".
В новый текстовый файл запишите найденные биграммы; на каждой строке нужно записать биграмму и предложение, в котором она встретилась,
разделив их табуляцией. Повторяющиеся биграммы убирать не надо."""

import re
import os
#Задание 1:
def get_files(path):
    files = [files for root, dirs, files in os.walk(path)]
    return files

def search_info(files, path):
    with open('task1_info.csv', 'w', encoding='utf-8') as f:
        f.write('doc_id' + '\t' + 'title' + '\t' + 'author' + '\t' + 'created' + '\t' + 'topic' + '\t' +'tagging' + '\n')
        for file in files[0]:
            with open(os.path.join(path, file), encoding='cp1251') as f_news:
                for el in f_news:
                    print(el)
                    match_id = re.search(r'<meta content="(.*?)" name="docid">', el)
                    if match_id:
                        docid = match_id.group(1)
                        print(docid)
                        f.write(docid + '\t')

                    match_title = re.search('r<title>(.*?)</title>', el)
                    if match_title:
                        title = match_title.group(1)
                        f.write(title + '\t')

                    match_author = re.search('r<meta content="(.*?)" name="author">', el)
                    if match_author:
                        author = match_author.group(1)
                        f.write(author + '\t')

                    match_created = re.search('r<meta content="(.*?)" name="created">', el)
                    if match_created:
                        created = match_created.group(1)
                        f.write(created + '\t')

                    match_topic = re.search('r<meta content="(.*?)" name="topic">', el)
                    if match_topic:
                        topic = match_topic.group(1)
                        f.write(topic+ '\t')

                    match_tagging = re.search('r<meta content="(.*?)" name="tagging">', el)
                    if match_tagging:
                        tagging = matc_tagging.group(1)
                        f.write(tagging + '\n')
                #f.write(docid + '\t' + title + '\t' + author + '\t' + created + '\t' + topic + '\t' + tagging + '\n')
 
get_files('news')
       
search_info(get_files('news'),'news')

#Задание 2
def abbrev(path):
    abb_dict = {}
    files = [files for root, dirs, files in os.walk(path)]
    with open('task2_abb.csv', 'w', encoding='utf-8') as f:
        for file in files[0]:
            with open(os.path.join(path, file), encoding='cp1251') as f_news:
                for element in f_news:
                    match = re.search(r'lex="(.*?)"', element)
                    if match:
                        abbr = match.group(1)
                        if abbr.isupper():
                            abb_dict[abbr] += 1
        for key in abb_dict:
            f.write(key.encode('utf-8') + '\t' + str(abb_dict[key]))
            
abbrev('news')
