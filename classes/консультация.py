year_2016 = []
with open ('C:\\Users\\pavlo\\Desktop\\cons.csv', encoding="utf-8") as f:
    lines = f.readlines()
for line in lines:
    #print(line)
    cells = line.split(',')
    if cells[2] == '2016':
        years_2016 = year_2016.append(cells)
        print(cells)
country = input('Введите, пожалуйста, страну: ')
countries = []
"""
for country in year_2016:
    countries = countries.append(country[0])
    print(countries)
"""
i = 0
for element in year_2016:
    if country == element[0]:
        element[3] = str(element[3]).strip('\n')
        element[3] = str(element[3])
        element [3] = float(element[3]) #(sdsfg.strip())
        print(element[3])
        i += 1
        break
if i == 0:
    print('Такой страны нет')
#или через true/false
#есть таблица, собрали данные за 2016, собрать топ-10 самых счастливых и самых несчасливых стран.
sorted_list = []
to_sort = []
print(type(sorted_list))
for k in year_2016:
    k[3] = str(k[3]).strip()
    k[3] = float(k[3])
    to_sort = k[3], k[0]
    print(to_sort)
    sorted_list = sorted_list.append(to_sort)
"""       
    #cells[3] через стрип и флоат переводим в число + cells[0]
    #p = []
"""
