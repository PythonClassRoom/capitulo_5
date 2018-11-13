def cuenta_atras(item):
    while item > 0:
        yield item
        item -=1
for i in cuenta_atras(5):
    print(i)

lista = [1,2,3]
gen = (7*item for item in lista)
for i in gen:
    print(i)