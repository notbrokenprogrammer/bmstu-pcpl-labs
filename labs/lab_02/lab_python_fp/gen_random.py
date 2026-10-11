import random

def gen_random(num_count, begin, end):
    '''Генерирование случайного диапозона с заданным min и max, а так же количества'''
    for _ in range(num_count):
        yield random.randint(begin, end)
