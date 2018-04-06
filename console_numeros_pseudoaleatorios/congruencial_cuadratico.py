def validar(x0,a,b,c):
    while (x0<0):
        x0  = int(input("Inserta un valor de semilla x0 positivo: "))
    while (a%2 != 0):
        a  = int(input("Inserta un valor par para a: "))
    while (c%2 == 0):
        c  = int(input("Inserta un valor impar para c: "))
    #while ((b-1)%4 != 1):
        #b  = int(input("Inserta un valor valido para b: "))
    generar(x0,a,b,c) 

def generar(x0,a,b,c):
    for i in range(n+1):
        xi = ((a*(x0**2))+(b*x0)+c)%m
        ri = xi/(m-1)
        r.append(ri)
        x0=xi

def imprimir():
    if(len(r)!=0):
        print("Los {} números pseudoaleatorios son: ".format(n+1))
    for idi, ri in enumerate(r):
        print("{} : {}".format(idi+1, ri))

def guardar():
    with open('congruencial_cuadratico.txt', 'w') as f:
        for num  in r:
            f.write(str(num)+'\n')

if __name__ == '__main__':
    x0 = int(input("Inserta el valor semilla x0: "))
    m = 2 **(int(input("Inserta la potencia de dos g que va a generar el número m: ")))
    a = int(input("Inserta una constante a: "))
    b = int(input("Inserta una constante b: "))
    c = int(input("Inserta una constante c: "))
    n = m-1
    r = []
    validar(x0,a,b,c)
    imprimir()
    guardar()