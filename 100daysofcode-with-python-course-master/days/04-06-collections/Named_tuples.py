from collections import namedtuple

Human = namedtuple('Human', 'first_name last_name ethnicity')
h1 = Human('Chengiz','Khan','Mongol')
print(h1.ethnicity)

Movie = namedtuple('movie','name year imdb_score')
m1 = Movie('Gangs of Wasseypur','2012','8.9')
m2 = Movie('Pather Panchali','1963','8.1')
m3 = Movie('Dev D','2009','8.3')

movie_list = []
movie_list.append(m1)
movie_list.append(m2)
for movie in movie_list:
    print(movie.name)
