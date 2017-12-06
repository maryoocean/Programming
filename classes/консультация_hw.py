
year_2016 = []
with open ('C:\\Users\\pavlo\\Desktop\\cons.csv', encoding="utf-8") as f:
    lines = f.readlines()
for line in lines:
    #print(line)
    cells = line.split(',')
    if cells[2] == '2016':
        year_2016.append(cells)
        #print(cells)
country = input('Введите, пожалуйста страну: ')
found_answer = False
for element in year_2016:
    if country == element[0]:
        element[3] = float(element[3].strip())
        print(element[3])
        found_answer = True
        break
if not found_answer:
    print('Данных об этой стране нет')
my_list = []
to_sort = []
sorted_list_hap = []
sorted_list_unhap = []
for line in year_2016:
    line[3] = float(line[3].strip('\n'))
    to_sort = line[3], line[0]
    my_list.append(to_sort)
sorted_list_hap = sorted(my_list, reverse=True)
sorted_list_unhap = sorted(my_list, reverse=False)
print("Топ-10 самых счастливых стран: ",sorted_list_hap[0:10])
print("Топ-10 самых несчастливых стран: ",sorted_list_unhap[0:10])
