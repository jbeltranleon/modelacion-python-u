def validar(x,m):
    while (m<0):
        m  = int(input("Inserta un valor m positivo: "))
    print("Validar")
    generar(x,m)

def generar(x,m):
    for i in range(cantidad):
        x.append((x[len(x)-1]+x[i])%m)
        ri = x[len(x)-1]/(m-1)
        r.append(ri)

def imprimir():
    if(len(r)!=0):
        print("Los {} números pseudoaleatorios son: ".format(cantidad))
    for idi, ri in enumerate(r):
        print("{} : {}".format(idi+1, ri))

def guardar():
    with open('congruencial_aditivo.txt', 'w') as f:
        for num  in r:
            f.write(str(num)+'\n')

if __name__ == '__main__':
    n = int(input("Ingrese la cantidad de dígitos n de su secuencia: "))
    x = []
    for i in range(n):
        x.append(int(input("Ingresa el valor de x{}: ".format(i+1))))
    m = int(input("Ingresa el valor del modulo m: "))
    cantidad = int(input("¿Cuantos números desea generar?"))
    r = []
    validar(x,m)
    imprimir()
    guardar()