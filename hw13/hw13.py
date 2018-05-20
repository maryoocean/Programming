# Вариант 6:
# в скольких папках встречается несколько файлов с одним и тем же расширением
import os

def roots():
    my_roots = []
    start_path = '.'
    for root, dirs, files in os.walk(start_path):
        my_roots.append(root)
    return my_roots

def dirs(my_roots):
    i = 0
    for root in my_roots:
        get_files = os.listdir(root)
        ext_d = {}
        for file in get_files:
            my_fname, my_ext = os.path.splitext(os.path.join(root, file))
            if my_ext != '':
                if my_ext in ext_d:
                    ext_d[my_ext] += 1
                else:
                    ext_d[my_ext] = 1
        my_values = ext_d.values()
        for value in my_values:
            if value > 1:
                i += 1
                break
    print('Количество папок, в которых встречается несколько файлов с одним и тем же расширением:',i)
    
def main():
    the_roots = roots()
    the_dirs = dirs(the_roots)

if __name__=='__main__':
    main()

