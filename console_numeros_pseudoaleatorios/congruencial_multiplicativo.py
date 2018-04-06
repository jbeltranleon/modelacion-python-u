def validar(x0,a,m):
    while (x0<0):
        x0  = int(input("Inserta un valor de semilla x0 positivo: "))
    while (a<0):
        a  = int(input("Inserta un valor a positivo: "))
    while (m<0):
        m  = int(input("Inserta un valor m positivo: "))
    #Falta validar que c sea relativamente primo a m
    generar(x0,a,m)  

def generar(x0,a,m):
    for i in range(n+1):
        xi = (a*x0)%m
        ri = xi/(m-1)
        r.append(ri)
        x0=xi

def imprimir():
    if(len(r)!=0):
        print("Los {} números pseudoaleatorios son: ".format(n+1))
    for idi, ri in enumerate(r):
        print("{} : {}".format(idi+1, ri))

def guardar():
    with open('congruencial_multiplicativo.txt', 'w') as f:
        for num  in r:
            f.write(str(num)+'\n')

if __name__ == '__main__':
    print("El algoritmo congruencial m ultiplicativo surge del algoritmo congruencial lineal cuando c = 0")
    x0 = int(input("Inserta el valor semilla x0: "))
    a = 3 + 8*(int(input("Inserta una constante k que va a generar la constante multiplicativa a: ")))
    m = 2 ** (int(input("Inserta la potencia de dos g que va a generar el número m: ")))
    n = (m//4)-1
    r = []
    validar(x0,a,m)
    imprimir()
    guardar()