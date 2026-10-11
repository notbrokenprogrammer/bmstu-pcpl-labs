# def print_result(func):
# from collections.abc import Callable collections Абстрактный класс, который характеризует базовые объекты Callable[[str], None]

def print_result(func):
    def wrapper(*args, **kwargs):
        val = func(*args, **kwargs)
        print(func.__name__)
        match val:
            case dict():
                for key in val:
                    print(str(key) + " = " + str(val[key]))
            case list():
                for i in val:
                    print(i)
            case _:
                print(val)
        return val
        
    return wrapper

@print_result
def test_1():
    return 1

@print_result
def test_2():
    return 'iu5'

@print_result
def test_3():
    return {'a': 1, 'b': 2}

@print_result
def test_4():
    return [1, 2]

if __name__ == '__main__':
    print('!!!!!!!!!!!!!')
    # result = test_1() + 10
    # print(result)
    test_1()
    test_2()
    test_3()
    test_4()

