from cuadrado import cuadrado
from triangulo import triangulo
mi_cuadrado=cuadrado
mi_triangulo=triangulo
print("que quiere hacer?")
print("1.cuadrado, 2.triangulo,3.imprimir,4.calcular area 5.salir")
opc=5
opc=(int(input("ingrese un numero")))
if opc==1:
	print("cuadrado")
	numero=(int(input("ingrese un valor")))
	mi_cuadrado=cuadrado(numero)
if opc==2:
	print(triangulo)
	base=(int(input("ingrese un valor")))
	h=(int(input("ingrese un valor")))
	mi_triangulo=triangulo(base*altura)/2
