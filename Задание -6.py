goods = int(input('Введите кол-во товара- '))
my_list = []
my_analys = {}
num = 0
for i in range(goods):
    goods_dict = dict({'name': input("введите название "),
                       'price': int(input("Введите цену ")),
                       'quantity': int(input('Введите количество ')),
                       'unit': input("Введите единицу измерения ")})
    num += 1
    my_list.append((num, goods_dict))
    my_analys = dict(name=[], price=[], quantity=[], unit=['шт.'])
for i, x in my_list:
    my_analys['name'].append(x['name'])
    my_analys['price'].append(x['price'])
    my_analys['quantity'].append(x['quantity'])
    my_analys['unit'].__add__([])
print(*my_list, sep='\n')
print(my_analys)
