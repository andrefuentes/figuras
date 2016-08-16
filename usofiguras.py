from cuadrado import Cuadrado
from triangulo import Triangulo

opc=0
while opc!=2:
	opc=int(input("1.crear figura,2.salir: "))

	if opc==1:
		opc=int(input("1.cuadrado,2.triangulo,3.ambas: "))

	if opc==1:
		print("cuadrado")
		numero=(int(input("ingrese un valor")))

		mi_figura=Cuadrado(numero)
		print(mi_figura.calcular_area)
	if opc==2:

		base=(int(input("ingrese un valor")))
		h=(int(input("ingrese un valor")))
		mi_figura=Triangulo(base*altura)/2
		print(mi_figura.calcular_area())


		print ("area",mi_figura.calcularar_area())
		print (mi_figura.imprimir())
		