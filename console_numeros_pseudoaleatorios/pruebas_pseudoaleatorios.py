def main():
	with open(files[name], 'r') as f:
		for line in f:
			r.append(float(line.strip('\n')))
		if len(r) < 10:
			print("Necesitamos más de 10 números para continuar")
			exit()
		p_medias = medias(r)
		print(p_medias)
		p_varianza = varianza(r)
		print(p_varianza)
		chi_cuadrada(r)
		"""kolmogorov(r)
		corridas_arriba_y_abajo(r)
		corridas_arriba_y_abajo_de_la_media(r)
		poker(r)
		series(r)
		huecos(r)"""

def mean(r):
	sum_r = 0
	for num in r:
		sum_r += num

	promedio = sum_r/len(r)
	return promedio

def medias(r):
	promedio = mean(r)
	print("__________El resultado de la prueba de medias: {0:.4f}__________".format(promedio))
	LI = 0.5-(1.96*(1/(12*len(r))**(0.5)))
	LS = 0.5+(1.96*(1/(12*len(r))**(0.5)))
	if (promedio>LI)&(promedio<LS):
		print("Aceptamos la hipótesis Nula")
		print("Limites de aceptación: {0:.4f} y {1:.4f}".format(LI,LS))
		print("________________________________________________________________")
		return True
	else:
		print("Rechazamos la hipótesis Nula porque está afuera de los limites de aceptación")
		print("Limites de aceptación: {0:.4f} y {1:.4f}".format(LI,LS))
		print("________________________________________________________________")
		return False

def varianza(r):
	promedio = mean(r)
	varianza = 0
	for num in r:
		varianza += ((num - promedio)**2)/(len(r)-1)

	print("__________El resultado de la prueba de medias: {0:.4f}__________".format(varianza))
	LS = (tabla[len(r)-20])/((12)*(len(r)-1))
	LI = (tabla_b[len(r)-20])/((12)*(len(r)-1))

	if (varianza<LS) & (varianza>LI):
		print("Aceptamos la hipótesis nula")
		print("Limites de aceptación: {0:.4f} y {1:.4f}".format(LI,LS))
		print("________________________________________________________________")
		return True
	else:
		print("Rechazamos la hipótesis Nula porque está afuera de los limites de aceptación")
		print("Limites de aceptación: {0:.4f} y {1:.4f}".format(LI,LS))
		print("________________________________________________________________")
		return False

def chi_cuadrada(r):
	m = (len(r))**0.5
	if m%1 != 0:
		m = int(m)+1

	print(m)

	observadas = []

	for salto in range(m):
		observadas.append(0)

	print(observadas)

	limites = []

	for salto in range(m):
		limites.append(round(((salto+1)/m),3))

	print(limites)

	for num in r:
		for limite in limites:
			if num < limite:
				observadas[limites.index(limite)] += 1

	print(observadas)


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
	tabla = [32.8523, 34.1696, 35.4789, 36.7807, 38.0756, 39.3641, 40.6465, 41.9231,
			 43.1945, 44.4608, 45.7223, 46.9792, 48.2319, 49.4804, 50.7251, 51.9660,
			 53.2033, 54.4373, 55.6680, 56.8955, 58.1201]

	tabla_b = [ ((19.1069+18.3376)/2),((20.1272+19.3374)/2),((21.1470+20.3372)/2),
				((22.1663+21.3370)/2),((23.1852+22.3369)/2),((24.2036+23.3367)/2),
				((25.2218+24.3366)/2),((26.2395+25.3365)/2),((27.2569+26.3363)/2),
				((28.2740+27.3362)/2),((29.2908+28.3361)/2),((30.3073+29.3360)/2),
				((31.3235+30.3359)/2),((32.3394+31.3359)/2),((33.3551+32.3358)/2),
				((34.3706+33.3357)/2),((35.3858+34.3356)/2),((36.4008+35.3356)/2),
				((37.4156+36.3355)/2),((38.4302+37.3354)/2),((39.4446+38.3354)/2)]

	main()
	print("Los datos con los que se trabajo fueron {} ".format(r))