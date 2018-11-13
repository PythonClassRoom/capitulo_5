#Esto es un ejemplo de iterador

class CuentaAtras:
    def __init__(self,start):
        self.count = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.count <= 0:
            raise StopIteration
        r =self.count
        self.count -= 1
        return r

for i in CuentaAtras(10):
    print(i)


class Rango:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        self.current += 1
        return self.current - 1

for i in Rango(5,9):
    print(i)