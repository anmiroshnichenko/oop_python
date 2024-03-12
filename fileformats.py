# Формат csv
import csv  # библиотека для работы с csv

# Вариант 1 - Чтение файла построчно(любые файлы)
# with open('newsafr.csv') as f:
#     reader = csv.reader(f)
#     # print(type(reader))
#     count = 0    
#     for row in reader:
#         if count > 0: # избавимся от вывода первой строки "title"
#             # print(type(row), row)
#             print(row[-1])
#         count += 1
# print(f'В этом файле {count-1} новостей') #  '-1' исключили перую строку "title"

# Вариант 2 - обработка файла целиком (относительно небольшие файла <= 2gb)
# with open('newsafr.csv') as f:
#     reader = csv.reader(f)
#     print(type(reader))
#     new_list =  list(reader)
# header = new_list.pop(0)  #убираем первую строку
# print(header)
# for row in new_list:
#     print(row[-1])
# print(f'В этом файле {len(new_list)} новостей') 

# Вариант 3 - чтение через словари(обратка сложного файла с множеством полей)
# with open('newsafr.csv') as f:
#     reader = csv.DictReader(f) #работает только построчно
#     count = 0
#     for row in reader:
#         print(row['title'])
#         count += 1
# print(f'В этом файле {count} новостей')

# Записать в csv  файл
with open('newsafr.csv') as f:
    reader = csv.reader(f)
    print(type(reader))
    new_list =  list(reader)
header = new_list.pop(0)  #убираем первую строку
print(header)

csv.register_dialect("comma_no_quoting", delimiter=",", quoting=csv.QUOTE_NONE, escapechar='\\')
csv.register_dialect("semicolon_quoteal", delimiter=";", quoting=csv.QUOTE_ALL)
# w = write, a = append
with open('newsafr2.csv', 'w') as f:
    # writer = csv.writer(f)
    # writer = csv.writer(f, delimiter=";") # изменили разделитель  
    # writer = csv.writer(f, delimiter=";", quoting=csv.QUOTE_ALL) # изменили разделитель и добавили кавычки
    # writer = csv.writer(f, delimiter=",", quoting=csv.QUOTE_NONE, escapechar='\\')  # экранирование запятой "/,"
    writer = csv.writer(f, dialect="comma_no_quoting")  # используем диалект
    writer = csv.writer(f, dialect="semicolon_quoteal")
    writer.writerow(header)
    writer.writerows(new_list[:3]) 



# with open('newsafr.csv', newline='') as f: #newline=''  - убрать возможные пустые строки 
    # reader = csv.reader(f, delimiter=',') # указали раздилитель ','
    # reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE, quotechar='"', escapechar='\\') 
    # 1- читаем весь cvs в список 
    # news_list = list(reader) #файл не большой, сразу можем преобразовать  в список
    # 2 -читаем по строчно, если большой файл
    # for news in reader:
        # print(news)
    # 3 - читаем в словарь
    # reader = csv.DictReader(f, delimiter=',')
    # for news in reader:
        # print(news)
        # print(news['title'])    
# print(news_list[:2])

# Формат json
## import pprint #импорт модуля pprint
## pprint.pprint() #использование 
import json  # библиотека для работы с json
from pprint import pprint  #импортируем модуль 
with open('newsafr.json', 'r') as f: # открокрыть файл на чтение
    json_date = json.load(f)
# print(len(json_date['rss']['channel']['items'])) # узнаем количество  новостей с списке
# pprint(json_date['rss']['channel']['items'][0]) # выведем первую новость
    
# with open('newsafr2.json', 'w') as f: # откроем новый(несуществующий) файл на запись 
    # json.dump(json_date, f) # сохраним  данные в открытый файл на запись, кирилица сохранилась в виде "\u043f\u043e"
    # json.dump(json_date, f, ensure_ascii=False) # добавили флаг ensure_ascii=False и в сохраненном файле кирилица в читаемом виде
    # json.dump(json_date, f, ensure_ascii=False, indent=4) # с флагом indent=4 сохраним в красивом виде

# d = {"hello": "python", "goodbye": 'java'}
# result = json.dumps(d)
# print(type(result))

# Формат yaml
import yaml
with open('newsafr2.yaml', 'w') as f: # откроем новый(несуществующий) файл на запись 
    yaml.dump(json_date, f, allow_unicode=True, default_flow_style=False) # со
    
#Формат xml
import xml.etree.ElementTree as ET # импорт модуля   для работы xml
# parser = ET.XMLParser(encoding='utf-8')
# tree = ET.parse('newsafr.xml', parser)
tree = ET.parse('newsafr.xml')
root = tree.getroot()
# print(root.tag)
# print(root.text)
# print(root.attrib)

