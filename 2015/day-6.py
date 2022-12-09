from utils import *

data = read_lines(get_day(__file__))

def parse_coords(coords):
    return [int(x) for x in coords.split(',')]

def parse_cmd(cmd):
    tokens = cmd.split()
    if tokens[0] == 'toggle':
        return 'toggle', parse_coords(tokens[1]), parse_coords(tokens[3])
    elif tokens[1]=='on':
        return 'on', parse_coords(tokens[2]), parse_coords(tokens[4])
    return 'off', parse_coords(tokens[2]), parse_coords(tokens[4])


def step1():
    lights = [False]*1000*1000

    for cmd in data:
        op, start_coords, end_coords = parse_cmd(cmd)
        for x in range(start_coords[0], end_coords[0]+1):
            for y in range(start_coords[1], end_coords[1]+1):
                i = x*1000+y
                if op == 'toggle':
                    lights[i] = not lights[i]
                else:
                    lights[i] = op == 'on'


    print(sum(lights))

brightness = {
    'off': -1,
    'on': 1,
    'toggle': 2,
}


def step2():
    lights = [0]*1000*1000

    for cmd in data:
        op, start_coords, end_coords = parse_cmd(cmd)
        for x in range(start_coords[0], end_coords[0]+1):
            for y in range(start_coords[1], end_coords[1]+1):
                i = x*1000+y
                lights[i] = max(0, lights[i] + brightness[op])

    print(sum(lights))

if __name__ == '__main__':
    step1()
    step2()