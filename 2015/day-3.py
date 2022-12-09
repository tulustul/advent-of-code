from utils import *

data = read(get_day(__file__))

def step1():
    from collections import defaultdict
    visits = defaultdict(int)
    x,y = 0,0
    visits[(x,y)] += 1

    for c in data:
        if c == '>':
            x +=1
        elif c == 'v':
            y += 1
        elif c == '<':
            x -= 1
        elif c == '^':
            y -= 1

        visits[(x,y)] += 1
    print(len(visits))

def step2():
    from collections import defaultdict

    def move(x,y,c):
        if c == '>':
            return x + 1, y
        elif c == 'v':
            return x, y + 1
        elif c == '<':
            return x - 1, y
        elif c == '^':
            return x, y - 1
        return x, y

    visits = defaultdict(int)
    sx,sy = 0,0
    rx,ry = 0,0
    visits[(sx,sy)] += 2

    for i in range(0, len(data), 2):
        sx, sy = move(sx, sy, data[i])
        rx, ry = move(rx, ry, data[i+1])

        visits[(sx,sy)] += 1
        visits[(rx,ry)] += 1
    print(len(visits))

if __name__ == '__main__':
    step1()
    step2()