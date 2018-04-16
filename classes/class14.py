import os
import re
"""
files = os.listdir() #достает список файлов, которые находятся на том же уровне, что и сам файл программы
print(files)
"""
""" #считаем количество файлов и папок
files = os.listdir('bbc')
print(files)
count_f = 0
count_d = 0
for element in files:
    element = element.lower()
    if element.endswith('.txt'):
        count_f += 1
    else:
        count_d += 1
print(count_f, count_d)
"""
"""
files = os.listdir('bbc')
print(files)
my_d = {}
for element in files:
    element = element.lower()
    parts = element.split('.')
    if ext in my_d:
        my_d[ext] += 1
    else:
        my_d[ext] = 0

print(my_d)

#считаем количество файлов в каждой папке в папке bbc
start_path = 'bbc'
files = os.listdir(start_path)
for fname in files:
    if '.' not in fname:
        print(fname)
         #формировать путь как строку не оч хорошо, потому что
            #не во всех операционках это сработает - прямой/обратный слэш и тд)
        inter_files = os.listdir(start_path + '/' + fname)
        int_files = os.path.join(start_path, fname)
        print(len(int_files), 'files')
#os.path.join
"""
            
#start_path = r"C:\Users\student\Desktop\bbc"
#start_path = r".\bbc"
start_path = 'bbc'
fnames = os.listdir(start_path)
for fname in fnames:
    path_to_file = os.path.exists(os.path.join(start_path, fname))
    if os.path.isfile(path_to_file):
        print(fname + 'is a file')
    elif os.path.isdir(path_to_file):
        print(fname + 'is a folder')
    else:
        print('I have no idea...')
"""
#проверяем, существует ли какой-то файл/папка в какой-то папке
#так можно избежать ситуации, когда мы пытаемся открыть какой-то файл, а его нет
if os.path.exists(os.path.join(start_path, 'README.TXT')):
    with open('.\\bbc\\README.TXT', encoding="utf-8") as f:
        text = f.read()
        print(text)
else:
    print('fuck')
"""
#os.path.split - штука, обратная os.path.join
#change.dir
#listdir - это обычные строки, их можно сплитовать и делать что-то регулярками
#os.mkdir(путь или название папки)
#переименовать папки: создадим где-то папку bbc_rename; создаем в ней 5 подпапок с такими же названеям
#находим имена всех папок в ббс, идем по ним циклам, создаем в ббс_ренэйм создаем файл такой же
#открываем исходный файл для чтения и копируем в другой файл содержимое через write


