import re
import csv

def get_data():
    global main_data
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
    for i in range(1,4):
        list_1 = []
        with open(f'info_{i}.txt', encoding = 'utf-8') as f:
            s = f.read()
            
        os_prod = re.findall(r'Изготовитель ОС:\s*([\w|\w ]+)', s)
        os_name = re.findall(r'Название ОС:\s*([\w|\w ]+)', s)
        os_code = re.findall(r'Код продукта:\s*([\w|\w-]+)', s)
        os_type = re.findall(r'Тип системы:\s*([\w|\w |\w-]+)', s)
        list_1.append(os_prod[0])
        list_1.append(os_name[0])
        list_1.append(os_code[0])
        list_1.append(os_type[0])
        main_data.append(list_1)
        

def write_to_csv():
    get_data()
    with open('some.csv', 'w', encoding = 'utf-8') as file:
        writer = csv.writer(file)
        for row in main_data:
            writer.writerow(row)

write_to_csv()


with open('some.csv', encoding = 'utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

