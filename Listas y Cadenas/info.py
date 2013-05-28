print "=========================================================================="
print "TRABAJANDO CON LISTAS"
print "=========================================================================="

#La lista es una colección de datos ordenada, alguna equivalencia con
#otros lenguajes seria los arrays o vectores.
#La lista puede contener cualquier tipo de dato (enteros, cadenas y otras
#listas ) veamos cómo se puede crear una lista:

#Utilizando un tipo de datos string, sería.

lista = ["hola","esto","es","python"]

#Para acceder a cada elemento, debemos utilizar un indice que nos muestre
#el elemento que indicamos a traves de corchetes "[]". Hay que tomar en
#cuenta que python toma como valor inicial el "0"

print (lista[0],"Mostramos el primer valor de la lista")
print (lista[1],"Mostramos el segundo valor de la lista")
print (lista[2],"Mostramos el tercer valor de la lista")
print (lista[3],"Mostramos el cuarto valor de la lista")
print ""
print "AQUI IMPRIMIMOS TODA LA LISTA"

#Si queremos rescatar toda la cadena
print (lista)

print ""

print "Tambien podemos crear listas con numeros enteros"

listaNumeros = ["1","2","3","4","5","6","7","8","9","0"]

print (listaNumeros[0])
print (listaNumeros[1])
print (listaNumeros[2])
print (listaNumeros[3])
print (listaNumeros[4])
print (listaNumeros[5])
print (listaNumeros[6])
print (listaNumeros[7])
print (listaNumeros[8])
print (listaNumeros[9])
print (listaNumeros)

print ""

#soporta numeros + y - para rescatar los elementos deseados. Veamos:)
print (listaNumeros[-1])
print (listaNumeros[-2])
print (listaNumeros[-3])
print (listaNumeros[-4])
print (listaNumeros[-5])
print (listaNumeros[-6])
print (listaNumeros[-7])
print (listaNumeros[-8])
print (listaNumeros[-9])
print (listaNumeros[-10])

print ""
print "RESCATANDO UN RANGO DE DATOS"

print (listaNumeros[0:5]);#Se toma valores desde el incio hasta el 5 elemento
print (listaNumeros[5:]);#Se inicia desde el valor 5 en adelante
print (listaNumeros[:5]);#Se inicia desde el primer valor hasta el 5

print ""

print "RESCATANDO UN RANGO DE DATOS PERO CON UN INTERVALO (inicio-fin-salto)"

#Utilizando siempre con listaNumeros

print (listaNumeros[0:10:2])#0=Inicio 10=fin 2=salto(intevalo)
print (listaNumeros[::2]);#Muestro todos los elementos con un salto de dos en dos

print ""
print "ANIDANDO LISTA DENTRO DE LISTA"

listas_anidadas = ([1,2,3,4,5],[6,7,8,9,10])
print listas_anidadas

print ""

print "USO DEL APPEND(OBJECT)"
print "Añadiendo un objeto al final de la lista digamos que tenemos:" 
lista=[1,2,3,4,5,6,7] 
lista.append(10)#Numero a agregar 
print(lista)

print ""

print "USO DEL COUNT(VALUE)"
listacontar=[2,4,6,8,10,10,8,6,4,2,4,6,8,10]
print listacontar.count(10)#Devuelve el numero de veces que se encontro 10

print ""
print "CONCATENAR DATOS A UNA LISTAS EXISTENTE"
lista.extend([11,12,13,14,15])#Valores a concatenar con "lista"
print (lista)

print ""
print "INSERTAR UN ELEMENTO EN UNA POSICION DENTRO DE UNA LISTA"
lista.insert(0,50)#0=posicion 50=elemento a ingresar
print (lista)

print ""
print "ELIMINAR UN ELEMENTO EN PARTICULAR"
print (lista)
lista.remove(50)#Numero a eliminar
print lista


print ""
print "INVERTIR LISTA"
print (lista)
lista.reverse()#Accion que invierte la lista
print lista

