# Операции с файлом 
```
f = open('test.txt')
print(type(f))
date = f.read()
print(date, type(date))
f.close()
```

# Менеджер контекста
```
def is_closed(file_):
    if file_.closed:
        print('Файд закрыт')
    else:
       print('Файд открыт') 

with open('test.txt') as f: #конструкция сама позаботилась закрыть файл при выходе из контекста
    print(type(f))
    date = f.read()
    # is_closed(f)
is_closed(f)
```
# Чтение  данных из файла 

## Метод raed
```
with open('test.txt') as f: #конструкция сама позаботилась закрыть файл при выходе из контекста
    date = f.read()  #  метод read читае  полностью весь файл, если файл очень большой, твои проблемы
    print(date)
date += '\nЕще одна строка'
print(date)
 ```       
## Метод raedline
```
with open('test.txt') as f: #конструкция сама позаботилась закрыть файл при выходе из контекста
    # date = f.read()  # read читае  полностью весь файл, если файл очень большой, твои проблемы
    print(f.readline().strip()) #Это первая строка   readline - читает одну строку
    print(f.readline().strip()) #Это вторая
    print(f.readline().strip())
    print(f.readline().strip())
    print(f.readline().strip())
    print(f.readline().strip())
    print(f.readline() == '') #True  пустая стррока
    print(f.readline() is None) #False  пустая строка   файла
```       
## Метод raedlines  
```
with open('test.txt') as f:
    lines = f.readlines() #метод raedlines собирает в список все строки файла
    print(type(lines))
    print(len(lines))
    print(lines[1])
```
## Итерация -самый простой способ  читать из файла
```
with open('test.txt') as f:
    for line in f:
        print(line.strip())
    
with open('test.txt') as f:
    for idx, line in enumerate(f):
        print(idx, line.strip())    
```    
# Записывать информацию в файл
    -'r' — чтение (по умолчанию)
    -'w' — запись
    -'a' — запись в конец файл
#Режимы чтения/записи
    -'b' — двоичный режим (работаем с байтами)
    -'t' — текстовый режим (работаем со строками, по умолчанию)

## Метод write
```
with open('test.txt') as f: # будет ошибка
with open('test.txt', 'w') as f: # строка запишется(перезапишется) в файл, удалив все данные 
    f.write('Привет мир')  # строка запишется(перезапишется) в файл, удалив все данные 
    print(f.read()) #not readable - необходимо указать  режим по умолчанию 'r'

with open('test.txt', 'w') as f:
    f.write('Это первая строка\n')
with open('test.txt', 'a') as f:
    f.write('\nВторая_1 строка')  # строка  допишется  в   конец файла 
    print(f.read()) #not readable - необходимо указать  режим по умолчанию 'r'

with open('test.txt', 'rb') as f:  #двоичный режим (работаем с байтами)
    date = f.read()
    print(type(date))
    print(date)  

with open('test.txt', 'rb') as f: #двоичный режим (работаем с байтами)
    print(f.readline()) 
```
## Абсолютный и относительный путь к файлу
```
import os
import time
print(os.getcwd()) # посмотртеь абсолютный путь 
with open('path.txt', 'w') as f:
    f.write(f'{time.time()}')
with open('path.txt') as f:
    print(f.read())
print(os.getcwd()) # посмотртеь абсолютный путь 
file_path = os.path.join(os.getcwd(), 'path.txt') # os.path.join - функция для построения пути к файлу
print(file_path)

with open(file_path) as f: #откроем файл  по абсолютному пути
    print(f.read())

with open('/home/miroshnichenko_an/oop_python/path.txt') as f: #откроем файл  по абсолютному пути
    print(f.read())
```
## Использование вложенного контекста
```
with open('path.txt', 'r+') as f:
    f.write('Kakaytostroka')
    f.flush() # метод   моментально запишет все данные
    with open('path.txt') as f1: #вложенный контекст, сохранение  записи после выхода(закрытия) из контекста
        print(f1.read())
with open('path.txt') as f1: # можно не использовать вложенный контекст
        print(f1.read())
```
## Использование кодировок (по умолчанию UTF-8)
```
with open('utf.txt', 'w', encoding='utf-8') as f: #encoding='utf-8' задан по умолчанию
    f.write('Привет, мир')
with open('cp.txt', 'w', encoding='cp1251') as f: #изменили кодировку
    f.write('Привет, мир')
with open('utf.txt', 'rb') as f: #откроем в бинарном режиме
    print(f.read())
print()
with open('cp.txt', 'rb') as f: #откроем в бинарном режиме
    print(f.read())

with open('cp.txt') as f: #откроем cp.txt(cp1251) в текстовом режиме и получим ошибку кодировки
    print(f.read())
with open('cp.txt', 'r', encoding='cp1251') as f: #откроем cp.txt(cp1251) в текстовом режиме с указанием кодировки cp1251
    print(f.read())
```
## Распознавание   кодировки chardet
```
import urllib.request, chardet
rawdata = urllib.request.urlopen('http://yandex.ru/').read()
chardet.detect(rawdata)
# {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}
rawdata = urllib.request.urlopen('https://www.zeit.de/index').read()
chardet.detect(rawdata)
# {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}
```








