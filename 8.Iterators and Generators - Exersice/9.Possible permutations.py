from itertools import  permutations

def possible_permutations(my_list):
    for per in permutations(my_list):
        yield list(per)

[print(n) for n in possible_permutations([1, 2, 3])]