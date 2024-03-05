# Когда вы открыли файл на чтение, вам нужно подумать как в цикле,
# считывая построчно информацию из файла, последовательно получать данные по каждому блюду,
# добавлять эти данные в список словарей заданной конфигурации.
# В цикле вы в первой строке получаете названия блюда и сохраняете в переменную.
# Во второй строке вы получаете количество ингредиентов, которое тоже сохраняете в переменную.
# Далее идет еще один вложенный цикл в котором вы уже перебираете ингредиенты.
# Количество итераций в этом цикле вы получаете из переменной с количеством ингредиентов.
# Перебирая ингредиенты вы через сплит по символу " | " получаете название ингредиента, количество и единицы измерения.
# Из этих данных вы формируете словарик, который тут же добавляете в список словарей.

cook_book = {} 
with open('recipes.txt') as f:   
    # print(f.readline().strip())
    # print(f.readline().strip())
    # print(f.readline().strip())
    # print(f.readline().strip())
    # print(f.readline().strip())
    # print(f.readline().strip())
    # print(f.readline().strip())
    for ind,  line  in enumerate(f):
        line_1 = line.strip()
        # line_2 = line.strip()
        if ind ==  2:
            continue
        print(line_1)
    # считываем строку
    #     line_ = line
    #     print(line)

    #     line_1 = f.readline().strip()
    # #     # line_1 = f.readline().strip()
    # # прерываем цикл, если строка пустая
    #     # if line == '':
    #     if line == '':
    #         break
    
    #     print(line, line_1)
    # lines_1 = f.readlines()[0]  
    # lines_2 = f.readlines()[1] 
    # print(lines_2) 
    # for i, line in enumerate(f):
    #     print(line)

        
    #     print(line.split('|'))
        # if line.strip() == '':
        #     for line in f:
        #         pass
                # print(line.strip())
        # print(index, line.strip())


# with open('recipes.txt') as f:    
#     for index, line in enumerate(f):
#         if index == 0:
#             dish = line
#         elif index == 1:
#             ingradients = line
#         else:
#             print(line.strip())
#             # for ingr in line:
#             #     print(ingr.split(" | "))
            
    

    # print(dish, ingradients)
    

            
     

        


    




