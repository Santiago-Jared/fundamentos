"""
Programa que calcule el área y el perimetro 
de un rectangulo a partir de su base y su altura
Entradas:
     basse: integer
     altura: integer
Salidas:
    perimetro: integer
    área: integer     
Analisis:
    Se requiere clacular con las frormulas para
    área y perimetro
"""
# input siempre regresa un string
# para tratarlo como otro dato se debe convertir
base = input("Escribe la base del rectángulo: ")
base = int(base)
altura = input("Escribe la altura del rectángulo: ")
altura = int(altura)
area = base * altura
perimetro = (base + altura) *  2
print("El area del rectangulo es ", area)
print("El perimetro del rectangulo es ", perimetro)
‎Ejercicio3.py
+18
Original file line number	Diff line number	Diff line change
@@ -0,0 +1,18 @@
'''
Ejercicio 3 
  Programa que calcula la hipotenusa a partir de los dos catetos ç
Entradas:
   CatetoA: int - a
   CatetoB: int - b
Salidas:
   hipotenusa: float - c
Análisis:
   Se utiliza el teorema de Pitágoras
'''
a = input ("Escribe el valor de cateto A: ")
a = int (a)
b = input ("Escribe el valor del cateto B: ")
b = int (b)
c = (a * a + b * b) ** (1 / 2)
print("El valor de a hipotenusa: ", c)
