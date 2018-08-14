import re

# when not to use regex

text = "There is so much sorrow in the world that it hurls me towards happiness"

print(text.startswith("There"))

print(text.replace('sorrow','beauty'))

# search matches a sub string , match matches a full string

print(re.search(r'is so much',text))

print(re.match(r'There is so much*',text))

string_to_search = "It is like super awesome to take the #100daysofcode challenge,i am at day 30"

m = re.match(r'.*(#\d+daysofcode).*',string_to_search)
print(m.groups()[0])

m = re.findall(r'\d+', string_to_search)
print(m)

string_to_search = '''Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been """Lore 
the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and 
scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into 
electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of
Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus
PageMaker including versions of Lorem Ipsum'''

# interesting to see if you use a * instead of a + here what will happen ?
# * give matches for 0 or more characters , * is 1 of more
m = re.findall(r'\w+',string_to_search)

print(m)
# get a list from a multi line string split by new line
print(string_to_search.split('\n'))

#find move names (from below list) that have 2 words in the title
movies = '''1. Citizen Kane (1941)
2. The Godfather (1972)
3. Casablanca (1942)
4. Raging Bull (1980)
5. Singin' in the Rain (1952)
6. Gone with the Wind (1939)
7. Lawrence of Arabia (1962)
8. Schindler's List (1993)
9. Vertigo (1958)
10. The Wizard of Oz (1939)'''

m = re.findall(r'\d+\.\s+([A-Za-z\']+\s+){3}\(\d+\)',movies)
m1 = re.findall(r'\d+\.\s+(?:[A-Za-z\']+\s+){2}\(\d+\)',movies)
print(m)
print(m1)

#find and replace one number with another

def find_and_replace(text):
    subbed = re.sub(r'\d+daysof\w+','100daysofPython',text)
    print(subbed)

text = ''' I am having fun doing #100daysofPython #200daysofnothing #300daysofighthing
'''

find_and_replace(text)

text = 'Use match vs search wisely'

print(re.match('.*search',text))
print(re.search('search',text))

# example that shows difference with and without the use of ?:
tweet = 'New PyBites article: Module of the Week - Requests-cache for Repeated API Calls - http://pybit.es/requests-cache.html … #python #APIs'
m = re.findall(r'((?:#|http)\S+)',tweet)
m1 = re.findall(r'((#|http)\S+)',tweet)
print(m)
print(m1)




