import sys

from models import ObjectRoot
from handlers import get_roots as functional_get_roots

def coef(index, promt) -> float:
    '''Функция, которая читает из параметров запуска коэффиценты и в случае неудачи просит ввести эти коэфиценты. '''
    try:
        coef_str = sys.argv[index]
    except IndexError:
        coef_str = input(promt)

    return float(coef_str)

def get_roots(a, b, c) -> list[float]:
    '''Вычисление корней'''
    result = []
    D = b*b - 4*a*c
    if D > 0:
        x1 = (-b + (D)**0.5) / (2*a)
        x2 = (-b - (D)**0.5) / (2*a)
        x3 = -((-b + (D)**0.5) / (2*a))
        x4 = -((-b - (D)**0.5) / (2*a))
        result.append(x1)
        result.append(x2)
        result.append(x3)
        result.append(x4)
   
    elif D == 0:
        x1 = (-b) / 2*a
        x2 = -((-b) / 2*a)
        result.append(x1)
        result.append(x2)

    return result

def start_def():
    '''Запуск процедурной парадигмы. '''
    a = coef(1, "Введите первый коэфицент: ")
    b = coef(2, "Введите второй коэфицент: ")
    c = coef(3, "Введите третий коэфицент: ")
    roots = get_roots(a, b, c)
    for root in roots:
        print(root)

def object_root():
    '''Запуск объектно ориентированной парадигмы. '''
    a = coef(1, "Введите первый коэфицент: ")
    b = coef(2, "Введите второй коэфицент: ")
    c = coef(3, "Введите третий коэфицент: ")
    object = ObjectRoot(a, b, c)
    object.get_roots()
    object.roots_run()

def handlers_run():
    '''Запуск фундаментальной парадигмы. '''
    a = coef(1, "Введите первый коэфицент: ")
    b = coef(2, "Введите второй коэфицент: ")
    c = coef(3, "Введите третий коэфицент: ")
    functional_get_roots(a, b, c)

def main():
    '''Поочерёдный запуск парадигм:'''
    
    print("Процедурной парадигма: ")
    start_def()

    print("Объектно ориентированная парадигма: ")
    object_root()

    print("Фундаментальная парадигма: ")
    handlers_run()






if __name__ == "__main__":
    main()