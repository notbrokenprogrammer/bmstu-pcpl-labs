class ObjectRoot:
    '''Объкут для решения биквадартного уравнения'''
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c
        self.roots: list[float] = []
    def get_roots(self):
        '''Получение корней'''
        a, b, c = self.a, self.b, self.c
        D = b*b - 4*a*c
        if D > 0:
            x1 = (-b + (D)**0.5) / (2*a)
            x2 = (-b - (D)**0.5) / (2*a)
            x3 = -((-b + (D)**0.5) / (2*a))
            x4 = -((-b - (D)**0.5) / (2*a))
            self.roots.append(x1)
            self.roots.append(x2)
            self.roots.append(x3)
            self.roots.append(x4)
        
        elif D == 0:
            x1 = (-b) / 2*a
            x2 = -((-b) / 2*a)
            self.roots.append(x1)
            self.roots.append(x2)
    
    def roots_run(self):
        '''Вывод результата'''
        for root in self.roots:
            print(root)
