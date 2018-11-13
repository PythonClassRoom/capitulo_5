#como leer archivos



with open('archivo_prueba.txt', 'r+') as f:
    a = f.readline()
    f.write('\n'+a *2 + '\n')

pass