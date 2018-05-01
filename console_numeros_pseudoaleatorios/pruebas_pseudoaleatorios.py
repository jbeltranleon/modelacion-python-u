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
		p_chi_cuadrada = chi_cuadrada(r)
		p_arriba_abajo = arriba_abajo(r)
		print(p_chi_cuadrada)
		p_kolmogorov = kolmogorov(r)
		print(p_kolmogorov)
		p_poker = poker(r)
		print(p_poker)
		"""corridas_arriba_y_abajo_de_la_media(r)
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
	print("**********El resultado de la prueba de medias: {0:.4f}**********".format(promedio))
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

	print("**********El resultado de la prueba de medias: {0:.4f}**********".format(varianza))
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
	else:
		m = int(m)

	observadas = []

	print("Este m da problemas {}".format(m))

	for salto in range(m):
		observadas.append(0)

	limites = []
	for salto in range(m):
		limites.append(round(((salto+1)/m),3))

	for num in r:
		for limite in limites:
			if num < limite:
				observadas[limites.index(limite)] += 1

	esperada = len(r)/m

	chi = []

	for observada in observadas:
		chi.append(((esperada-observada)**2)/esperada)

	sum_chi = 0
	for val in chi:
		sum_chi += val

	valor_en_tablas = tabla_c[m-2]

	print("*******El resultado de la prueba de chi cuadrada: {0:.4f}*******".format(sum_chi))

	if sum_chi < valor_en_tablas:
		print("Aceptamos la hipótesis nula")
		print("Valor obtenido: {0:.4f} Valor en tablas {1:.4f}".format(sum_chi,valor_en_tablas))
		print("________________________________________________________________")
		return True
	else:
		print("Rechazamos la hipótesis Nula porque está afuera de los limites de aceptación")
		print("Valor obtenido: {0:.4f} Valor en tablas {1:.4f}".format(sum_chi,valor_en_tablas))
		print("________________________________________________________________")
		return False

def arriba_abajo(r):
	s = []
	for num in r:
		if r.index(num) != 0:
			anterior = r[r.index(num)-1]
			if num <= anterior:
				s.append(0)
			else:
				s.append(1)

	corrida = 1

	for i in range(len(s)):
		if i != 0:
			anterior = s[i - 1]
			actual = s[i]
			if actual != anterior:
				corrida += 1
	longitud = len(s)
	print('---*---*---*---*---*---*---*---*---')
	print("la lista de numeros es: {}\nla cantidad de corridas es: {}\nel tamaño del vector es: {}".format(s,corrida,longitud))
	print('---*---*---*---*---*---*---*---*---')

def kolmogorov(r):
	if len(r) > 20:
		return "LA PRUEBA KOLMOGOROV NO SE PUEDE REALIZAR EN CONJUNTOS MAYORES A 20"
	else:
		r_ordenada = sorted(r)

	prev_d_mas = []
	prev_d_menos = []

	for num in r_ordenada:
		prev_d_mas.append(((r_ordenada.index(num)+1)/len(r_ordenada))-num)
		prev_d_menos.append(num-((r_ordenada.index(num)+1)/len(r_ordenada)))

	d_mas = max(prev_d_mas)
	d_menos = max(prev_d_menos)
	d = max(d_mas,d_menos)

	print("*******El resultado de la prueba de Kolmogorov: {0:.4f}*******".format(d))

	valor_critico = tabla_kolmogorov[len(r)-10]
	print(valor_critico)

	if d > valor_critico:
		print("Los números no siguen una distribución uniforme")
		print("Valor obtenido: {0:.4f} Valor en tablas {1:.4f}".format(d,valor_critico))
		print("________________________________________________________________")
		return False
	else:
		print("no se ha detectado diferencia significativa entre la distribución de los r y la distribución uniforme.")
		print("Valor obtenido: {0:.4f} Valor en tablas {1:.4f}".format(d,valor_critico))
		print("________________________________________________________________")
		return True

def poker(r):
	flops = []
	for num in r:
		hand = str(num)[2:7]
		for i in range(5-(len(hand))):	
			hand += '0'

		flops.append(hand)

	quintilla = 0
	poker = 0
	combinaciones = []
	diferentes = []
	trio = 0
	par = 0
	trio_y_par = 0
	doble_par = 0
	diferente = 0

	for flop in flops:
		seen_numbers = {}
		for i, number in enumerate(flop):
			if number not in seen_numbers:
				seen_numbers[number] = 1
			else:
				seen_numbers[number] += 1

		#print(seen_numbers)
		combinaciones = []
		diferentes = []
		for value in seen_numbers.values():
			if value == 5:
				quintilla += 1
				#print('Quintilla {}'.format(quintilla))
			elif value == 4:
				poker += 1
				#print('Poker {}'.format(poker))
			elif value == 3:
				combinaciones.append('trio')
			elif value == 2:
				combinaciones.append('par')
			else:
				diferentes.append('diferente')

		if len(diferentes) == 5:
			diferente +=1
			#print('Todos diferentes {}'.format(diferente))

		if len(combinaciones) == 1:
			if 'trio' in combinaciones:
				trio += 1
				#print('Trio {}'.format(trio))
			else:
				par += 1
				#print('Par {}'.format(par))
		else:
			if ('trio' in combinaciones) & ('par' in combinaciones):
				trio_y_par += 1
				#print('Trio y par {}'.format(trio_y_par))
			elif('par' in combinaciones):
				doble_par += 1
				#print('Doble par {}'.format(doble_par))

	#print(flops)

	TD =       (((0.3024*len(flops))-diferente) **2) / (0.3024*len(flops))
	PAR =      (((0.5040*len(flops))-par)       **2) / (0.5040*len(flops))
	DOBLEPAR = (((0.1080*len(flops))-doble_par) **2) / (0.1080*len(flops))
	TP =       (((0.0090*len(flops))-trio_y_par)**2) / (0.0090*len(flops))
	T =        (((0.0720*len(flops))-trio)      **2) / (0.0720*len(flops))
	P =        (((0.0045*len(flops))-poker)     **2) / (0.0045*len(flops))
	Q =        (((0.0001*len(flops))-quintilla) **2) / (0.0001*len(flops))

	valor_obtenido = TD+PAR+DOBLEPAR+TP+T+P+Q
	valor_esperado = tabla_c[5]

	print("*******El resultado de la prueba de Poker: {0:.4f}*******".format(valor_obtenido))
	print('Quintilla {}'.format(quintilla))
	print('Poker {}'.format(poker))
	print('Trio {}'.format(trio))
	print('Par {}'.format(par))
	print('Todos diferentes {}'.format(diferente))
	print('Trio y par {}'.format(trio_y_par))
	print('Doble par {}'.format(doble_par))
	print('Flops: {}'.format(len(flops)))

	if valor_obtenido < valor_esperado:
		print("No se puede rechazar la independencia de los números del conjunto")
		print("Valor obtenido: {0:.4f} Valor en tablas {1:.4f}".format(valor_obtenido,valor_esperado))
		print("________________________________________________________________")
		return True
	else:
		print("La independencia de los números del conjunto se rechaza")
		print("Valor obtenido: {0:.4f} Valor en tablas {1:.4f}".format(valor_obtenido,valor_esperado))
		print("________________________________________________________________")
		return False
		

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

	tabla_c = [3.8415,5.9915,7.8147,9.4877,11.0705,12.5916,14.0671,15.5073,16.9190,18.3070]

	tabla_kolmogorov = [0.40925, 0.39122, 0.37543, 0.36143, 0.34890,
						0.33760, 0.32733, 0.31796, 0.30936, 0.30143, 0.29408]

	main()
	print("Los datos con los que se trabajo fueron {} ".format(r))

