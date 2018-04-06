def validar(x0,a,D):
    while (D<3):
        D  = int(input("Inserta una cantidad de digitos mayor a 3: "))
    while ((len(str(x0))!=(D))):
        x0  = int(input("Inserta un valor de semilla x0 valido: "))
    while ((len(str(a))!=(D))):
        a  = int(input("Inserta un valor de constante a valido: "))
    generar(x0, a)

def generar(x0, a):
    for i in range(n+1):
        y0=a*x0
        xi = int(digitos_centrales(str(y0),D))
        ri = xi/10**D
        if(ri<0.0):
            print("Error, la semilla no es valida para generar {} numeros aleatorios".format(n+1))
            semilla_insuficiente()
            break
        r.append(ri)
        x0=xi

def digitos_centrales(s,k):
    # Para asegurar que el número no sea negativo usamos el max(tupla)
    m = max((len(s)-k)//2, 0) # El // es para que el resultado de la división sea entera
    return s[m:m+k]

def imprimir():
    if(len(r)!=0):
        print("Los {} números pseudoaleatorios son: ".format(n+1))
    for idi, ri in enumerate(r):
        print("{} : {}".format(idi+1, ri))

def guardar():
    with open('multiplicador_constante.txt', 'w') as f:
        for num  in r:
            f.write(str(num)+'\n')

if __name__ == '__main__':
    D = int(input("Inserte la cantidad de D digitos: "))
    x0 = int(input("Inserta el valor semilla x0: "))
    a = int(input("Inserta una constante a: "))
    n = int(input("¿Cuantos números pseudoaleatorios desea?: "))-1
    r = []
    validar(x0,a,D)
    imprimir()
    guardar()