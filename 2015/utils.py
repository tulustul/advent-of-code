import re

day_regex = re.compile('^.*day-(\d)\.py$')

def read(day: int):
    with open(f'inputs/input-{day}') as f:
        return f.read()

def read_lines(day: int):
    with open(f'inputs/input-{day}') as f:
        return [line.replace('\n', '') for line in f.readlines()]

def get_day(file_name:str):
    return day_regex.findall(file_name)[0]