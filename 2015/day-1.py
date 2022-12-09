from utils import *

data = read(get_day(__file__))

def step1():
    from collections import Counter

    c = Counter(data)
    print(c['('] - c[')'])

def step2():
    floor = 0
    for i, c in enumerate(data):
        floor += 1 if c == '(' else -1
        if floor == -1:
            print(i+1)
            return

if __name__ == '__main__':
    step1()
    step2()