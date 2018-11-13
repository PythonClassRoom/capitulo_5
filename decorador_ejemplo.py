class Decorador:
    def __init__(self,f):
        self.f = f

    def __call__(self):
        print('inicio', self.f.__name__)
        self.f()
        print('final', self.f.__name__)

@Decorador
def funcion():
    print('hola, soy la funcion')

funcion()
pass


def principal(f):
    def nueva():
        print('inicio', f.__name__)
        f()
        print('final', f.__name__)
    return nueva

@principal
def decorada():
    print("decorada")









decorada()