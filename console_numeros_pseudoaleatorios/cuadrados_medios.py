def validar(x0, D):
    while (D<3):
        D  = int(input("Inserta una cantidad de digitos mayor a 3: "))
    while ((len(str(x0))!=(D))):
        x0  = int(input("Inserta un valor de semilla valido: "))
    generar(x0)

def generar(x0):
    for i in range(n+1):
        y0=x0**2
        xi = int(digitos_centrales(str(y0),D))
        ri = xi/10**D
        if(ri<=0.0):
            print("Error, la semilla no es valida para generar {} numeros aleatorios".format(n+1))
            semilla_insuficiente()
            break
        r.append(ri)
        x0=xi

def digitos_centrales(s,k):
    # Para asegurar que el número no sea negativo usamos el max(tupla)
    m = max((len(s)-k)//2, 0) # El // es para que el resultado de la división sea entera
    return s[m:m+k]

def semilla_insuficiente():
    x0  = int(input("Inserta un valor de semilla sin demasiados ceros: "))
    validar(x0)

def imprimir():
    if(len(r)!=0):
        print("Los {} números pseudoaleatorios son: ".format(n+1))
    for idi, ri in enumerate(r):
        print("{} : {}".format(idi+1, ri))

def guardar():
    with open('cuadrados_medios.txt', 'w') as f:
        for num  in r:
            f.write(str(num)+'\n')

if __name__ == '__main__':
    D = int(input("Inserte la cantidad de D digitos: "))
    x0  = int(input("Inserta el valor semilla x0: "))
    n = int(input("¿Cuantos números pseudoaleatorios desea?: "))-1
    r = []
    validar(x0, D)
    imprimir()
    guardar()