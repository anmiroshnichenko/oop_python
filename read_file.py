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

# Нужно написать функцию, которая на вход принимает список блюд из cook_book и количество персон для кого мы будем готовить 
# На выходе мы должны получить словарь с названием ингредиентов и его количества для блюда.   
def get_shop_list_by_dishes(dishes, person_count):
    cook_book = format_recipes()    
    dict_ingredients = {}
    for dish  in dishes:
        for ingredient  in cook_book[dish]:            
            ingredient_name = ingredient.pop('ingredient_name')  
            t = ingredient.values()
            print(t)
            # print(ingredient['measure'])          
            measure = ingredient['measure']
            quantity = int(ingredient['quantity'])
            ingredient_amount = {}  
            # print(quantity * person_count)
            # dict_ingredients[ingredient_name] = ingredient['quantity'] = int('quantity') * 2
    return dict_ingredients



get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)




    




