import csv

#открытие файла
with open('space.txt', encoding='utf8') as f:
    #запись файла в ридер
    reader = csv.reader(f, delimiter='*')
    ques = input()
    #начало "бесконечного" цикла
    while ques != 'stop':
        #установка флайга га проверку наличия корабля в файле
        fl = 0
        for row in reader:
            #нахождение корабля
            if row[0] == ques:
                print(f'Корабль {row[0]} был отправлен с планеты: {row[1]} и его направление движения было: {row[3]}')
                fl = 1
        #вывод ошибки если корабля нету в файле и флаг не сменился
        if fl == 0:
            print('error.. er.. ror..')
        ques = input()
