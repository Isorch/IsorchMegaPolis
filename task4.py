import csv


def password(planet, code):
    pswd = planet[-3:].upper() + code.split('-')[0][1:3][::-1].upper() + planet[:3].upper()
    return pswd

with open('space.txt', encoding='utf8') as f:
    file = open('space_uniq_password.csv', 'w')
    reader = csv.reader(f, delimiter='*')
    for row in reader:
        if row[0] == 'ShipName':
            for i in range(len(row)):
                el = row[i] + ';'
                file.writelines(el)
            file.writelines('password')
            file.writelines('\n')  
        pswd = password(row[1], row[0])
        for i in range(len(row)):
            el = row[i] + ';'
            file.writelines(el)
        file.writelines(pswd)
        file.writelines('\n')
            

