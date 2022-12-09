from utils import *
from itertools import *

data = read_lines(get_day(__file__))

def step1():
    cities = set()
    distances = {}
    for line in data:
        a,b,d=parse_line(line)
        cities.add(a)
        cities.add(b)
        distances[(a,b)]=d
        distances[(b,a)]=d

    perms = permutations(cities)

    min_d = 99999999
    for perm in perms:
        d = 0
        for i in range(len(perm) - 1):
            a = perm[i]
            b = perm[i+1]
            d += distances[(a,b)]
        if d < min_d:
            min_d = d

    print(min_d)


def step2():
    cities = set()
    distances = {}
    for line in data:
        a,b,d=parse_line(line)
        cities.add(a)
        cities.add(b)
        distances[(a,b)]=d
        distances[(b,a)]=d

    perms = permutations(cities)

    max_d = 0
    for perm in perms:
        d = 0
        for i in range(len(perm) - 1):
            a = perm[i]
            b = perm[i+1]
            d += distances[(a,b)]
        if d > max_d:
            max_d = d

    print(max_d)


def parse_line(line:str):
    tokens = line.split()
    return (tokens[0], tokens[2], int(tokens[4]))

if __name__ == '__main__':
    step1()
    step2()
