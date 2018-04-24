def main():
	with open(files[name], 'r') as f:
		for line in f:
			r.append(float(line.strip('\n')))
		medias(r)
		"""varianza(r)
		chi_cuadrada(r)
		kolmogorov(r)
		corridas_arriba_y_abajo(r)
		corridas_arriba_y_abajo_de_la_media(r)
		poker(r)
		series(r)
		huecos(r)"""

def medias(r):
	sum_r = 0
	for num in r:
		sum_r += num

	promedio = sum_r/len(r)
	print("El resultado de la prueba de medias: {}".format(promedio))
	LI = 0.5-(1.96*(1/(12*len(r))**(0.5)))
	LS = 0.5+(1.96*(1/(12*len(r))**(0.5)))
	print(LI,LS)

if __name__ == '__main__':
	files = ['congruencial_aditivo.txt',
			'congruencial_cuadratico.txt',
			'congruencial_multiplicativo.txt',
			'cuadrados_medios.txt',
			'lineal.txt',
			'multiplicador_constante.txt',
			'producto_de_medios.txt'
	]
	name = int(input("Ingrese el número del archivo que desea revisar: "+
					"\n 1. congruencial_aditivo"+
					"\n 2. congruencial_cuadratico"+
					"\n 3. congruencial_multiplicativo"+
					"\n 4. cuadrados_medios"+
					"\n 5. lineal"+
					"\n 6. multiplicador_constante"+
					"\n 7. producto_de_medios"+
					"\n Número: "))-1
	r = []
	main()
	print(r)