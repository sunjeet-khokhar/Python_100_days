import os
import csv

read_data =[]

def data_read():
    base_folder = os.path.dirname(__file__)
    filepath = os.path.join(base_folder,'data','NYC_Weather.csv')
    with open(filepath,'r',encoding='utf-8') as f:
        next(f, None)
        data = [row for row in (csv.reader(f.read().splitlines()))]
    return data[1]

def data_dict_read():
    base_folder = os.path.dirname(__file__)
    filepath = os.path.join(base_folder, 'data', 'NYC_Weather.csv')
    with open(filepath, 'r', encoding='utf-8') as f:
        data = csv.DictReader(f)
        for row in data:
            print(row)
            print(row.get('actual_max_temp'))


#if __name__ == '__main__':
 #   data_read()
