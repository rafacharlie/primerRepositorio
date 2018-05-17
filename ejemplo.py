#-*- encoding: utf-8 -*-
#Escriba un PROGRAMA que pida dos números enteros y que calcule su división,
#escribiendo si la división es exacta o no.
#ya esta solucionado el problema
#resolucionado del todo
import os
print 'Escribe un numero entero: '
nNumero1=int(input())
print 'Escriba un segundo numero:'
nNumero2=int(input())
while nNumero2==0:
	print 'No se puede dividir por 0. Inserte otro numero mayor que 0:'
	nNumero2=int(input())
division=(nNumero1/nNumero2)
modulo=(nNumero1%nNumero2)
if modulo==0:
	print'La division es exacta. El resultado es : cociente= %s' % str(division)
else:
	print 'La division no es exacta. El resultado es : cociente= %s y el resto= %s' % (str(division),str(modulo))
os.system('pause')
