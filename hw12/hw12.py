#Вариант 6
import os

def fnames():
    files = os.listdir()
    fnames_list = []
    for file in files:
        if os.path.isfile(file):
            file = file.lower()
            file_n = file.split('.')
            i = len(file_n)
            n = 0
            fname = ''
            while n < i-1:
                n += 1
                fname += file_n[n-1] + '.'
            fnames_list.append(fname[0:-1])                
        elif os.path.isdir(file):
            file = file.lower()
            fnames_list.append(file)
        else:
            continue
    return fnames_list


def fnames_p(fnames_list):
    fnames_punct = {}
    punct = ',.!;\''
    for fname in fnames_list:
        for element in fname:
            if element in punct:
                fnames_punct[fname] = 1
                break
    return fnames_punct


def print_fnames(fnames_punct):
    fnames_keys = fnames_punct.keys()
    if len(fnames_keys) > 0:
        print('Файлы и папки со знаками препинания в названии:')
        for element in fnames_keys:
            print(element)
    else:
        print('Файлов и папок со знаками препинания в названии нет')

    
def main():
    my_fnames = fnames()
    punct_fnames = fnames_p(my_fnames)
    fnames_to_print = print_fnames(punct_fnames)


if __name__=='__main__':
    main()
