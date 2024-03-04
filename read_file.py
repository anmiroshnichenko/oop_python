cook_book = {} ## Создаем пустой словарь
with open('recipes.txt') as f: #Читаем файл
    # lines = f.read().splitlines() # read().splitlines() - чтобы небыло пустых строк
    # print(lines)   
    for line in f: # Проходимся по каждой строчке
        print(line.strip().replace("|", "")) #обрежет строку с обоих концов. Если аргумент не задан удалит пробелы с обоих концов строки
        # print(line.strip())
    #     # key, value = line.split(': ') # Разделяем каждую строку по двоеточии(в key будет - пицца, в value - 01)
    #     key, value = line.split()
    #     cook_book.update({key:value})	 # Добавляем в словарь
    
        # print(line)
    # lines = f.readlines()
    # print(lines[0])
    # for lines in f:
    #     for  line in lines:
    #         print(line)
        # key, value = line.split()
        # cook_book[key] = value
print(cook_book) # Вывод словаря на консоль
	




# for line in lines: # Проходимся по каждой строчке
# 	key,value = line.split(': ') # Разделяем каждую строку по двоеточии(в key будет - пицца, в value - 01)
# 	dic.update({key:value})	 # Добавляем в словарь

  