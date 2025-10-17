#control de flujo
#La sentencia if, nos dice a donde pertenece segun el tamaño del nuemero que pongamos
print("Ingresamos el 42 como ejemplo")
x = int(input("Ingresa un entero, por favor: "))


if x < 0:
    x = 0
    print('Negativo cambiado a cero')
elif x == 0:
        print('Cero')
elif x == 1:
        print('Simple')
else:
        print('Mas' + "\n")

#La Sentencia For
#Midiendo cadenas de texto, vemos cuantas letras tiene cada palabra
palabras = ['gato', 'ventana', 'defenestrado']
for p in palabras:
    print(p, len(p))
print("\n")

#si necesitas modificar la secuencia sobre la que estas escribiendo 
# dentro de un ciclo for se recomienda hacer una copia    
for p in palabras[:]:# hace una copia por rebanada de toda la lista
    if len(p) > 6:
        palabras.insert(0, p)
print(palabras)
print("\n")

#La funcion range() nos dice el rango de un punto a otro
for i in range (5):
    print(i)
 
for i in range(5, 10):
    print(i, end=',')
print("\n")
    
for i in range(0, 10, 3):
    print(i, end=',')
print("\n")
    
for i in range(-10, -100, -30):
    print(i, end=',')
print("\n")

# puedes combinar range() y len() así:
a = ['Mary', 'tenia', 'un', 'corderito']
for i in range(len(a)):
    print(i, a[i])
print("\n")

print (range(10))
print("\n")
print(list(range(5)))
print("\n")

#Las sentencias break, continue, y else en lazos
for n in range(2, 10):
     for x in range(2, n):
         if n % x == 0:
             print(n, 'es igual a', x, '*', n//x)
             #se le pone doble // para que de numeros enteros
             break
     else:
         # sigue el bucle sin encontrar un factor
         print(n, 'es un numero primo')
print("\n")

#La Sentencia Continue
for num in range(2, 10):
     if num % 2 == 0:
         print("Encontré un número par", num)
         continue
     print("Encontré un número", num)
print("\n")


#Definiendo funciones
# escribe la serie de Fibonacci hasta un limite
def fib(n): 
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()
print(fib(2000)) # escribe la serie de Fibonacci hasta n

f = fib
print(f(100))

#Valores por omision
#def pedir_confirmacion(prompt, reintentos=4, queja='Si o no, por favor!'):
    #while True:
        #ok = input(prompt)
        #if ok in ('s', 'S', 'si', 'Si', 'SI'):
            #return True
        #if ok in ('n', 'no', 'No', 'NO'):
            #return False
        #reintentos = reintentos - 1
        #if reintentos < 0:
            #raise OSError('usuario duro')
        #print(queja)
        
#En este programa omite un valor ya declarado

print("\n")
i = 5

def f(arg=i):
    print(arg)
i = 6
f()
print("\n")

def f(a, L=[]):
    L.append(a)
    return L
print(f(1))
print(f(2))
print(f(3))
print("\n")


def loro(tension, estado='muerto', accion='explotar', tipo='Azul Nordico'):
    print("-- Este loro no va a", accion, end=' ')
    print("si le aplicás", tension, "voltios.")
    print("-- Gran plumaje tiene el", tipo)
    print("-- Está", estado, "!")
loro(1000)                                          # 1 argumento posicional
loro(tension=1000)                                  # 1 argumento nombrado
loro(tension=1000000, accion='VOOOOOM')             # 2 argumentos nombrados
loro(accion='VOOOOOM', tension=1000000)             # 2 argumentos nombrados
loro('un millón', 'despojado de vida', 'saltar')    # 3 args posicionales
loro('mil', estado = 'viendo crecer las flores desde abajo')  # uno y uno


#listas de argumentos
#este concatena distintas variables y separa con el comando sep="algo"
def concatenar(*args, sep="/"):
    return sep.join(args)

concatenar("tierra", "marte", "venus")

concatenar("tierra", "marte", "venus", sep=".")

#Desempaquetado de una lista
list(range(3, 6))   # llamada normal con argumentos separados
[3, 4, 5]
args = [3, 6]
list(range(*args))  # llamada con argumentos desempaquetados de la lista


#expresion lambda, este nos ayuda a incrementar 
def hacer_incrementador(n):
    return lambda x: x + n

f = hacer_incrementador(42)
print(f(0))
 
print(f(1))

#anotaciones, con este codigo se pueden crear anotaciones dentro del codigo para imprimir{
def f(jamon: 42, huevos: int = 'carne'): #  -> "nada nada":
    print("Anotaciones:", f.__annotations__)
    print("Argumentos:", jamon, huevos)

print(f('maravillosa'))