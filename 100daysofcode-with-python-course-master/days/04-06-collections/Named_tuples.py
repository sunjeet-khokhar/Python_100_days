from collections import namedtuple

Human = namedtuple('Human', 'first_name last_name ethnicity')
h1 = Human('Chengiz','Khan','Mongol')
print(h1.ethnicity)
