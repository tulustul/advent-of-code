from utils import *

data = read_lines(get_day(__file__))

def step1():
    total_area = 0
    for line in data:
        dims = [int(t) for t in line.split('x')]
        areas = [dims[0]*dims[1], dims[1]*dims[2], dims[0]*dims[2]]
        total_area += sum(areas)*2+min(areas)

    print(total_area)

def step2():
    total_length = 0
    for line in data:
        dims = [int(t) for t in line.split('x')]
        combinations = [(dims[0]+dims[1])*2, (dims[0]+dims[2])*2, (dims[1]+dims[2])*2]
        total_length += min(combinations) + dims[0]*dims[1]*dims[2]
    print(total_length)

if __name__ == '__main__':
    step1()
    step2()