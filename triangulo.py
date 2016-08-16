from figura import Figurageometrica
class Triangulo(Figurageometrica):
	def __init__ (self,altura):
		super(). __init__ (altura,base)
	def imprimir (self):
		resultado = " "
		for i in range (self, altura):
			resultado+="*"*(i+1)+"\n"
			print (resultado)