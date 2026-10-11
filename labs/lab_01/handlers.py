def get_roots(a, b, c):
    '''Получение корней'''
    D = b*b - 4*a*c
    result: list[float] = []
    match D:
        case v if v > 0:
            x1 = (-b + (D)**0.5) / (2*a)
            x2 = (-b - (D)**0.5) / (2*a)
            x3 = -((-b + (D)**0.5) / (2*a))
            x4 = -((-b - (D)**0.5) / (2*a))
            result.append(x1)
            result.append(x2)
            result.append(x3)
            result.append(x4)
        case 0:
            x1 = (-b) / (2*a)
            x2 = -((-b) / (2*a))
            result.append(x1)
            result.append(x2)

    for res in result:
        print(res)