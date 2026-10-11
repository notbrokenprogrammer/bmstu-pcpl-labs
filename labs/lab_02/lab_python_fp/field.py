from lab_python_fp.gen_random import gen_random
goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'color': 'black'}
]

def field(items: list[dict], *args):

    if len(args) == 1:
        for dictionary in items:
            value = dictionary.get(args[0])
            yield value
    else:
        arr = {}
        for dictionary in items: #{'title': 'Ковер', 'price': 2000, 'color': 'green'},
            for a in args: #a = 'title'
                value = dictionary.get(a)
                if value is not None:
                    arr[a] = value
            yield arr


# def main():
#     for i in field(goods, 'title', 'color'):
#         print(i)
#     print("-------------------------")
#     for i in gen_random(5, 1, 3):
#         print(i)

# if __name__ == "__main__":
#     main()
    
    # if len(args) == 1:
    #     arr: list[any] = []
    #     for dictionary in items:
    #         for elem in dictionary:
    #             for i in args:
    #                 if elem == i:
    #                     arr.append(dict[elem])
