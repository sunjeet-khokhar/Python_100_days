import csv
from collections import namedtuple
from collections import defaultdict

Movie = namedtuple('movie','name year imdb_score')
movie_details = []
movie_list = defaultdict(list)
with open('movie_metadata.csv',encoding='utf-8',mode='r') as movies_csv:
    for row in csv.DictReader(movies_csv):
        #print(row)
        director = row['director_name']
        name = row['movie_title'].replace('\xa0','')
        year = row['title_year']
        imdb_score = row['imdb_score']
        mov = Movie(name,year,imdb_score)
        movie_list[director].append(mov)
# print all the diretors (and their moves) rated more than or equal to 8.0
for director,movie in movie_list.items():
    for movie in movie:
        if float(movie.imdb_score) >= 8.0:
            print(director,movie.name)

# print all movies per director name
for director,movie in movie_list.items():
    print(director,movie)

# print the names of movies by Akira Kurosawa
for director,movie in movie_list.items():
    if director == 'Akira Kurosawa':
        for movie in movie:
            print(movie.name)












