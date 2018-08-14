from collections import Counter
import calendar
import itertools
import random
import re
import string
import requests

names = 'The majestic Magnificent Lord of Trivial ruminations'.split()
#print(names)

#for name in names:
    #print(name.title())

#orint words starting with M
for name in names:
    if name[0] in ['m','M']:
        print(name)

#now achieve the same using list comprehensions
new_names = [name for name in names if name[0] in ['m','M']]
print(new_names)


#assert new_names == names


def parsing_a_remote_txt_file(url):

    remote_text_content = requests.get(url)
    best_words = remote_text_content.text.lower().split()
    # okay we dont want a wall of text, lets just print the first 10 items
    print(best_words[:10])
    # get the top 3  common words from the response
    count = Counter(best_words)
    print(count.most_common(3))
    top_words = [word for word in best_words if word not in ['the','he','í']]
    count = Counter(top_words)
    print(count.most_common(3))
    #rmeove particular chars using a reg ex
    remove_chars = [re.sub(r'\w+',r' ',word) for word in best_words]
    print(remove_chars)


parsing_a_remote_txt_file('http://projects.bobbelderbos.com/pcc/harry.txt')


input_list = ['Nelson Mandela', 'Mohandas Ghandhi','Napolean Bonaparte', 'Sachin Tendulkar']


def converting_list_to_upper_case(input_list):
    output_list = list(set([name.upper() for name in input_list]))
    #enhance above list comprehension to remove duplicates
    #convert the data structure to a set, and then use sroted function with key to sort the list by last name
    print(sorted(input_list,key= lambda x: x.split()[1]))
    print(sorted(input_list,key= last_name))

def last_name(x):
    return x.split()[1]


def sort_list_by_shortest_first_name(input_list):
    output_list = list(set([name.upper() for name in input_list]))
    print(sorted(output_list,key = lambda x: len(x.split()[0])))


def reversing_list_items(name):
    first, last = name.split()
    #return ' '.join([last, first])
    return f'{last} hee haaw {first}'


reversed_name = [reversing_list_items(name) for name in input_list]
#reversed_name = reversing_list_items(input_list)
print(list(set(reversed_name)))

converting_list_to_upper_case(input_list)

sort_list_by_shortest_first_name(input_list)
