import csv
def sol(data):
    with open(data, 'r', encoding='utf-8') as f:
        r = csv.reader(f)
        for line in r:
            s1, s2 = '', ''
            for i in line[1].replace(',', ''):
                if i == '3':
                    s1 += '1'
                    s2 += '2'
                elif i == '4':
                    s1 += '2'
                    s2 += '2'
                elif i == '6':
                    s1 += '1'
                    s2 += '5'
                else:
                    s1 += i
                    s2 += '0'
            print(int(s1), int(s2))
            
data = 'test.csv'
sol(data)