def validar(x0,a,c):
    while (x0<0):
        x0  = int(input("Inserta un valor de semilla x0 positivo: "))
    while (a<0):
        a  = int(input("Inserta un valor a positivo: "))
    while (c<0):
        c  = int(input("Inserta un valor c mayor a 0, si desea que c sea igual a 0 use el algoritmo congruencial multiplicativo: "))
    #Falta validar que c sea relativamente primo a m
    generar(x0,a,c)

def generar(x0,a,c):
    for i in range(n+1):
        xi = ((a*x0)+c)%m
        ri = xi/(m-1)
        r.append(ri)
        x0=xi

def imprimir():
    if(len(r)!=0):
        print("Los {} números pseudoaleatorios son: ".format(n+1))
    for idi, ri in enumerate(r):
        print("{} : {}".format(idi+1, ri))

def guardar():
    with open('lineal.txt', 'w') as f:
        for num  in r:
            f.write(str(num)+'\n')

if __name__ == '__main__':
    x0 = int(input("Inserta el valor semilla x0: "))
    a = 1 + 4*(int(input("Inserta una constante k que va a generar la constante multiplicativa a: ")))
    c = int(input("Inserta una constante aditiva c: "))
    m = 2 ** (int(input("Inserta la potencia de dos g que va a generar el número m: ")))
    n = m-1
    r = []
    validar(x0,a,c)
    imprimir()
    guardar()