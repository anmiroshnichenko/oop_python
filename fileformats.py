# Формат csv
# import csv  # библиотека для работы с csv
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
print(root.tag)
print(root.text)
print(root.attrib)

