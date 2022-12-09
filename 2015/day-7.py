from utils import *

data = read_lines(get_day(__file__))

def parse_cmd(cmd):
    tokens = cmd.split()
    return tokens[:-2], tokens[-1]

def cache_value(cache, value, result):
    cache[value]=result
    return result

def get_value(wires, value, cache):
    if value in cache:
        return cache[value]

    if value.isdigit():
        return cache_value(cache, value, int(value))

    tokens = wires[value]

    if len(tokens) == 1:
        return cache_value(cache, value, get_value(wires, tokens[0], cache))

    if tokens[0] == 'NOT':
        return cache_value(cache, value, ~get_value(wires,tokens[1], cache))

    op, l, r = tokens[1], get_value(wires,tokens[0], cache), get_value(wires,tokens[2], cache)

    if op == 'LSHIFT':
        return cache_value(cache, value, l << int(tokens[2]))

    if op == 'RSHIFT':
        return cache_value(cache, value, l >> int(tokens[2]))

    if op == 'AND':
        return cache_value(cache, value, l & r)

    if op == 'OR':
        return cache_value(cache, value, l | r)


def step1():
    wires = {}
    for cmd in data:
        op, wire = parse_cmd(cmd)
        wires[wire] = op

    print(get_value(wires, 'a', {}))

def step2():
    wires = {}
    for cmd in data:
        op, wire = parse_cmd(cmd)
        wires[wire] = op

    value = get_value(wires, 'a', {})
    wires['b'] = [f'{value}']
    print(get_value(wires, 'a', {}))

if __name__ == '__main__':
    step1()
    step2()