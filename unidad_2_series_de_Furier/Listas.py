#Listas y sus tipos
#Las listas pueden contener items de difrentes tipos, pero generalmente usan items del mismo tipo
print("cuadrados = [1, 4, 9, 16, 25]")
cuadrados = [1, 4, 9, 16, 25]
print(cuadrados)
#las listas tambien pueden ser indexadas y rebanadas
print(cuadrados[0]) # retorna un item
print(cuadrados[-1])
print(cuadrados[-3:])#retorna una lista nueva(con los numeros ya puestos)

#el siguiente pedido de esta rebanada devuelve una copia superficial de la lista
print(cuadrados[:])

#las listas tambien se pueden concatenar
print(cuadrados + [36, 49, 64, 81, 100])
print("\n")

#las lista a diferencia de las cadenas de texto si pueden ser mutables(cambiar su contenido)
cubos = [1, 8, 27, 65, 125]
print("cubos = [1, 8, 27, 65, 125]")
print(" hay algo mal aquí")
print("4**3 = " + str(4**3 ) + ", el cubo de 4 es 64 no 65!")
cubos[3] = 64 #remplazamos el valor incorrecto
print(cubos)

#se pueden agregar nuevos items al final de la lista usando el metodo append()
print("agregamos cubo de 6 y 7")
cubos.append(216) #agregamos el cubo de 6
cubos.append(7**3) #agregamos el cubo de 7
print(cubos)
print("\n")

#tambien es posible asignar a una rebanada, y esto incluso puede cambiar la longitud de la lista o vaciarla totalmente:
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print("letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g']")
print(letras)
# reemplazar algunos valores
letras[2:5] = ['C', 'D', 'E']
print(letras)
#ahora borramos las que agregamos
letras[2:5] = []
print("letras[2:5] = []")
print(letras)
#borramos la lista completa con una lista vacia
letras[:] = []
print("letras[:] = []")
print(letras)
print("\n")

#la funcion len() tambien lee listas
letras = ['a', 'b', 'c', 'd']
print("letras = ['a', 'b', 'c', 'd']")
print(len(letras))
print("\n")
#es posible anidar listas(listas que tengan otras listas)
a = ['a', 'b', 'c']
n = [1,2,3]
x = [a,n]
print(x)
print(x[0])
print(x[0][1] + "\n")

#serie fibonacci pequeña (la suma de dos elementos define el siguiente)
print("serie pequeña fibonacci")
a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a+b
print("\n")

i = 256*256
print('El valor de i es ', i)
print("\n")

#el paramatro end puede usarse para evitar el salto de linea al final de la salida
# o terminar la salida con una cadena diferente  
a, b = 0, 1
while b < 1000:
    print(b, end = '.')
    a, b = b, a+b
print("\n")
