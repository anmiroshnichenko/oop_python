# Когда вы открыли файл на чтение, вам нужно подумать как в цикле,
# считывая построчно информацию из файла, последовательно получать данные по каждому блюду,
# добавлять эти данные в список словарей заданной конфигурации.
# В цикле вы в первой строке получаете названия блюда и сохраняете в переменную.
# Во второй строке вы получаете количество ингредиентов, которое тоже сохраняете в переменную.
# Далее идет еще один вложенный цикл в котором вы уже перебираете ингредиенты.
# Количество итераций в этом цикле вы получаете из переменной с количеством ингредиентов.
# Перебирая ингредиенты вы через сплит по символу " | " получаете название ингредиента, количество и единицы измерения.
# Из этих данных вы формируете словарик, который тут же добавляете в список словарей.

from pprint import pprint

# Задача №1
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Читать список рецептов из  файла recipes.txt
#Должен получится следующий словарь:
# cook_book = {
#   'Омлет': [
#     {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
#     {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
#     {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
#     ],
#   'Утка по-пекински': [
#     {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
#     {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
#     {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
#     {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
#     ],
#   'Запеченный картофель': [
#     {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
#     {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
#     {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
#     ]
#   }

def format_recipes():
    cook_book = {} 
    with open('recipes.txt', 'r', encoding='utf-8') as f:
        book_line = f.readline().strip()
        while book_line != '':
            food_dish =  book_line       
            number_ingredients = int(f.readline().strip())
            ingredients = []
            for number in range(number_ingredients):
                ingredient = f.readline().strip().split(' | ')         
                ingredients_dict = {'ingredient_name': ingredient[0], 'quantity': ingredient[1], 'measure': ingredient[2]}            
                ingredients.append(ingredients_dict)           
            cook_book[food_dish] = ingredients
            f.readline()
            book_line = f.readline().strip() 
    return cook_book

# pprint(format_recipes())


# Задача №2
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Нужно написать функцию, которая на вход принимает список блюд из cook_book и количество персон для кого мы будем готовить 
# На выходе мы должны получить словарь с названием ингредиентов и его количества для блюда:
# {
#   'Картофель': {'measure': 'кг', 'quantity': 2},
#   'Молоко': {'measure': 'мл', 'quantity': 200},
#   'Помидор': {'measure': 'шт', 'quantity': 4},
#   'Сыр гауда': {'measure': 'г', 'quantity': 200},
#   'Яйцо': {'measure': 'шт', 'quantity': 4},
#   'Чеснок': {'measure': 'зубч', 'quantity': 6}
# }

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = format_recipes()    
    dict_ingredients = {}
    for dish  in dishes:
        for ingredient  in cook_book[dish]:            
            ingredient_name = ingredient.pop('ingredient_name')            
            quantity = int(ingredient['quantity']) * person_count
            ingredient['quantity'] = quantity
            ingredient_amount = {}              
            dict_ingredients[ingredient_name] = ingredient
    return dict_ingredients

# pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

# Задача №3
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# В папке ./sorted лежит некоторое количество файлов. Считайте, что их количество и имена вам заранее известны.
# Необходимо объединить их в один по следующим правилам:
#   1. Содержимое исходных файлов в результирующем файле должно быть отсортировано по количеству строк в них 
#   (то есть первым нужно записать файл с наименьшим количеством строк, а последним - с наибольшим)
#   2. Содержимое файла должно предваряться служебной информацией на 2-х строках: имя файла и количество строк в нем
# Например даны файлы: 
# 1.txt:
#-------------------------------
# Строка номер 1 файла номер 1
# Строка номер 2 файла номер 1
#-------------------------------
# 2.txt:
#-------------------------------
# Строка номер 1 файла номер 2
#--------------------------------
# Должен  получится итоговый файл:
#----------------------------------
# 2.txt
# 1
# Строка номер 1 файла номер 2
# 1.txt
# 2
# Строка номер 1 файла номер 1
# Строка номер 2 файла номер 1
#-------------------------------------  

import os

# def merge_files():
#     files = os.listdir('sorted')
#     # print(files)
#     all_files = []

#     for file in files:
#         # print(file)
#         with open(f'sorted/{file}') as f:
#             line = f.read()
#             # f.seek(0)
#             all_files.append({'name': file, 'count_lines': len(f.readlines()), 'text': line})

#             # print(line)
#     print(all_files)

# merge_files()


def merge_files():
    files = os.listdir('sorted')
    # print(files)
    all_files = []


    for file in files:
        # print(file)
        with open(f'sorted/{file}') as f:
            # line = f.read()
            line = f.readlines()
            count_string = len(line) 
            # line = f.read()
            # f.seek(0)
            all_files.append({'file_name': file, 'line_count': count_string, 'content': ''.join(line)})
    sorted_all_files = sorted(all_files, key=lambda x: x['line_count'])        
    # print(sorted_all_files)    
    with open('sorted/merge_file', 'a') as f:
        for text in sorted_all_files:
            # print(text['file_name'])
            f.write(text['file_name'] + '\n')
            f.write(str(text['line_count']) + '\n')
            f.write(text['content'])           
    
merge_files()






# file_1 = []
# path = 'sorted/1.txt'
# all_files[0].append(os.path.basename(path) + '\n')
# with open(path) as f:
#     lines = f.readlines() #метод raedlines собирает в список все строки файла
#     all_files[0].append(str(len(lines)) + '\n')
#     all_files[0].append(''.join(lines))    

# all_files[1].append(file_1) 
# print(file_1[1])
# print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

# file_2 = []
# path = 'sorted/2.txt'
# file_2.append(os.path.basename(path) + '\n')
# with open(path) as f:
#     lines = f.readlines() #метод raedlines собирает в список все строки файла
#     file_2.append(str(len(lines)) + '\n')
#     file_2.append(''.join(lines))    

# print(file_2[1])
# int(file_1[1]),  int(file_2[1])

# all_files.extend(file_1, file_2)
  

# for line in file_1:
#     print(line)
#     with open('sorted/merge_file', 'a') as f:
#         f.write(line)
#     # f.write(len_1)
#     # f.write(''.join(file_1))



# with open('sorted/2.txt') as f:
#     lines = f.readlines() 
#     # print(type(lines))
#     print(len(lines))
#     print(lines)

# with open('sorted/3.txt') as f:
#     lines = f.readlines() 
#     # print(type(lines))
#     print(len(lines))
#     print(lines)




    




