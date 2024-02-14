import csv

with open('space.txt', encoding='utf8') as f:
    file = open('space_new.txt', 'w', encoding='utf8')
    #запись файла в ридер
    reader = csv.reader(f, delimiter='*')
    #проход по ридеру
    for row in reader:
        #если находится нулеыое значение, то заменяется
        if row[2] == "0 0":
            ShipName = row[0]
            ShipName = ShipName.split('-')
            firstnum = int(ShipName[1][0])
            secondnum = int(ShipName[1][1])
            xd = int(row[-1].split()[0])
            yd = int(row[-1].split()[1])
            planet = len(row[1])
            if firstnum > 5:
                x = firstnum + xd
            if firstnum <= 5:
                x = -(firstnum + xd) * 4 + planet
            if secondnum > 3:
                y = secondnum + planet + yd
            if secondnum <= 3:
                y = -(firstnum + yd) * secondnum
            row[2] = f'{x} {y}'
        #поиск кораблей чей код оканчивается на 'V'
        if row[0].split('-')[0][-1] == 'V':
            print(row[0])
        #запись в новый файл
        for i in range(len(row) - 1):
            el = row[i] + '*'
            file.writelines(el)
        file.writelines(row[-1])
        file.writelines('\n')
    file.close()



                    