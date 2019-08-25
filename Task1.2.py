school = {'1а':30, '1б':27, '2б':24, '6а':28, '7в':21}
print('Для зміни кількості учнів у класі введіть команду CHANGE')
print('Для добавлення класу введіть команду ADDED')
print('Для вилучення класу введіть команду DELETE')
print('Для загальної кількості учнів введіть команду TOTAL')
print('Для закінчення введіть EXIT')
command = ''
while command != 'EXIT':
    command = input('Введіть команду:')
    if command == 'CHANGE':
        com_d1 = input('Введіть клас:')
        if com_d1 not in school:
            print('Вказаного класу не існує,або змініть розкладку!')
        else:
            com_count = 0
            while com_count <= 0:
                com_count = input('Введіть кількість учнів:')
                if com_count.isnumeric():
                    com_count = int(com_count)
                school[com_d1] = int(com_count)
            print(school)
        continue
    elif command == 'ADDED':
        com_d1 = input('Введіть новий клас:')
        if com_d1 in school:
            print('Введений клас вже існує!')
        else:
            com_count = 0
            while com_count <= 0:
                com_count = input('Введіть кількість учнів:')
                if com_count.isnumeric():
                    com_count = int(com_count)
            school[com_d1] = com_count
            print(school)
        continue
    elif command == 'DELETE':
        com_d1 = input('Введіть клас: ')
        if com_d1 not in school:
            print('Такого класу не існує!')
        else:
            school.pop(com_d1)
            print(school)
        continue
    elif command == 'TOTAL':
          summ = 0
          for i in school.values():
              summ = summ + i
          print(summ, 'загальна кількість учнів в школі')
          continue
print(school)










