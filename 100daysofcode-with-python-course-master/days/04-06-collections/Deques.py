
# importing the required module
import timeit

# code snippet to be executed only once
mysetup = '''from collections import deque
import random'''

# code snippet whose execution time is to be measured
mycode = '''
million_ints_list = deque(range(1000000))
for x in range(10):
    index = random.choice(range(100))
    million_ints_list.remove(index)
    million_ints_list.insert(index, index)
'''

# timeit statement
print(timeit.timeit(setup=mysetup,stmt=mycode))

