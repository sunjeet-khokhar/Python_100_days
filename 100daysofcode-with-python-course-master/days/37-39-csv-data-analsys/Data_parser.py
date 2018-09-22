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
        # parses the csv files as ordered dictionary
        data = csv.DictReader(f)
        for row in data:
            #print(row)
            max_temp = int(row.get('actual_max_temp'))
            if max_temp >= 90:
                hot_date = row.get('date')
                print(f'{hot_date} was a hot day')

def thanksgiving_parse():
    base_folder = os.path.dirname(__file__)
    filepath = os.path.join(base_folder, 'data', 'thanksgiving-2015-poll-data.csv')
    with open(filepath, 'r', encoding='utf-8') as f:
        # parses the csv files as ordered dictionary
        data = csv.DictReader(f)
        count = 0
        for row in data:
            if (str(row.get('What is typically the main dish at your Thanksgiving dinner?'))) == 'Chicken':
                count = count + 1
        print(f'The number of people who eat cxhicken on ThanksGving is = {count}')



#if __name__ == '__main__':
 #   data_read()
