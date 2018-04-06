def main():
	counter = 0
	with open('cuadrados_medios.txt', 'r') as f:
		for line in f:
			cuadrados_medios.append(float(line.strip('\n')))

if __name__ == '__main__':
	cuadrados_medios = []
	congruencial_aditivo = []
	main()
	print(cuadrados_medios)