#Además de los números, Python también sabe manipular cadenas, que se pueden
#expresar de diversas maneras. Se pueden encerrar entre comillas simples o dobles.
print ""

print "=========================================================================="
print "TRABAJANDO CON CADENAS"
print "=========================================================================="

#Además de los números, Python también sabe manipular cadenas, que se pueden
#expresar de diversas maneras. Se pueden encerrar entre comillas simples o dobles:

# 'cadena'
# "Hospitalet"

#Las cadenas pueden ocupar varias líneas de diferentes maneras. Se puede impedir
#que el final de línea física se interprete como final de línea lógica usando una
#barra invertida al final de cada línea parcial:

hola = "Esto es un texto bastante largo que contiene\n\
varias líneas de texto, como si fuera C.\n\
    Observa que el espacio en blanco al principio de la línea es\
 significativo."
print hola

#Hay que observar que los saltos de línea se han de incrustar en la cadena con \n,
#pues el salto de línea físico se desecha. El ejemplo mostraría lo siguiente:

#Esto es un texto bastante largo que contiene
#varias líneas de texto, como si fuera C.
#    Observa que el espacio en blanco al principio de la línea es significativo.
#Sin embargo, si hacemos de la cadena una cadena ``en bruto'', las secuencias \n
#no se convierten en saltos de línea, sino que se incluyen tanto la barra invertida y
#el carácter de salto de línea del código fuente en la cadena como datos. Así, el ejemplo:

 
hola = r"Ésta es una cadena bastante larga que contiene\n\
varias líneas de texto de manera parecida a como se haría en C." 

print hola

 
#Ésta es una cadena bastante larga que contiene\n\ 
#varias líneas de texto de manera parecida a como se haría en C.
#O se pueden encerrar las cadenas entre comillas triples emparejadas: """ o '''.
#No es necesario poner barra invertida en los avances de línea cuando se utilizan
#comillas triples; se incluyen en la cadena.

print """
Uso: cosilla [OPCIONES] 
     -h                        Mostrar este mensaje de uso
     -H NombreServidor         Nombre del servidor al que conectarse
"""

#presenta:

#Uso: cosilla [OPCIONES] 
#     -h                        Mostrar este mensaje de uso
#     -H NombreServidor         Nombre del servidor al que conectarse

#Se puede concatenar cadenas (pegarlas) con el operador + y repetirlas con *:

palabra='Auda' + 'Z'
print palabra
print '<' + palabra*5 + '>'

#Dos literales juntos se concatenan automáticamente. La primera línea de
#arriba se podría haber escrito "palabra = 'Auda' 'Z'". Esto sólo funciona con literales, no con expresiones de cadena arbitrarias.

print ""
#DESDE El SHELL SERIA
#>>> import string 
#>>> 'cad' 'ena'                 
#'cadena'
#>>> 'cad'.strip() + 'ena'   
#'cadena'

print ""
print "DESDE El MODULE SERIA"
cadena1 = 'Cad'
cadena2 = 'ena'
print cadena1 + cadena2

#Se puede indexar una cadena. Como en C, el primer carácter de una cadena
#tiene el índice 0. No hay un tipo carácter diferente; un carácter es una
#cadena de longitud uno: dos índices separados por dos puntos.
print ""
#ejemplo
texto1 = "Dios es FIEL"
texto2 = " y Justo"
print texto1[0]   #solo imprime la primera letra
print texto1[0:7] #imprime un rango entre 0 a 7 caracteres
print texto1[0:]  #imprime desde el caracter 0 en adelante
print texto1[:4]  #imprime desde el caracter 0 hasta el caracter 4

print ""
print "CONCATENANDO LOS DOS TEXTOS(CADENAS) UTILZANDO RANGOS"
print texto1[0:] + texto2[0:]
print ""

print "AGREGANDO UNA NUEVA CADENA A UNA CADENA EXISTENTE"
print 'La Biblia dice que: ' + texto1[0:]








