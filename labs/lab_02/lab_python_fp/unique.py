class Unique():
    '''
    Итератор, которы принимает массив данных и 
    возвращает этот же массив, но без повторов
    '''
    def __init__(self, items, **kwargs):
        self.items = iter(items)
        self.ignore_case = False
        if kwargs.get("ignore_case") != None:
            self.ignore_case = kwargs.get("ignore_case")
        self.arr = []

    def __next__(self):
        if self.ignore_case:
            for word in self.items:
                if isinstance(word, str): # Проверка на то строка это или нет
                    val: str = word.upper()
                    if val not in self.arr:
                        self.arr.append(val)
                        return word
                else:
                    if word not in self.arr:
                        self.arr.append(word)
                        return word
            raise StopIteration       
        else:
            for word in self.items:
                if word not in self.arr:
                    self.arr.append(word)
                    return word
                    
            raise StopIteration # Нжуен для того чтобы for, который я вызываю пеонял, что список кончился, иначе выведет None

    def __iter__(self):
        return self