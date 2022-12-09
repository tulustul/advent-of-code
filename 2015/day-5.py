from utils import *

data = read_lines(get_day(__file__))

vowels = 'aeiou'
black_list = ['ab', 'cd', 'pq', 'xy']

def step1():
    nice_words = 0
    for s in data:
        is_forbidden = False
        for forbidden in black_list:
            is_forbidden = forbidden in s
            if is_forbidden:
                break;

        if is_forbidden:
            continue


        included_vowels = 0
        last_letter = ''
        has_twice_in_a_row = False
        for c in s:
            if c in vowels:
                included_vowels += 1
            if not has_twice_in_a_row:
                if c == last_letter:
                    has_twice_in_a_row = True
                last_letter = c

        if not has_twice_in_a_row or included_vowels < 3:
            continue

        nice_words += 1

    print(nice_words)


def step2():
    nice_words = 0
    for s in data:
        repeats_twice = False
        middle = False
        for i in range(len(s)):
            start = s[:i]
            end = s[i:]
            if not repeats_twice and len(end) >= 2:
                repeats_twice = end[:2] in start
            if not middle and len(start) >= 2:
                middle = end[0] == start[-2]

        if repeats_twice and middle:
            nice_words +=1

    print(nice_words)



if __name__ == '__main__':
    step1()
    step2()