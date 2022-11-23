secret = 'iwrupvqb'

def find_number(zeros):
    from hashlib import md5

    i = 0
    while True:
        _hash = md5(f'{secret}{i}'.encode())
        if _hash.hexdigest().startswith('0'*zeros):
            print(i)
            return
        i+=1


def step1():
    find_number(5)

def step2():
    find_number(6)

if __name__ == '__main__':
    step1()
    step2()