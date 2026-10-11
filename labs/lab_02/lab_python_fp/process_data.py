import sys
import json

from lab_python_fp.print_result import print_result
from lab_python_fp.field import field
from lab_python_fp.unique import Unique
from lab_python_fp.cm_timer import cm_timer_1
from lab_python_fp.gen_random import gen_random

path = '/Users/a1/BMSTU/COURSE_PCPL_MAIN/labs/lab_02/data_light.json'

with open(path) as f:
    data = json.load(f)

# print(data[1])

@print_result
def f1(data): 
    arr: list[str] = []
    for elem in field(data, "job-name"):
        arr.append(elem)
    
    arr = sorted(arr, key=str.upper)
    target = Unique(arr, ignore_case=True)
    arr = []
    for t in target:
        arr.append(t)
    return arr
    
@print_result
def f2(arg):
    return list(filter(lambda s: s.split(" ")[0].upper() == "ПРОГРАММИСТ", arg))
    

@print_result
def f3(arg):
    return list(map(lambda s: s + " с опытом Python", arg))


@print_result
def f4(arg):
    arr: list[str] = []
    for price, el in zip(gen_random(len(arg), 100000, 200001), arg):
        arr.append(el + ", зарплата " + str(price) + " руб.")
    return arr

if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))