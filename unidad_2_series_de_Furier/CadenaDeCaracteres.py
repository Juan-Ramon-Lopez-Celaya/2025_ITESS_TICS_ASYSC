#Cadena de caracteres
#se imprimen las siguientes cadenas de caracteres.
print('huevos y pan')
print('doesn\'t')
print("doesn't")
print('"si," le dijo.')
print("\"si,\" le dijo.")
print('"Isn\'t." she said.' + "\n")

#la salida print() hace una salida mas limpia
s = 'Primera línea.\nSegunda línea.'
print(s + "\n")

#Los caracteres antes de \se desaparecen a menos que pongamos r antes.
print('C:\algun\nombre')
print(r'C:\algun\nombre' + "\n")

#estas 3 comillas nos dejan escribir varias lineas a la vez
print("""\
 Uso: algo [OPTIONS]
     -h                        Muestra el mensaje de uso
     -H nombrehost             Nombre del host al cual conectarse
 """)
 
#Cadenas de texto concatenadas (pegadas juntas) con el operador + y repetidas con *:
# 3 veces 'un', seguido de 'ium'
print("3 * 'un' + 'ium' = \n" + str(3 * 'un' + 'ium'))
#Dos cadenas o mas juntas(lado a lado) se concatenan automaticamente
print('py''thon')
#es util para unir cadenas largas
texto = ('Poné muchas cadenas dentro de paréntesis '
             'para que ellas sean unidas juntas.')
print(texto + "\n")

#depende de que tipo sea el número en la casilla, sera el caracter que regresara
palabra = "python"
print(palabra[0])
print(palabra[5])
print(palabra[-1])
print(palabra[-2])
print(palabra[-6] + "\n")

#la palabra tambien se puede dividir en rebanadas, de donde"[" hasta":" donde"]"
print(palabra[:2] + palabra[2:])
print(palabra[:4] + palabra[4:])#se suman las 2 rebanadas
print(palabra[:2])# caracteres desde el principio hasta la posición 2 (excluída)
print(palabra[4:])# caracterrs desde la posición 4 (incluída) hasta el final
print(palabra[-2:] + "\n")# caracteres desde la ante-última (incluída) hasta el final

#las rebanadas pueden manejar indices fuera del rango tal que este:
print(palabra[4:42])
print(palabra[42:])
#una cadena no puede ser modificada. ej: palabra[0] = 'J' ó palabra[2:] = 'py'
#se necesita crear una cadena diferente
print('J' + palabra[1:])
print(palabra[:2] + 'py' + "\n")

#para leer una nueva palabra se utiliza len()
s = 'supercalifrastilisticoespialidoso'
print(len(s))


