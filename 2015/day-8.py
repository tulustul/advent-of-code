from utils import *

data = read_lines(get_day(__file__))

def step1():
    literals = sum(len(s) for s in data)
    in_memory = sum(in_memory_len(s) for s in data)

    print(literals - in_memory)


def step2():
    print(encoded('"abc"'))

    encoded_s = sum(len(encoded(s)) + 2 for s in data)
    literals = sum(len(s) for s in data)
    in_memory = sum(in_memory_len(s) for s in data)

    print(encoded_s - literals)

def in_memory_len(s:str):
    count = 0
    skip = 0
    for i in range(len(s)):
        ss = s[i:]
        if skip:
            skip -=1
            continue
        if ss.startswith('"'):
            continue
        if ss.startswith('\\"'):
            count += 1
            skip = 1
            continue
        if ss.startswith('\\\\'):
            count += 1
            skip = 1
            continue
        if ss.startswith("\\x"):
            count += 1
            skip = 3
            continue
        count +=1
    return count


def encoded(s:str):
    return s.replace('\\', '\\\\').replace('\"', '\\"')

if __name__ == '__main__':
    step1()
    step2()
