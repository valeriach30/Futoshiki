from tkinter import *
from tkinter import messagebox
import pickle  		
import webbrowser as wb
from tkinter.font import BOLD
import random


global valor
valor = 0


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# grabar las listas de partidas en un archivo
f = open("futoshiki2020partidasfaciles.dat", "wb")   # abrir achivo para grabar datos
lista_partidas_faciles = [
((">", 0, 0), (">", 0, 2), (">", 0, 3), ("4", 1, 0), ("2", 1, 4),
("4", 2, 2), ("<", 3, 3), ("4", 3, 4), ("<", 4, 0), ("<", 4, 1)) , (("<", 0,0), ("<", 0, 3),
("4", 0, 4), ("<", 1, 3), ("2", 1,  4), ("^", 1, 2), ("<", 2, 3),  ("^", 2, 2), (">", 3, 0),
("^", 3, 4)), (( "v", 0, 0), ("<", 1, 1), ("<", 1, 2), ("5", 2, 0), ("<", 3, 1), ("^", 2,3),
("1", 3, 4), ("3", 4, 1),("1", 4, 2))
]

# grabar lista partidas fáciles
pickle.dump(lista_partidas_faciles ,f)

# Cerrar archivo
f.close()


f2 = open("futoshiki2020partidasintermedias.dat","wb") 
lista_partidas_intermedias = [
((">", 0, 0), ("2", 1, 2), ("^", 1, 0), ("v", 1,1), ("^", 2,3), ("v", 3, 4), ("4", 4,0), ("2", 4, 1),
("1", 4,3)), ((">", 0, 0), (">", 0, 2),  ("5", 0, 4), ("v", 1, 3), ("2", 2, 1), ("v", 2, 1), ("v", 2, 2),
("^", 2, 4), ("v", 3, 3), ("^", 3, 4)), (("1", 0, 0), ("^", 0, 4), ("<", 1, 0), ("^", 1, 3), ("^", 1, 4),
("<", 2, 0), ("^", 3, 3), ("4", 4, 4))
]

# grabar lista partidas intermedias	
pickle.dump(lista_partidas_intermedias,f2)

# Cerrar archivo
f2.close()


f3 = open("futoshiki2020partidasdificiles.dat","wb") 
lista_partidas_dificiles = [
((">", 0 ,0), ("1", 0, 2), (">", 1, 2), (">", 1, 3), ("v", 2,2), ("4", 3, 3), ("5", 4, 0),
("4", 4, 2),("2", 4, 3), ("<", 4, 3)),  (("<", 0, 0), ("4", 0, 3), (">", 0, 3), ("v", 0, 4),
(">", 1, 2), (">" ,2,0), (">", 2, 1), ("^", 2, 3), (">", 4, 0), ("2", 4, 3), (">", 4, 3)),
(("v", 0, 4), ("<", 1, 0), ("<", 1, 1), ("^", 1, 4), ("<", 2, 1), ("2", 2, 3), ("^", 2, 4),
("<", 3, 0),("^", 3, 2), (">", 4, 0), ("3", 4,4))
]

# grabar lista partidas difíciles
pickle.dump(lista_partidas_dificiles,f3)	        

# cerrar achivo
f3.close()


# Se crea el archivo del top 10
top10 = open("futoshiki2020top10.dat","wb")

top_10_facil = [("Isa", "00:00:10"), ("Esteban", "00:06:30"), ("Lucia", "00:08:30"),

            ("Juan Diego", "00:08:40"), ("Mariana", "00:09:30"), ("Julie", "00:10:15"),

            ("Jose", "00:11:30"), ("Valeria", "00:12:05"), ("Juan", "00:13:30"),

            ("Ema", "00:14:00"), ]


top_10_intermedio = [("Samantha", "00:00:30"), ("Esteban", "00:42:30"), ("Sergio", "00:50:40"),

            ("Juan Diego", "00:58:10"), ("Gloriana", "01:01:30"), ("Julie", "01:05:15"),

            ("Jose", "01:09:30"), ("Valeria", "01:10:05"), ("Jimena", "01:13:30"),

            ("Fiorella", "01:14:00"), ]

top_10_dificil = [("Diego", "00:00:15"), ("Alejandro", "01:16:30"), ("Armando", "01:18:40"),

            ("Nicole", "01:20:10"), ("Josue", "01:21:30"), ("Maria", "01:25:45"),

            ("Hilary", "01:28:30")]

pickle.dump(top_10_facil, top10)
pickle.dump(top_10_intermedio, top10)
pickle.dump(top_10_dificil, top10)

top10.close()

#-----------------------------------------------------------------------------------------------------------------------


# Funcion que devuelve los tiempos en segundos del top 10 del momento
def crea_tiempos():

    # Se abre el archivo
    top10 = open("futoshiki2020top10.dat","rb")

    top_10_facil = pickle.load(top10)
    top_10_intermedio = pickle.load(top10)
    top_10_dificil = pickle.load(top10)


    global tiempos_facil
    tiempos_facil = []

    for i in range(len(top_10_facil)):

        # Se obtiene el tiempo
        s_tiempo = top_10_facil[i][1]

        # Se divide el tiempo en partes y se transforma todo a segundos
        horas = int(s_tiempo[0:2]) * 3600
        minutos = int(s_tiempo[3:5]) * 60
        segundos = int(s_tiempo[6:8])

        tiempo_total = horas + minutos + segundos

        # Se agrega a la lista
        tiempos_facil += [(top_10_facil[i][0], tiempo_total)]

    global tiempos_intermedio
    tiempos_intermedio = []

    for i in range(len(top_10_intermedio)):

        # Se obtiene el tiempo
        s_tiempo = top_10_intermedio[i][1]

        # Se divide el tiempo en partes y se transforma todo a segundos
        horas = int(s_tiempo[0:2]) * 3600
        minutos = int(s_tiempo[3:5]) * 60
        segundos = int(s_tiempo[6:8])

        tiempo_total = horas + minutos + segundos

        # Se agrega a la lista
        tiempos_intermedio += [(top_10_intermedio[i][0], tiempo_total)]

    global tiempos_dificil
    tiempos_dificil = []

    for i in range(len(top_10_dificil)):

        # Se obtiene el tiempo
        s_tiempo = top_10_dificil[i][1]

        # Se divide el tiempo en partes y se transforma todo a segundos
        horas = int(s_tiempo[0:2]) * 3600
        minutos = int(s_tiempo[3:5]) * 60
        segundos = int(s_tiempo[6:8])

        tiempo_total = horas + minutos + segundos

        # Se agrega a la lista
        tiempos_dificil += [(top_10_dificil[i][0], tiempo_total)]

    # Se cierra el archivo
    top10.close()


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

juego_iniciado = False
entro_configurar = False 
global numero_boton
numero_boton = []
terminado = False
tiempo_final = "00:00:00"

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Se crea una funcion para que el boton cambie de color mientras
# este presionado
def btnpress(n):

    global valor
    
    # Llamar funcion para resetear
    # Entonces cada vez que entre va a
    # colocar los colores originales
    resetbtn()
    
    if n == 1:
        boton1.config(bg="pale green")
        valor = "1"
    elif n == 2:
        boton2.config(bg="pale green")
        valor = "2"
    elif n == 3:
        boton3.config(bg="pale green")
        valor = "3"
    elif n == 4:
        boton4.config(bg="pale green")
        valor = "4"
    elif n == 5:
        boton5.config(bg="pale green")
        valor = "5"

          

def resetbtn():
    # Resetea el color de los botones
    boton1.config(bg="white")
    boton2.config(bg="white")
    boton3.config(bg="white")
    boton4.config(bg="white")
    boton5.config(bg="white")

#-----------------------------------------------------------------------------------------------------------------------

# Funcion que determina las coordenas segun el indice del boton
def f_coordenadas(indice):

    if indice == 0:
        return (0,0)

    if indice == 1:
        return (0,1)

    if indice == 2:
        return (0,2)

    if indice == 3:
        return (0,3)

    if indice == 4:
        return (0,4)

    if indice == 5:
        return (1,0)

    if indice == 6:
        return (1,1)

    if indice == 7:
        return (1,2)

    if indice == 8:
        return (1,3)

    if indice == 9:
        return (1,4)

    if indice == 10:
        return (2,0)

    if indice == 11:
        return (2,1)
    
    if indice == 12:
        return (2,2)

    if indice == 13:
        return (2,3)

    if indice == 14:
        return (2,4)

    if indice == 15:
        return (3,0)
    
    if indice == 16:
        return (3,1)
    
    if indice == 17:
        return (3,2)

    if indice == 18:
        return (3,3)

    if indice == 19:
        return (3,4)

    if indice == 20:
        return (4,0)

    if indice == 21:
        return (4,1)

    if indice == 22:
        return (4,2)

    if indice == 23:
        return (4,3)

    if indice == 24:
        return (4,4)

#-----------------------------------------------------------------------------------------------------------------------

# Funcion que determina el indice segun las coordenadas en que se encuentra
def f_indice(pos):
    

    if pos == (0,0):
        return 0

    if pos == (0,1):
        return 1

    if pos == (0,2):
        return 2

    if pos == (0,3):
        return 3

    if pos == (0,4):
        return 4

    if pos == (1,0):
        return 5

    if pos == (1,1):
        return 6

    if pos == (1,2):
        return 7

    if pos == (1,3):
        return 8

    if pos == (1,4):
        return 9

    if pos == (2,0):
        return 10

    if pos == (2,1):
        return 11
    
    if pos == (2,2):
        return 12

    if pos == (2,3):
        return 13

    if pos == (2,4):
        return 14

    if pos == (3,0):
        return 15
    
    if pos == (3,1):
        return 16
    
    if pos == (3,2):
        return 17

    if pos == (3,3):
        return 18

    if pos == (3,4):
        return 19

    if pos == (4,0):
        return 20

    if pos == (4,1):
        return 21

    if pos == (4,2):
        return 22

    if pos == (4,3):
        return 23

    if pos == (4,4):
        return 24

#-----------------------------------------------------------------------------------------------------------------------

# Funcion que retorna una lista con las restricciones
# y con el boton que las tiene que cumplir 

def list_restriccion(indice, level):

    global lista_rest_2

    if level == 1:
        
        f = open("futoshiki2020partidasfaciles.dat", "rb")    

        lista_partidas_faciles = pickle.load(f)

        # Se forma una lista
        lista_restricciones = []
        
        # Lista para las restricciones
        lista_rest_2 = []
        
        for j in lista_partidas_faciles[indice]:
            
            if j[0] == "<" or j[0] == ">" or\
               j[0] == "^" or j[0] == "v":

                # Se determina la posicion
                pos = j[1], j[2]
                # Se determina a cual boton pertenece a esa posicion
                boton_restriccion = f_indice(pos)

                # Se agrega la restriccion a la lista
                lista_restricciones += [(j[0], boton_restriccion)]

                # Se agrega el boton que esta junto a ese restriccion

                if j[0] == "<" or j[0] == ">":
                    
                    lista_rest_2 += [(j[0], boton_restriccion + 1)]

                if j[0] == "^" or j[0] == "v":

                    lista_rest_2 += [(j[0], boton_restriccion + 5)]

        return lista_restricciones
        
        f.close()


    if level == 2:

        f2 = open("futoshiki2020partidasintermedias.dat","rb")
        
        lista_partidas_intermedias = pickle.load(f2)

        # Se forma una lista
        lista_restricciones = []

        # Lista para las restriccion
        lista_rest_2 = []

        for j in lista_partidas_intermedias[indice]:
            
            if j[0] == "<" or j[0] == ">" or\
               j[0] == "^" or j[0] == "v":

                # Se determina la posicion
                pos = j[1], j[2]

                # Se determina a cual boton pertenece a esa posicion
                boton_restriccion = f_indice(pos)

                # Se agrega la restriccion a la lista
                lista_restricciones += [(j[0], boton_restriccion)]

                # Se agrega el boton que esta junto a ese restriccion

                if j[0] == "<" or j[0] == ">":
                    
                    lista_rest_2 += [(j[0], boton_restriccion + 1)]

                if j[0] == "^" or j[0] == "v":

                    lista_rest_2 += [(j[0], boton_restriccion + 5)]

        return lista_restricciones

        f2.close()

    if level == 3:

        f3 = open("futoshiki2020partidasdificiles.dat","rb")
        
        lista_partidas_dificiles = pickle.load(f3)

        # Se forma una lista
        lista_restricciones = []

        # Lista para las restricciones
        lista_rest_2 = []

        for j in lista_partidas_dificiles[indice]:
            
            if j[0] == "<" or j[0] == ">" or\
               j[0] == "^" or j[0] == "v":

                # Se determina la posicion
                pos = j[1], j[2]

                # Se determina a cual boton pertenece a esa posicion
                boton_restriccion = f_indice(pos)

                # Se agrega la restriccion a la lista
                lista_restricciones += [(j[0], boton_restriccion)]

                if j[0] == "<" or j[0] == ">":
                    
                    lista_rest_2 += [(j[0], boton_restriccion + 1)]

                if j[0] == "^" or j[0] == "v":

                    lista_rest_2 += [(j[0], boton_restriccion + 5)]



        return lista_restricciones

#-----------------------------------------------------------------------------------------------------------------------
def valores_botones(boton, board):

    coordenadas = f_coordenadas(boton)
    
    valor = board[coordenadas[0]][coordenadas[1]]

    if valor != "":
        return valor

    else:
        return 0

    
def restricciones(boton, valor, board):


    valor = int(valor)

    lista = list_restriccion(ind, nivel.get())

    if nivel.get() == 4:
        lista = list_restriccion(ind, n)

    """CASOS ESPECIALES"""
    
    # Si el boton esta en la lista de restricciones
    # que estan junto a una restriccion entonces se
    # validan los valores de una manera distinta

    # Se valida las restricciones especiales
    for i in range(len(lista_rest_2)):

        if lista_rest_2[i][1] == boton:

            # Se determina la restriccion
            restriccion = lista_rest_2[i][0]
            
            if restriccion == ">":

               
                # El valor2 va a ser el valor del boton con la restriccion
                valor2 = valores_botones(boton - 1, board)

                # Caso especial: si el valor2 es cero significa que
                # no hay ningun dato registrado entonces se permite el numero
                if valor2 == 0:
                    return True

                # Si el valor es mayor que el valor2 quien debe ser mayor, entonces se
                # retorna falso
                if int(valor) > int(valor2):
                    return False

            if restriccion == "<":
                
                # El valor2 va a ser el valor del boton con la restriccion
                valor2 = valores_botones(boton - 1, board)

                # Caso especial: si el valor2 es cero significa que
                # no hay ningun dato registrado entonces se permite el numero
                if valor2 == 0:
                    return True

                # Si el valor es mayor que el valor2 quien debe ser mayor, entonces se
                # retorna falso
                if int(valor) < int(valor2):
                    return False

            if restriccion == "v":

                # El valor2 va a ser el valor del boton con la restriccion
                valor2 = valores_botones(boton - 5, board)

                # Caso especial: si el valor2 es cero significa que
                # no hay ningun dato registrado entonces se permite el numero
                if valor2 == 0:
                    return True

                # Si el valor es mayor que el valor2 quien debe ser mayor, entonces se
                # retorna falso
                if int(valor) > int(valor2):
                    return False
                
            if restriccion == "^":

                # El valor2 va a ser el valor del boton con la restriccion
                valor2 = valores_botones(boton - 5, board)

                # Caso especial: si el valor2 es cero significa que
                # no hay ningun dato registrado entonces se permite el numero
                if valor2 == 0:
                    return True

                # Si el valor es mayor que el valor2 quien debe ser mayor, entonces se
                # retorna falso
                if int(valor) < int(valor2):
                    return False

                

    """CASOS GENERALES"""
    
    for i in range(len(lista)):

        # Si el segundo elemento de alguna
        # tupla de la lista es igual al valor
        # del boton esto significa que este boton
        # tiene una restriccion

        if lista[i][1] == boton:

            # Se determina el tipo de restriccion

            restriccion = lista[i][0]

            if restriccion == ">":

                # Se obtiene el valor del boton que esta
                # junto a este
                valor2 = valores_botones(boton + 1, board)
                
                # Se valida la restriccion
                if int(valor) < int(valor2):
                    return False


            if restriccion == "<":

                # Se obtiene el valor del boton que esta a la par
                valor2 = valores_botones(boton + 1, board)

                if valor2 == 0:
                    return True
                
                # Se valida la restriccion
                if int(valor) > int(valor2):
                    return False
  
            if restriccion == "v":

                # Se obtiene el valor del boton que esta a la par
                valor2 = valores_botones(boton + 5, board)

                if valor2 == 0:
                    return True
                
                # Se valida la restriccion
                if int(valor) < int(valor2):
                    return False

            if restriccion == "^":

                # Se obtiene el valor del boton que esta a la par
                valor2 = valores_botones(boton + 5, board)

                if valor2 == 0:
                    return True
                
                # Se valida la restriccion
                if int(valor) > int(valor2):
                    return False
                

    return True   

#-----------------------------------------------------------------------------------------------------------------------

# Funcion para validar las filas
def fila(board, numero, posicion):

    global no_permite

    # Validar fila
    for i in range(len(board[0])):

        # Se valida cada elemento de la fila
        # Se valida que la funcion no tome
        # en cuenta si la posicion es la misma
        # en la que acaba de poner el numero

        if board[posicion[0]][i] == numero and\
           posicion[1] != i:
            # Se obtienen las coordenas del numero que no
            # permite que se coloque
            no_permite = (posicion[0],i)
            return False
        
        
    return True

#-----------------------------------------------------------------------------------------------------------------------
# Funcion para validar las columnas
def columna(board, numero, posicion):

    global columna_no_permite
    
    # Validar columna
    for i in range(len(board)):
        
        if board[i][posicion[1]] == numero and\
           posicion[0] != i:
            
            columna_no_permite = (i, posicion[1])
            return False

    return True
#-----------------------------------------------------------------------------------------------------------------------

def find_empty(board):

    for i in range(len(board)):

        for j in range(len(board[0])):

            if board[i][j] == "":
                return False

    return True

#-----------------------------------------------------------------------------------------------------------------------

def validar(indice, valor, board, indicador):
    
    # Se configura el texto del boton para que tenga
    # el mismo valor que el numero seleccionado
    lista_botones[indice].config(text = valor)


    # Se obtienen las coordenadas de ese indice
    coordenadas = f_coordenadas(indice)

    # Se crea una variable con la jugada
    jugada = lista_botones[indice]

    # Se agrega la jugada a la lista de jugadas
    lista_jugadas.append(jugada)

    global numero_boton
    # Se almacena el numero del boton en una lista
    numero_boton += [indice] 
    
    board[coordenadas[0]][coordenadas[1]] = valor

    # Se gana el juego si el board no tiene espacios vacios
    global terminado
    terminado = find_empty(board)

    if terminado == True:

        if nivel.get() == 4:

            # Se decide si va al top
            decidir_top(tiempo_final)
            messagebox.showinfo(message = 'FELICIDADES! HA COMPLETADO EL JUEGO')
            jugar.destroy()
            open_jugar(n + 1)

        else:
            
            # Se envia un mensaje diciendo que ya acabo el juego
            messagebox.showinfo(message = 'FELICIDADES! HA COMPLETADO EL JUEGO')
            decidir_top(tiempo_final)
        
    # Se determina si cumple con la restriccion
    restriccion = restricciones(indice, valor, board)

    # Caso especial
    if indice in lista_rest_2:
        restricciones(indice, valor)

    if restriccion == False:
        
        # Se quita la ultima jugada y el ultimo indice
        lista_jugadas.pop()
        numero_boton.pop()
        
        # Poner de color rojo el boton que no permite la jugada
        lista_botones[indice].config(bg = "tomato")
        messagebox.showerror(message = 'Jugada no es valida porque porque el elemento no cumple con la restriccion')
        lista_botones[indice].config(text = "")
        
        lista_botones[indice].config(bg = "gray95")

        # Quitar el elemento del board
        board[coordenadas[0]][coordenadas[1]] = ""

    # Se hacen las validaciones
    
    validacion_fila = fila(board, valor, (coordenadas))
    

    # Se obtienen el indice del boton que no permite
    # que se coloque el numero ahi
    indice_no_permite = f_indice(no_permite)
    
    
    if validacion_fila == True:
        pass
    
    if validacion_fila == False:

        # Se quita la ultima jugada y el ultimo indice
        lista_jugadas.pop()
        numero_boton.pop()
        
        # Poner de color rojo el boton que no permite la jugada
        lista_botones[indice_no_permite].config(bg = "tomato")

        # Enviar mensaje de error
        messagebox.showerror(message = 'Jugada no es valida porque porque el elemento ya esta en la fila')

        # Quitar el texto y el color rojo de los botones
        lista_botones[indice].config(text = "")
        lista_botones[indice_no_permite].config(bg = "gray95")

        # Quitar el elemento del board
        board[coordenadas[0]][coordenadas[1]] = ""

    validacion_columna = columna(board, valor, (coordenadas))
    indice_no_permite_2 = f_indice(columna_no_permite)
    
    if validacion_columna == False:

        # Poner de color rojo el boton que no permite la jugada
        lista_botones[indice_no_permite_2].config(bg = "tomato")

        # Enviar mensaje de error
        messagebox.showerror(message = 'Jugada no es valida porque porque el elemento ya esta en la columna')

        # Quitar el texto y el color rojo de los botones
        lista_botones[indice].config(text = "")
        lista_botones[indice_no_permite_2].config(bg = "gray95")

        # Quitar el elemento del board
        board[coordenadas[0]][coordenadas[1]] = ""

        # Se quita la ultima jugada y el ultimo indice
        lista_jugadas.pop()
        numero_boton.pop()

    
#-----------------------------------------------------------------------------------------------------------------------
    
def boton_seleccionado(indice, valor, board, indicador):
    global jugada, coordenadas

    try:

        
        
        # En caso de que el valor no haya sido definido se envia un error
        if valor == 0:

            # Se cambia el valor a vacio
            valor = ""

            # Se envia el mensaje
            messagebox.showerror(message = 'Digite un numero primero')

        # Se determina si el juego es cargado
        if indicador == True:
            
            # Solo los numeros inciales de la partida son fijos
            if indice in lista_indices_g:
                lista_botones[indice].config(bg = "tomato")
                messagebox.showerror(message = 'Jugada no es valida porque este es un numero fijo')
                lista_botones[indice].config(bg = "gray95")

            else:
                validar(indice, valor, board, indicador)

        if indicador == False and indice in lista_indices:
            # Se determina si es un numero fijo
            lista_botones[indice].config(bg = "tomato")
            messagebox.showerror(message = 'Jugada no es valida porque este es un numero fijo')
            lista_botones[indice].config(bg = "gray95")
           
        if not(indice in lista_indices):

            
            # Se obtienen las coordenadas
            coordenadas = f_coordenadas(indice)

            # Label que sirve solo para visualizacion mejor
            Label(jugar, text = 'Posibles Jugadas').place(x=590, y=170)
            Label(jugar, text= '  .         ', bg = "light cyan").place(x=600, y=150)

            # Se llama funcion que va a contener las posibles jugadas
            jugadas(coordenadas[0], coordenadas[1], board)
         
            # Se validan
            validar(indice, valor, board, indicador)

    except ValueError:
        pass

    except NameError:
        pass

    except IndexError:
        pass

#-----------------------------------------------------------------------------------------------------------------------

# Funcion para borrar todo el juego
def clicked_borrar():

    if juego_iniciado == True:

        # Se le pregunta al usuario si desea borrar el juego
        respuesta = messagebox.askyesno(message = 'Desea borrar el juego?')

        # Si la respuesta es si
        if respuesta == 1:

            indice = 0

            # Se quita el texto de todos los botones
            for x in lista_botones:

                # Se verifica que no sea un numero fijo
                if not(indice in lista_indices):

                    lista_botones[indice].config(text = "")

                # Se aumenta el contador
                indice += 1

        # Si la respuesta es no, nada ocurre
        if respuesta == 0:
            pass

    else:
         messagebox.showinfo(message = 'Debe iniciar el juego para borrar el juego')

#-----------------------------------------------------------------------------------------------------------------------
lista_rehacer = []
lista_rehacer_valores = []
bn_rehacer = []
# Funcion para eliminar ultima jugada
def borrar_jugada(board):

    global lista_rehacer, lista_rehacer_valores, bn_rehacer, lista_jugadas
    
    # Solo funciona si ya se inicio el juego
    if juego_iniciado == True:

        try:
            # Variable que contiene la ultima jugada
            ultima_jugada = lista_jugadas[-1]

            # Se agrega jugada a rehacer
            lista_rehacer.append(ultima_jugada)

            # Se obtiene el valor de la ultima jugada
            valor_jugada = ultima_jugada["text"]
            bn_rehacer.append(numero_boton[-1])

            # Se configura el texto del boton a vacio
            ultima_jugada.config(text = "")
            
            # Se quita la ultima jugada
            lista_jugadas.pop()
            
            # Se quita el valor de esa jugada del board
            cd = f_coordenadas(numero_boton[-1])
            board[cd[0]][cd[1]] = ""

            # Se quita el ultimo valor de la lista de indices de botones
            numero_boton.pop()

            # Se agrega el vaalor de jugadas borradas a una lista
            lista_rehacer_valores.append(valor_jugada)

        # Si la lista de jugadas se queda sin elementos
        # se envia un mensaje de error
        except:
            messagebox.showerror(message = 'No hay más jugadas para borrar')

    # De lo contrario retorna un mensaje
    else:
         messagebox.showinfo(message = 'Debe iniciar el juego para borrar una jugada')

#-----------------------------------------------------------------------------------------------------------------------

def rehacer_jugada(board):

    global lista_jugadas
    if juego_iniciado == True:

        try:
            
            # Se obtiene el valor de la jugada borrado
            valor_j = lista_rehacer_valores[-1]

            # Se modifica el texto
            lista_rehacer[-1].config(text = valor_j)

            # Se debe agregar a la lista de jugadas
            lista_jugadas.append(lista_rehacer[-1])

            # Se obtiene le numero del boton en que se rehizo la jugada
            bn_rh = bn_rehacer[-1]

            # Se obtienen las coordenadas
            cd_1 = f_coordenadas(bn_rehacer[-1])
            # Se vuelve a colocar eel valor en el board
            board[cd_1[0]][cd_1[1]] = valor_j

            # Se elimina
            lista_rehacer_valores.pop()
            lista_rehacer.pop()
            
        except IndexError:
            messagebox.showerror(message = 'No hay más jugadas para rehacer')

    else:
        messagebox.showinfo(message = 'Debe iniciar el juego para rehacer una jugada')

#-----------------------------------------------------------------------------------------------------------------------

def terminar_juego():


    if juego_iniciado == True:

        # Se le pregunta al usuario si desea borrar el juego
        respuesta = messagebox.askyesno(message = 'Desea terminar el juego?')

        # Si la respuesta es si
        if respuesta == 1:
            # Se quita la ventana
            jugar.withdraw()
            # Se vuelve a abrir la ventana
            open_jugar()

        # Si la respuesta es no, nada ocurre
        if respuesta == 0:
            pass

    else:
        messagebox.showinfo(message = 'Debe iniciar el juego para borrarlo')



#-----------------------------------------------------------------------------------------------------------------------

# Funcion para validar los datos del timer
def validar_timer():

    if int(horas1.get()) > 2 or int(horas1.get()) < 0:
        messagebox.showinfo(message = 'Horas deben entre 0 y 2')

    if int(minutos1.get()) > 59 or int(minutos1.get()) < 0:
        messagebox.showinfo(message = 'Mintuos deben ser deben entre 0 y 59')

    if int(segundos1.get()) > 59 or int(segundos1.get()) < 0:
        messagebox.showinfo(message = 'Segundos deben ser deben entre 0 y 59')

    if int(segundos1.get()) == 0 and int(minutos1.get()) == 0 and\
        int(horas1.get()) == 0:
        messagebox.showinfo(message = 'Debe introducir al menos un dato')
       
#-----------------------------------------------------------------------------------------------------------------------

def open_configurar():

    global nivel, reloj, posicion, entro_configurar
    
    entro_configurar = True 

    configurar = Toplevel()

    lbl = Label(configurar, text="Configurar",  bg="light sky blue", fg="white",font=("Aharoni",30),
      bd=1, relief="solid").pack()

    # Titulo
    configurar.title("Configurar")
    
    # Tamaño
    miFrame2 = Frame(configurar, width = 800, height= 500)
    miFrame2.pack()

    # El usuario no va a poder modificar el tamaño
    configurar.resizable(0,0)
    
    # Se agregan los textos
    
    facilLabel= Label(configurar,text="1. Nivel:")
    facilLabel.place(x=100,y=100)

    relojLabel = Label(configurar, text= "2. Reloj:")
    relojLabel.place(x = 100, y = 220)

    digitosLabel = Label(configurar, text="3. Posición en la ventana\n del panel de dígitos:")
    digitosLabel.place(x= 100, y = 330)
    
    # Se indice que la variable nivel va a ser un int
    nivel = IntVar()
    nivel.set("1")

    # Por default el nivel siempre va a estar en facil

    # Se indica que la variable reloj va a ser un int
    reloj = IntVar()
    # Por default va a tener reloj si
    reloj.set("1")

    # Se indica que la variabla posicion va a ser un int
    posicion = IntVar()

    # Por default van a estar a la derecha
    posicion.set("1")
    
    # Se agregan los circulos redondos que funcionan para escoger
    # distintas opciones

   
    # Nivel Fácil
    facil = Radiobutton(configurar, text="Fácil", variable = nivel, value=1)
    facil.place(x = 300, y = 100)

    # Nivel Intermedio
    intermedio = Radiobutton(configurar, text="Intermedio", variable = nivel, value=2)
    intermedio.place(x = 300, y = 130)
    
    # Nivel Dificil
    intermedio = Radiobutton(configurar, text="Difícil", variable = nivel, value=3)
    intermedio.place(x = 300, y = 160)

    # Multinivel
    multinivel = Radiobutton(configurar, text="Multinivel", variable = nivel, value=4)
    multinivel.place(x = 300, y = 190)
    
    # Reloj Si
    reloj_si = Radiobutton(configurar, text="Si", variable = reloj, value = 1)
    reloj_si.place(x = 300, y = 220)

    # Reloj no
    reloj_no = Radiobutton(configurar, text="No", variable = reloj, value = 2)
    reloj_no.place(x = 300, y = 250)

    # Timer
    timer = Radiobutton(configurar, text="Timer", variable = reloj, value = 3)
    timer.place(x = 300, y = 280)

    # Digitos derecha
    derecha = Radiobutton(configurar, text="Derecha", variable = posicion, value = 1)
    derecha.place(x = 300, y= 330)

    # Digitos Izquierda
    izquierda =  Radiobutton(configurar, text="Izquierda", variable = posicion, value = 2)
    izquierda.place(x = 300, y= 360)
    

    global h, m, s
    h = IntVar()
    h.set("0")

    m = IntVar()
    m.set("0")

    s = IntVar()
    s.set("0")

    # Timer
    
    # Textos
    Label(configurar, text= "Horas").place(x=467.5, y=210)
    Label(configurar, text= "Minutos").place(x=503, y=210)
    Label(configurar, text= "Segundos").place(x=550, y=210)

    global horas, minutos, segundos
    
    # Boton para aceptar
    boton_aceptar = Button(configurar, text="Aceptar", height=1,
                           width=5, command = validar_timer).place(x = 610, y = 235)

    # Indicar al usuario que coloque un cero donde no va a poner numeros
    Label(configurar, text="Coloque un cero en aquellos datos que no desee",
          bg="light sky blue", fg="white", bd=1, relief="solid").place(x = 465, y= 300)

    ejemplo = Label(configurar,
          text="Ejemplo: Si desea un timer de 5 min,\n coloque cero en las horas y segundos",
                    bg="light sky blue", fg="white", bd=1, relief="solid")
    ejemplo.place(x= 520, y = 330)

    global horas1, minutos1, segundos1
    # Se declaran las variables
    horas1=StringVar() 
    minutos1=StringVar() 
    segundos1=StringVar()

    # Por defaul los valores van a ser cero

    horas1.set("00") 
    minutos1.set("00") 
    segundos1.set("00")

    # Entradas
    horas = Entry(configurar, justify='right', font=("Arial",12), textvariable=horas1)
    horas.place(height = 25, width = 35, x = 467.5, y= 235)
    minutos = Entry(configurar, justify='right', font=("Arial",12), textvariable=minutos1)
    minutos.place(height = 25, width = 35, x =  510,y= 235)
    segundos = Entry(configurar, justify='right', font=("Arial",12), textvariable=segundos1)
    segundos.place(height = 25, width = 35, x = 560, y= 235)


    
    configurar.mainloop()

#-----------------------------------------------------------------------------------------------------------------------
  
# Se valida que el nombre sea dado antes de iniciar la partida 
def nombre():

    global nombre_registrado

    if len(nombre_jugador.get()) < 0 or\
        len(nombre_jugador.get()) > 20:
        messagebox.showerror(message = 'Nombre debe tener menos de 20 caracteres')

    if nombre_jugador.get() == "":
        nombre_registrado = False

    else:
        nombre_registrado = True
    

#-----------------------------------------------------------------------------------------------------------------------

"""-------------------RELOJ-------------------"""
proceso = 0
def reloj1(lugar, tiempo):
    
    class App():
        
        
        # Funcion que define la variable count y le indica que se comience
        # llamando a otra funcion
        def start(self):
            
            try:
                if nombre_registrado == False:
                    
                    messagebox.showinfo(message = 'Debe introducir el nombre del jugador')
                else:
                    global juego_iniciado
                    juego_iniciado = True
                    global count
                    count = 0
                    self.start_timer()
                
            except NameError:
                messagebox.showinfo(message = 'Debe introducir el nombre del jugador')
            

        def start_timer(self):

            global count
            self.timer()

        def stop2(self):
            try:
                
                if terminado == True:

                    # Se actualiza el top 10 y se abre la ventana respectiva
                    update()
                    open_top()

                global tiempo_final
                tiempo_final = (self.d)

                global count
                count = 1
                open_top()

            except AttributeError:
                open_top()

        def stop(self):

            try:

                if terminado == True:
                    
                    global tiempo_final
                    tiempo_final = (self.d)

                    global count
                    count = 1

                    # Se actualiza el top 10 y se abre la ventana respectiva
                    update()
                    open_top()
                if terminado == False:
                    messagebox.showerror(message = 'Solo puede detener el tiempo si ya termino el juego')

   
            except AttributeError:
                open_top()

        def timer(self):

            global count

            # Si el tiempo debe estar corriendo ocurre lo siguiente
            if count == 0:
                global d
                # Se obtiene el valor de la variable t y se almacena en d
                self.d = str(self.t.get())
                global tiempo_final
                tiempo_final = (self.d)
                # Se divide la variable d en tres partes: horas, minutos y segundos
                # Se usa la funcion map
                h, m, s = map(int, self.d.split(":"))

                # Se convierten en un numero entero
                h = int(h)
                m = int(m)
                s = int(s)

                # Si los segundos son menores que 59 entonces simplemente
                # se aumenta en 1
                if s < 59:
                    s += 1

                # Si los segundos == 59 entonces se coloca s en 0
                elif s == 59:
                    s = 0

                    # Se debe aumentar los minutos
                    # Si m es menor que 59 simplemente se aumenta en 1
                    if m < 59:
                        m+= 1

                    # Si los minutos == 59 entonces se aumentan las horas
                    elif m == 59:
                        h += 1

                # Se aplica la siguiente logica para que el reloj
                # se muestre 01:08:09 y no asi 1:8:9

                # Si las horas son menor que 10 se le agrega un 0 al inicio
                if h < 10:
                    h = str(0)+str(h)
                # De lo contario h continua igual
                else:
                    h = str(h)

                # Si los minuto son menores que 10 se le agrega un 0 al inicio
                if m < 10:
                    m = str(0)+str(m)
                # De lo contario m continua igual    
                else:
                    m = str(m)

                # Si los segundos son menores que 10 se le agrega un 0 al inicio
                if s < 10:
                    s = str(0)+str(s)
                # De lo contario s continua igual   
                else:
                    s = str(s)

                # Se unen de nuevo los numeros
                self.d = h + ":" + m + ":" + s

                # Se coloca en la variable t que es la que se muestra en pantalla
                self.t.set(self.d)

                # Como es un reloj se debe realizar lo anterior varias veces
                # Entonces despues de 930 milisegundos se llama a la funcion
                if count == 0:
                    self.root.after(930, self.start_timer)

            

        def __init__(self):
            self.root = lugar
            # Se declara la variable t que va a tener el tiempo
            self.t = StringVar()
            # Se comienza en cero
            self.t.set(tiempo)

            # Se crea una label que va a contener como texto la variable t
            self.lb = Label(lugar, textvariable = self.t)
            # Se configura el tipo de letra
            self.lb.config(font=("Courier 25 bold"))
            
            # Se agrega boton de iniciar juego
            self.boton_iniciar = Button(lugar, text="INICIAR\n JUEGO", bg= "VioletRed1",
                           font=("Aharoni",10), command= self.start)

            # Se agrega boton top 10
            self.boton_top = Button(lugar, text="TOP\n 10", bg= "gold",
                           font=("Aharoni",10), command = self.stop2)
            
            
            self.bt2 = Button(lugar, text="Stop", command = self.stop,
                       font=("Courier 10 bold"))

            # Se colocan los widgets en la pantalla
            self.lb.place(x = 50, y =600)
            self.boton_iniciar.place(x=50, y=500, height=50, width=100)
            self.bt2.place(x = 110, y =650)
            self.boton_top.place(x=530, y=500, height=50, width=100)

    App()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

"""-------------------COUNTDOWN TIMER-------------------"""
def reloj2(lugar, tiempo):

    global count

    # Variable que nos dice si se ya se empezo o se detuvo el reloj
    # Count = 0 -> El tiempo se detiene
    # Count = 1 -> El tiempo corre

    count = 0
    x = 1
    # Se crea la clase
    class App():
        
        def update(self):

            # Se validan las restricciones
            
            if int(horas1.get()) > 2 or int(horas1.get()) < 0:
                messagebox.showinfo(message = 'Horas deben entre 0 y 2')

            if int(minutos1.get()) > 59 or int(minutos1.get()) < 0:
                messagebox.showinfo(message = 'Mintuos deben ser deben entre 0 y 59')

            if int(segundos1.get()) > 59 or int(segundos1.get()) < 0:
                messagebox.showinfo(message = 'Segundos deben ser deben entre 0 y 59')

            if int(segundos1.get()) == 0 and int(minutos1.get()) == 0 and\
               int(horas1.get()) == 0:
                messagebox.showinfo(message = 'Debe introducir al menos un dato')
            
            if int(horas1.get()) < 2 and int(horas1.get()) >= 0 and\
               int(minutos1.get()) < 59 and int(minutos1.get()) >= 0 and\
               int(segundos1.get()) < 59 and int(segundos1.get()) >= 0:
                
                global tiempo_timer, x
                x = 0
                # Se obtiene el valor de las entradas despues de dar click en aceptar
                tiempo_timer =  horas1.get() + ":" + minutos1.get() + ":" + segundos1.get()

                # Se configura el texto del timer
                self.t.set(tiempo_timer)
                self.lb.config(text = tiempo_timer)
            
 
        # Funcion que define la variable count y le indica que se comience
        # llamando a otra funcion

        def start(self):
            global juego_iniciado
            juego_iniciado = True
            try:
                if nombre_registrado == False:
                    messagebox.showinfo(message = 'Debe introducir el nombre del jugador')
                else:
                    global count
                    count = 0
                    self.start_timer()
                
            except NameError:
                messagebox.showinfo(message = 'Debe introducir el nombre del jugador')

        def start_timer(self):

            global count
            self.timer()

        def stop2(self):
            
            try:
                
                global tiempo_final
                tiempo_final = (self.d)

                global count
                count = 1

                open_top()

            except AttributeError:
                open_top()
            
        def stop(self):
            try:

                if terminado == True:
                    # Se detiene el tiempo
                    global tiempo_final
                    tiempo_final = (self.d)

                    global count
                    count = 1

                    # Se actualiza el top 10 y se abre la ventana respectiva
                    update()
                    open_top()



                # Si no ha terminado el juego el boton stop no realiza nada
                if terminado == False:
                    messagebox.showerror(message = 'Solo puede detener el tiempo si ya termino el juego')

   
            except AttributeError:
                open_top()

            
        def timer(self):

            global count
            
            try:
                # Si el tiempo debe estar corriendo ocurre lo siguiente
                if count == 0:

                    # Se obtiene el valor de la variable t y se almacena en d
                    self.d = str(self.t.get())
                    global tiempo_final
                    tiempo_final = (self.d)
                    # Se divide la variable d en tres partes: horas, minutos y segundos
                    # Se usa la funcion map
                    h, m, s = map(int, self.d.split(":"))

                    # Se convierten en un numero entero
                    h = int(h)
                    m = int(m)
                    s = int(s)

                    # Si los segundos son menores que 59 entonces simplemente
                    # se aumenta en 1
                    if s > 0:
                        s -= 1

                    # Si los segundos == 59 entonces se coloca s en 0
                    elif s == 0:
                        s = 59

                        # Se debe aumentar los minutos
                        # Si m es menor que 59 simplemente se aumenta en 1
                        if m > 0:
                            m -= 1

                        # Si los minutos == 59 entonces se aumentan las horas
                        elif m == 0:
                            m = 59
                            h -= 1

                    # Se aplica la siguiente logica para que el reloj
                    # se muestre 01:08:09 y no asi 1:8:9

                    # Si las horas son menor que 10 se le agrega un 0 al inicio
                    if h < 10:
                        h = str(0)+str(h)
                    # De lo contario h continua igual
                    else:
                        h = str(h)

                    # Si los minuto son menores que 10 se le agrega un 0 al inicio
                    if m < 10:
                        m = str(0)+str(m)
                    # De lo contario m continua igual    
                    else:
                        m = str(m)

                    # Si los segundos son menores que 10 se le agrega un 0 al inicio
                    if s < 10:
                        s = str(0)+str(s)
                    # De lo contario s continua igual   
                    else:
                        s = str(s)

                    # Se unen de nuevo los numeros
                    self.d = h + ":" + m + ":" + s

                    # Se coloca en la variable t que es la que se muestra en pantalla
                    self.t.set(self.d)

                    # Si el tiempo es cero significa que se acabo
                    if self.d == "00:00:00":

                        # Se detiene el timer
                        self.stop

                        # Se le pregunta al usuario que desea hacer
                        respuesta = messagebox.askyesno(message =\
                                    'Tiempo expirado\n Desea continuar el juego?')
                        
                        if respuesta == 1:

                            # Se destruyen los botones y las labels
                            self.boton_aceptar.destroy()
                            horas.destroy()
                            minutos.destroy()
                            segundos.destroy()
                            self.lb.destroy()
                            self.bt2.destroy()
                            
                            # Se llama a la funcion reloj con el tiempo que tenia el timer
                            reloj1(lugar, tiempo_timer)
                    
                    # Como es un reloj se debe realizar lo anterior varias veces
                    # Entonces despues de 930 milisegundos se llama a la funcion
                    else:
                        self.root.after(930, self.start_timer)

            except ValueError:
                pass
                    
        def __init__(self):

            self.root = lugar
            # Se declara la variable t que va a tener el tiempo
            self.t = StringVar()

            # Se comienza el timer segun las variables
            
            if x != 0:
                global tiempo_timer
                tiempo_timer = horas1.get() + ":" + minutos1.get() + ":" + segundos1.get()
                
                self.t.set(tiempo_timer)
            try:
                if entrar_cargar == True:
                    self.t.set(tiempo)
            except NameError:
                pass
            # Se crea una label que va a contener como texto la variable t
            self.lb = Label(self.root, textvariable = self.t)
            # Se configura el tipo de letra
            self.lb.config(font=("Courier 20 bold"))
            
            # Se crean los botones
            
            self.boton_iniciar = Button(lugar, text="INICIAR\n JUEGO", bg= "VioletRed1",
                           font=("Aharoni",10), command= self.start)

            self.boton_aceptar = Button(self.root, text="Aceptar", height=1,
                           width=5, command = self.update)

            # Se agrega boton top 10
            self.boton_top = Button(lugar, text="TOP\n 10", bg= "gold",
                           font=("Aharoni",10), command = self.stop2)
            
            self.bt2 = Button(self.root, text="Stop", command = self.stop,
                       font=("Courier 10 bold"))

            # Se colocan los widgets en la pantalla
            self.lb.place(x = 50, y =630)
            self.boton_aceptar.place(x = 220, y = 590)
            self.boton_iniciar.place(x=50, y=500, height=50, width=100)
            self.bt2.place(x = 200, y =635)
            self.boton_top.place(x=530, y=500, height=50, width=100)

    a = App()            

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def guardar(board):

    if juego_iniciado == True:
        
        
        guardar = open("futoshiki2020juegoactual.dat","wb")

        # Se vacia el archivo
        guardar.seek(0)
        guardar.truncate()

        # Se guardan los datos actuales en variables
        nombre_g = nombre_jugador.get()
        reloj_g = reloj.get()
        digitos_g = posicion.get()
        nivel_g = nivel.get()
        indice_partida = ind
        board_g = board
        numero_boton_g = numero_boton
        lista_indices_g = lista_indices
        tiempo_g = tiempo_final
        
        
        # Se agregan al archivo
        pickle.dump(nombre_g, guardar)
        pickle.dump(digitos_g, guardar)
        pickle.dump(reloj_g, guardar)
        pickle.dump(nivel_g, guardar)
        pickle.dump(indice_partida, guardar)
        pickle.dump(board_g, guardar)
        pickle.dump(numero_boton_g, guardar)
        pickle.dump(lista_indices_g, guardar)
        pickle.dump(tiempo_g, guardar)
        
        guardar.close()

    else:
        messagebox.showerror(message = "Debe iniciar el juego para guardar la partida")
    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def restriccion_facil(ind, lugar):

    if ind == 0:
        
        # Labels
        Label(lugar, text= ">", font=("Aharoni",15, BOLD),fg= "black").place(x=250, y=160)
        Label(lugar, text= ">", font=("Aharoni",15, BOLD),fg= "black").place(x=390, y=160)
        Label(lugar, text= ">", font=("Aharoni",15, BOLD),fg= "black").place(x=465, y=160)
        Label(lugar, text= "<", font=("Aharoni",15, BOLD),fg= "black").place(x=465, y=380)      
        Label(lugar, text= "<", font=("Aharoni",15, BOLD),fg= "black").place(x=250, y=450)    
        Label(lugar, text= "<", font=("Aharoni",15, BOLD),fg= "black").place(x=320, y=450)

        
    if ind == 1:
       
        Label(lugar, text= "<", font=("Aharoni",15, BOLD),fg= "black").place(x=250, y=160)
        Label(lugar, text= "<", font=("Aharoni",15, BOLD),fg= "black").place(x=465, y=160)
        Label(lugar, text= "<", font=("Aharoni",15, BOLD),fg= "black").place(x=465, y=230)
        Label(lugar, text= "^", font=("Aharoni",15, BOLD),fg= "black").place(x=355, y=265)
        Label(lugar, text= "<", font=("Aharoni",15, BOLD),fg= "black").place(x=465, y=300)
        Label(lugar, text= "^", font=("Aharoni",15, BOLD),fg= "black").place(x=355, y=335)
        Label(lugar, text= ">", font=("Aharoni",15, BOLD),fg= "black").place(x=250, y=370)
        Label(lugar, text= "^", font=("Aharoni",15, BOLD),fg= "black").place(x=500, y=415)
        

    if ind == 2:

        Label(lugar, text= "v", font=("Aharoni",13, BOLD),fg= "black").place(x=215, y=195)
        Label(lugar, text= "<", font=("Aharoni",15, BOLD),fg= "black").place(x=320, y=235)
        Label(lugar, text= "<", font=("Aharoni",15, BOLD),fg= "black").place(x=320, y=370)
        Label(lugar, text= "<", font=("Aharoni",15, BOLD),fg= "black").place(x=390, y=235)
        Label(lugar, text= "^", font=("Aharoni",15, BOLD),fg= "black").place(x=430, y=340)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def restriccion_intermedio(ind, lugar):
    
    if ind == 0:
        Label(lugar, text= ">", font=("Aharoni",15, BOLD),fg= "black").place(x=250, y=160)             
        Label(lugar, text= "^", font=("Aharoni",15, BOLD),fg= "black").place(x=215, y=265)
        Label(lugar, text= "v", font=("Aharoni",13, BOLD),fg= "black").place(x=285, y=265)
        Label(lugar, text= "^", font=("Aharoni",15, BOLD),fg= "black").place(x=430, y=340)
        Label(lugar, text= "v", font=("Aharoni",13, BOLD),fg= "black").place(x=505, y=413)


    if ind == 1:

        Label(lugar, text= ">", font=("Aharoni",15, BOLD),fg= "black").place(x=250, y=160)
        Label(lugar, text= ">", font=("Aharoni",15, BOLD),fg= "black").place(x=390, y=160)
        Label(lugar, text= "v", font=("Aharoni",13, BOLD),fg= "black").place(x=430, y=268)
        Label(lugar, text= "v", font=("Aharoni",13, BOLD),fg= "black").place(x=288, y=340)
        Label(lugar, text= "v", font=("Aharoni",13, BOLD),fg= "black").place(x=360, y=340)
        Label(lugar, text= "^", font=("Aharoni",15, BOLD),fg= "black").place(x=500, y=338)
        Label(lugar, text= "v", font=("Aharoni",13, BOLD),fg= "black").place(x=430, y=410)
        Label(lugar, text= "^", font=("Aharoni",15, BOLD),fg= "black").place(x=500, y=410)

    if ind == 2:

        Label(lugar, text= "<", font=("Aharoni",15, BOLD),fg= "black").place(x=250, y=235)
        Label(lugar, text= "<", font=("Aharoni",15, BOLD),fg= "black").place(x=250, y=300)
        Label(lugar, text= "^", font=("Aharoni",15, BOLD),fg= "black").place(x=500, y=193)
        Label(lugar, text= "^", font=("Aharoni",15, BOLD),fg= "black").place(x=500, y=268)
        Label(lugar, text= "^", font=("Aharoni",15, BOLD),fg= "black").place(x=430, y=268)
        Label(lugar, text= "^", font=("Aharoni",15, BOLD),fg= "black").place(x=430, y=410)


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
def restriccion_dificil(ind, lugar):

    if ind == 0:
                
        Label(lugar, text= ">", font=("Aharoni",15, BOLD),fg= "black").place(x=250, y=160)
        Label(lugar, text= ">", font=("Aharoni",15, BOLD),fg= "black").place(x=390, y=230)
        Label(lugar, text= ">", font=("Aharoni",15, BOLD),fg= "black").place(x=465, y=230)
        Label(lugar, text= "<", font=("Aharoni",15, BOLD),fg= "black").place(x=465, y=450)
        Label(lugar, text= "v", font=("Aharoni",13, BOLD),fg= "black").place(x=360, y=340)

    if ind == 1:

        Label(lugar, text= "<", font=("Aharoni",15, BOLD),fg= "black").place(x=250, y=160)
        Label(lugar, text= ">", font=("Aharoni",15, BOLD),fg= "black").place(x=465, y=160)
        Label(lugar, text= ">", font=("Aharoni",15, BOLD),fg= "black").place(x=390, y=230)
        Label(lugar, text= "v", font=("Aharoni",13, BOLD),fg= "black").place(x=500, y=196)
        Label(lugar, text= ">", font=("Aharoni",15, BOLD),fg= "black").place(x=250, y=300)
        Label(lugar, text= ">", font=("Aharoni",15, BOLD),fg= "black").place(x=320, y=300)
        Label(lugar, text= "^", font=("Aharoni",15, BOLD),fg= "black").place(x=430, y=340)
        Label(lugar, text= ">", font=("Aharoni",15, BOLD),fg= "black").place(x=250, y=450)
        Label(lugar, text= ">", font=("Aharoni",15, BOLD),fg= "black").place(x=465, y=450)

        
    if ind == 2:

        Label(lugar, text= "<", font=("Aharoni",15, BOLD),fg= "black").place(x=250, y=230)
        Label(lugar, text= "<", font=("Aharoni",15, BOLD),fg= "black").place(x=320, y=230)
        Label(lugar, text= "v", font=("Aharoni",13, BOLD),fg= "black").place(x=500, y=196)
        Label(lugar, text= "^", font=("Aharoni",15, BOLD),fg= "black").place(x=500, y=270)
        Label(lugar, text= "^", font=("Aharoni",15, BOLD),fg= "black").place(x=500, y=340)
        Label(lugar, text= "<", font=("Aharoni",15, BOLD),fg= "black").place(x=320, y=300)
        Label(lugar, text= "<", font=("Aharoni",15, BOLD),fg= "black").place(x=250, y=380)
        Label(lugar, text= ">", font=("Aharoni",15, BOLD),fg= "black").place(x=250, y=440)
        Label(lugar, text= "^", font=("Aharoni",15, BOLD),fg= "black").place(x=360, y=410)
        
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def digitos(num, lugar):
    
    # Las variable se hacen globales para que la funcion
    # anterior pueda usarlas
    global boton1, boton2, boton3, boton4, boton5
    
    if num == 1:
        # Botones de numeros
        boton1 = Button(lugar, text="1",font=("Aharoni",10), bg="white",
                        command = lambda:btnpress(1))
        boton1.place(x=700, y=150, width= 50, height=50)

        # Boton 2
        boton2 = Button(lugar, text="2",font=("Aharoni",10), bg="white",
                        command = lambda:btnpress(2))
        boton2.place(x=700, y=220, width= 50, height=50)

        # Boton 3
        boton3 = Button(lugar, text="3",font=("Aharoni",10), bg="white",
                        command = lambda:btnpress(3))
        boton3.place(x=700, y=290, width= 50, height=50)

        # Boton 4
        boton4 = Button(lugar, text="4",font=("Aharoni",10), bg="white",
                        command = lambda:btnpress(4))
        boton4.place(x=700, y=360, width= 50, height=50)

        # Boton 5
        boton5 = Button(lugar, text="5",font=("Aharoni",10), bg="white",
                        command = lambda:btnpress(5))
        boton5.place(x=700, y=430, width= 50, height=50)

    if num == 2:
        # Botones de numeros
        boton1 = Button(lugar, text="1",font=("Aharoni",10), bg="white",
                        command = lambda:btnpress(1))
        boton1.place(x=100, y=150, width= 50, height=50)

        # Boton 2
        boton2 = Button(lugar, text="2",font=("Aharoni",10), bg="white",
                        command = lambda:btnpress(2))
        boton2.place(x=100, y=220, width= 50, height=50)

        # Boton 3
        boton3 = Button(lugar, text="3",font=("Aharoni",10), bg="white",
                        command = lambda:btnpress(3))
        boton3.place(x=100, y=290, width= 50, height=50)

        # Boton 4
        boton4 = Button(lugar, text="4",font=("Aharoni",10), bg="white",
                        command = lambda:btnpress(4))
        boton4.place(x=100, y=360, width= 50, height=50)

        # Boton 5
        boton5 = Button(lugar, text="5",font=("Aharoni",10), bg="white",
                        command = lambda:btnpress(5))
        boton5.place(x=100, y=430, width= 50, height=50)
    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def casillas(lugar, board, indicador):
    
    # Casillas
    global lista_botones, lista_jugadas

    # Lista que va a contener los botones
    lista_botones = []
    lista_jugadas = []

 
    # Fila 0
    casilla0_0 = Button(lugar, width= 5, height=2,
                 command = lambda: boton_seleccionado(0, valor, board, indicador), bg = "gray95")
    lista_botones.append(casilla0_0)


    casilla0_1 = Button(lugar, width= 5, height=2,
                 command = lambda: boton_seleccionado(1, valor, board, indicador), bg = "gray95")
    lista_botones.append(casilla0_1)


    casilla0_2 = Button(lugar, width= 5, height=2,
                 command = lambda: boton_seleccionado(2, valor, board, indicador), bg = "gray95")
    lista_botones.append(casilla0_2)


    casilla0_3 = Button(lugar, width= 5, height=2,
                 command = lambda: boton_seleccionado(3, valor, board, indicador), bg = "gray95")
    lista_botones.append(casilla0_3)


    casilla0_4 = Button(lugar, width= 5, height=2,
                 command = lambda: boton_seleccionado(4, valor, board, indicador), bg = "gray95")
    lista_botones.append(casilla0_4)


    # Fila 1
    casilla1_0 = Button(lugar, width= 5, height=2,
                 command = lambda: boton_seleccionado(5, valor, board, indicador), bg = "gray95")
    lista_botones.append(casilla1_0)


    casilla1_1 = Button(lugar, width= 5, height=2,
                 command = lambda: boton_seleccionado(6, valor, board, indicador), bg = "gray95")
    lista_botones.append(casilla1_1)


    casilla1_2 = Button(lugar, width= 5, height=2,
                 command = lambda: boton_seleccionado(7, valor, board, indicador), bg = "gray95")
    lista_botones.append(casilla1_2)


    casilla1_3 = Button(lugar, width= 5, height=2,
                 command = lambda: boton_seleccionado(8, valor, board, indicador), bg = "gray95")
    lista_botones.append(casilla1_3)


    casilla1_4 = Button(lugar, width= 5, height=2,
                 command = lambda: boton_seleccionado(9, valor, board, indicador), bg = "gray95")
    lista_botones.append(casilla1_4)


    # Fila 2
    casilla2_0 = Button(lugar, width= 5, height=2,
                 command = lambda: boton_seleccionado(10, valor, board, indicador), bg = "gray95")
    lista_botones.append(casilla2_0)


    casilla2_1 = Button(lugar, width= 5, height=2,
                 command = lambda: boton_seleccionado(11, valor, board, indicador), bg = "gray95")
    lista_botones.append(casilla2_1)


    casilla2_2 = Button(lugar, width= 5, height=2,
                 command = lambda: boton_seleccionado(12, valor, board, indicador), bg = "gray95")
    lista_botones.append(casilla2_2)


    casilla2_3 = Button(lugar, width= 5, height=2,
                 command = lambda: boton_seleccionado(13, valor, board, indicador), bg = "gray95")
    lista_botones.append(casilla2_3)


    casilla2_4 = Button(lugar, width= 5, height=2,
                 command = lambda: boton_seleccionado(14, valor, board, indicador), bg = "gray95")
    lista_botones.append(casilla2_4)

    # Fila 3
    casilla3_0 = Button(lugar, width= 5, height=2,
                 command = lambda: boton_seleccionado(15, valor, board, indicador), bg = "gray95")
    lista_botones.append(casilla3_0)

    casilla3_1 = Button(lugar, width= 5, height=2,
                 command = lambda: boton_seleccionado(16, valor, board, indicador), bg = "gray95")
    lista_botones.append(casilla3_1)

    casilla3_2 = Button(lugar, width= 5, height=2,
                 command = lambda: boton_seleccionado(17, valor, board, indicador), bg = "gray95")
    lista_botones.append(casilla3_2)

    casilla3_3 = Button(lugar, width= 5, height=2,
                 command = lambda: boton_seleccionado(18, valor, board, indicador), bg = "gray95")
    lista_botones.append(casilla3_3)

    casilla3_4 = Button(lugar, width= 5, height=2,
                 command = lambda: boton_seleccionado(19, valor, board, indicador), bg = "gray95")
    lista_botones.append(casilla3_4)


    # Fila 4
    casilla4_0 = Button(lugar, width= 5, height=2,
                 command = lambda: boton_seleccionado(20, valor, board, indicador), bg = "gray95")
    lista_botones.append(casilla4_0)


    casilla4_1 = Button(lugar, width= 5, height=2,
                 command = lambda: boton_seleccionado(21, valor, board, indicador), bg = "gray95")
    lista_botones.append(casilla4_1)


    casilla4_2 = Button(lugar,width= 5, height=2,
                 command = lambda: boton_seleccionado(22, valor, board, indicador), bg = "gray95")
    lista_botones.append(casilla4_2)


    casilla4_3 = Button(lugar, width= 5, height=2,
                 command = lambda: boton_seleccionado(23, valor, board, indicador), bg = "gray95")
    lista_botones.append(casilla4_3)


    casilla4_4 = Button(lugar,width= 5, height=2,
                 command = lambda: boton_seleccionado(24, valor, board, indicador), bg = "gray95")
    lista_botones.append(casilla4_4)
    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def tiempo(lugar, reloj, tiempo):
    
    # Reloj
    global time
    if reloj == 1:

        # Labels
        Label(lugar, text = "Si termina el juego \n exitosamente de click en stop",
              bg ="light blue", bd=1, relief="solid").place(x = 300, y =650)

        Label(lugar, text = "Si entra al top 10 debe dar click en INICIAR \nJUEGO para que el reloj siga contando",
              bg ="light blue", bd=1, relief="solid").place(x = 480, y = 650)
        
        Label(lugar, text= "Horas").place(x=50, y=560)
        Label(lugar, text= "Minutos").place(x=110, y=560)
        Label(lugar, text= "Segundos").place(x=170, y=560)
        time = Label(lugar, fg='black', width=20, font=("Ahorani","18"))
        time.place(x = -8, y =580) 
        reloj1(lugar, tiempo)
    # Timer
    global timer

    if reloj == 3:
        # Labels

        Label(lugar, text = "Si termina el juego \n exitosamente de click en stop",
              bg ="light blue", bd=1, relief="solid").place(x = 300, y =650)

        Label(lugar, text = "Si entra al top 10 debe dar click en INICIAR \nJUEGO para que el reloj siga contando",
              bg ="light blue", bd=1, relief="solid").place(x = 480, y = 650)

        Label(lugar, text= "Horas").place(x=50, y=560)
        Label(lugar, text= "Minutos").place(x=110, y=560)
        Label(lugar, text= "Segundos").place(x=170, y=560)
        timer = Label(lugar, fg='black', width=20, font=("Ahorani","18"))
        timer.place(x = -8, y =580)

        # Entradas
        global horas, minutos, segundos

        horas = Entry(lugar, justify='right', font=("Arial",12), textvariable=horas1)
        horas.place(height = 25, width = 35, x = 50, y= 590)
        
            
        minutos = Entry(lugar, justify='right',font=("Arial",12), textvariable=minutos1)
        minutos.place(height = 25, width = 35, x = 110, y = 590)

             
        segundos = Entry(lugar, justify='right', font=("Arial",12), textvariable=segundos1)
        segundos.place(height = 25, width = 35, x = 170, y= 590)
        
        reloj2(lugar, tiempo)
        
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def cargar():
    
    if juego_iniciado == False:
        global entrar_cargar
        entrar_cargar = True

        # Se cierra la ventana
        jugar.withdraw()

        # Se vuelve a abrir pero con la informacion dada
        cargar = Toplevel()
        cargar.title("Juego")
        
        CargarFrame = Frame(cargar, width = 800, height= 700)
        CargarFrame.pack()
        cargar.resizable(0,0)
    
        # Se abre el archivo    
        guardar = open("futoshiki2020juegoactual.dat","rb")

        global board_g
        # Se obtienen los datos guardados
        nombre_g = pickle.load(guardar)

        digitos_g = pickle.load(guardar)

        reloj_g = pickle.load(guardar)

        nivel_g = pickle.load(guardar)

        indice_partida = pickle.load(guardar)      

        board_g = pickle.load(guardar)

        global lista_indices_g
        numero_boton_g = pickle.load(guardar)

        lista_indices_g = pickle.load(guardar)

        # Se agrega el nombre del juego
        Label(CargarFrame, text="Futoshiki", bg="red", fg="white",font=("Copperplate Gothic Bold",30),
              bd=1, relief="solid").place(x=300, y=0)

        
        global nombre_jugador
        
        # Se agrega la entrada del nombre del jugador
        nombre_jugador = Entry(cargar)
        nombre_jugador.place(x=250, y=100, width=300)

        # Se agrega el nombre del jugador
        nombre_jugador.insert(0, nombre_g)
        
        # Se agrega texto
        nombreLabel= Label(cargar,text="Nombre del jugador:")
        nombreLabel.place(x=100,y=100)

        # Boton que de aceptar al nombre
        nombre_boton = Button(cargar, text="OK", bg= "lavender", font=("Aharoni",10), command= nombre)
        nombre_boton.place(x= 570, y = 98, height=25, width=25)    

        # Se llama a la funcion que imprime los botones principales
        botones_principales(cargar, board_g)

        # Se imprimen los digitos
        digitos(digitos_g, cargar)
        
        # Se imprimen las restricciones
        if nivel_g == 1:
            restriccion_facil(indice_partida, cargar)

        if nivel_g == 2:
            restriccion_intermedio(indice_partida, cargar)

        if nivel_g == 3:
            restriccion_dificil(indice_partida, cargar)

        # Se indican las casillas
        casillas(cargar, board_g, True)
        
        # Se imprimen los botones
        imprimir_botones_g(indice_partida, board_g, lista_indices_g)
        
        # Tiempo
        tiempo_g = pickle.load(guardar)
        tiempo(cargar, reloj_g, tiempo_g)
        
        # Se cierra el archivo
        guardar.close()

        cargar.mainloop()

    else:
        messagebox.showerror(message = "No puede cargar el juego si ya ha iniciado la partida")
        
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def imprimir_botones_g(ind, board, lista):

    # PARTIDAS FACILES
    f = open("futoshiki2020partidasfaciles.dat", "rb")
    if nivel.get() == 1:

        lista_partidas_faciles = pickle.load(f)

        # Se llena la matriz board
        for j in lista_partidas_faciles[ind]:

            if j[0] == "v" or j[0] == "^" or\
               j[0] == ">" or j[0] == "<":

                pass
                
            else:
                index = lista_partidas_faciles[ind].index(j)
                # Se obtiene el numero que hay que colocar en la casilla
                valor1 = int(lista_partidas_faciles[ind][index][0])
                # Se obtiene el primer indice
                indice1 = lista_partidas_faciles[ind][index][1]
                # Se obtiene el segundo indice
                indice2 = lista_partidas_faciles[ind][index][2]
                # Se llena la casilla con el valor
                # Esto se hace en la posicion segun los indices
                board[indice1][indice2] = str(valor1)


        # Se imprimen los botones
        # Se crea una lista que contenga los indices de los botones que son fijos
        global lista_indices
        lista_indices = []
        fila_pos = 200
        columna_pos = 150
        boton = 0
        x = 0
        y = 0
        for fila in range(0,5):
            for columna in range(0,5):
                             

                lista_botones[boton].place(x = fila_pos, y = columna_pos)

                if board[x][y] == "":
                    lista_botones[boton].config(text = "")

                if board[x][y] != "":
                    lista_botones[boton].config(text = board[x][y])
                    # Se agrega el indice del boton fijo a la lista
                    lista_indices += [boton]

                # Se ponen en negrita solo aquellos que sean fijos
                if boton in lista:
                    lista_botones[boton].config(font=("Calibri (Body)", 9, BOLD))
                    

                boton += 1
                y += 1
                fila_pos += 72

            x += 1
            y = 0
            columna_pos += 72
            fila_pos = 200

        # Se imprimen las restricciones segun el indice
        if ind == 0:
           restriccion_facil(ind, jugar)
            
        if ind == 1:
            restriccion_facil(ind, jugar)
            
        if ind == 2:
            restriccion_facil(ind, jugar)

    f.close()

    # PARTIDAS INTERMEDIAS

    f2 = open("futoshiki2020partidasintermedias.dat","rb")
    
    if nivel.get() == 2:

        
        lista_partidas_intermedias = pickle.load(f2)

        for j in lista_partidas_intermedias[ind]:

            if j[0] == "v" or j[0] == "^" or\
               j[0] == ">" or j[0] == "<":

                pass
                
            else:
                index = lista_partidas_intermedias[ind].index(j)
                # Se obtiene el numero que hay que colocar en la casilla
                valor2 = int(lista_partidas_intermedias[ind][index][0])
                # Se obtiene el primer indice
                indice1 = lista_partidas_intermedias[ind][index][1]
                # Se obtiene el segundo indice
                indice2 = lista_partidas_intermedias[ind][index][2]
                # Se llena la casilla con el valor
                # Esto se hace en la posicion segun los indices
                board[indice1][indice2] = str(valor2)

        # Se crea una lista que contenga los indices de los botones que son fijos
        lista_indices = []

        fila_pos = 200
        columna_pos = 150
        boton = 0
        x = 0
        y = 0

        for fila in range(0,5):
            for columna in range(0,5):
                             

                lista_botones[boton].place(x = fila_pos, y = columna_pos)

                if board[x][y] == "":
                    lista_botones[boton].config(text = "")

                if board[x][y] != "":
                    lista_botones[boton].config(text = board[x][y])
                    # Se agrega el indice del boton fijo a la lista
                    lista_indices += [boton]
                # Se ponen en negrita solo aquellos que sean fijos
                if boton in lista:
                    lista_botones[boton].config(font=("Calibri (Body)", 9, BOLD))
                    
                boton += 1
                y += 1
                fila_pos += 72

            x += 1
            y = 0
            columna_pos += 72
            fila_pos = 200
        
        # Se imprimen las restricciones segun el indice
        if ind == 0:   
            restriccion_intermedio(ind, jugar)

        if ind == 1:
            restriccion_intermedio(ind, jugar)

        if ind == 2:
            restriccion_intermedio(ind, jugar)


    f2.close()


    # PARTIDAS DIFICILES
    
    f3 = open("futoshiki2020partidasdificiles.dat","rb")
    
    if nivel.get() == 3:

        
        lista_partidas_dificiles = pickle.load(f3)

        for j in lista_partidas_dificiles[ind]:

            if j[0] == "v" or j[0] == "^" or\
               j[0] == ">" or j[0] == "<":

                pass
                
            else:
                index = lista_partidas_dificiles[ind].index(j)
                # Se obtiene el numero que hay que colocar en la casilla
                valor3 = int(lista_partidas_dificiles[ind][index][0])
                # Se obtiene el primer indice
                indice1 = lista_partidas_dificiles[ind][index][1]
                # Se obtiene el segundo indice
                indice2 = lista_partidas_dificiles[ind][index][2]
                # Se llena la casilla con el valor
                # Esto se hace en la posicion segun los indices
                board[indice1][indice2] = str(valor3)


        # Crear los botones
        # Se crea una lista que contenga los indices de los botones que son fijos
        lista_indices = []

        fila_pos = 200
        columna_pos = 150
        boton = 0
        x = 0
        y = 0

        for fila in range(0,5):

            for columna in range(0,5):
                             

                lista_botones[boton].place(x = fila_pos, y = columna_pos)

                if board[x][y] == "":
                    lista_botones[boton].config(text = "")

                if board[x][y] != "":
                    lista_botones[boton].config(text = board[x][y])
                    # Se agrega el indice del boton fijo a la lista
                    lista_indices += [boton]
                # Se ponen en negrita solo aquellos que sean fijos
                if boton in lista:
                    lista_botones[boton].config(font=("Calibri (Body)", 9, BOLD))
                    
                boton += 1
                y += 1
                fila_pos += 72

            x += 1
            y = 0
            columna_pos += 72
            fila_pos = 200

        # Se imprimen las restricciones segun el indice
        if ind == 0:
            restriccion_dificil(ind, jugar)

        if ind == 1:
            restriccion_dificil(ind, jugar)

        if ind == 2:
            restriccion_dificil(ind, jugar)

    f3.close()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Funcion que pasa el tiempo del reloj normal a segundos
def pasar_tiempo(tiempo):

    # Se divide el tiempo en partes y se transforma todo a segundos
    horas = int(tiempo[0:2]) * 3600
    minutos = int(tiempo[3:5]) * 60
    segundos = int(tiempo[6:8])

    tiempo_total = horas + minutos + segundos

    return tiempo_total

# Funcion que pasa el tiempo del timer a segundos
def pasar(tiempo):

    # Se obtiene el tiempo en segundos que puso el usuario en el timer
    tiempo1 = pasar_tiempo(tiempo_timer)

    # Se obtiene el tiempo de finalizacion en segundos
    tiempo2 =  pasar_tiempo(tiempo)

    tiempo_final = tiempo1 - tiempo2

    return tiempo_final
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Funcion que devuelve el tiempo que duro
# el usuario en terminar el juego con timer
def timer_time(tiempo):


    # Se sacan los numeros segun el dato de entrada
    horas = tiempo//3600
    t1 = horas*3600
    t2 = tiempo- t1
    minutos = t2 // 60
    t3 = minutos * 60
    segundos = t2 - t3

    # Se forma el string
    string = ""

    # Si las horas son menor que 10 se le agrega un 0 al inicio
    if horas < 10:
        horas = str(0)+str(horas)
    # De lo contario h continua igual
    else:
        horas = str(horas)

    # Si los minuto son menores que 10 se le agrega un 0 al inicio
    if minutos < 10:
        minutos = str(0)+str(minutos)
    # De lo contario m continua igual    
    else:
        minutos = str(minutos)

    # Si los segundos son menores que 10 se le agrega un 0 al inicio
    if segundos < 10:
        segundos = str(0)+str(segundos)
    # De lo contario s continua igual   
    else:
        segundos = str(segundos)

    # Se unen de nuevo los numeros
    string = horas + ":" + minutos + ":" + segundos

    return string
    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def decidir_top(tiempo_final):

    # Se abre el archivo
    top10 = open("futoshiki2020top10.dat","rb")

    # Se sacan las listas del archivo
    top_10_facil = pickle.load(top10)
    top_10_intermedio = pickle.load(top10)
    top_10_dificil = pickle.load(top10)



    # Reloj Normal
    if reloj.get() == 1:

        # Se pasa el tiempo a segundos
        t_en_segundos = pasar_tiempo(tiempo_final)

        # El tiempo es igual al tiempo final debido a que
        # es el que se debe colocar en la ventana del top 10
        tiempo = tiempo_final

    # Timer
    if reloj.get() == 3:

        # Se pasa el tiempo a segundos
        t_en_segundos = pasar(tiempo_final)

        # Se determina el tiempo que se va a colocar en el top 10
        tiempo = timer_time(t_en_segundos)

    # Depende del nivel se alteran los datos para llamar a la funcion
    if nivel.get() == 1:

        # Se modifica la lista para colocar el nuevo record
        lista =  decidir_aux(tiempos_facil, t_en_segundos, 0, tiempo)

        # Se obtiene lista con nombres del nivel facil
        lista_nombres = ln(top_10_facil)

        return arreglar_top(lista, 1, lista_nombres)
        
    if nivel.get() == 2:

        # Se modifica la lista para colocar el nuevo record
        lista =  decidir_aux(tiempos_intermedio, t_en_segundos, 0, tiempo)

        lista_nombres = ln(top_10_intermedio)

        return  arreglar_top(lista, 2, lista_nombres)

    if nivel.get() == 3:

        # Se modifica la lista para colocar el nuevo record
        lista = decidir_aux(tiempos_dificil, t_en_segundos, 0, tiempo) 

        lista_nombres = ln(top_10_dificil)

        return arreglar_top(lista, 3, lista_nombres)
        
    top10.close()

# Funcion que da los nombres del top 10 de n nivel
def ln(lista):
    resultado = []
    for  i in range(len(lista)):

        resultado += [lista[i][0]]
    return resultado


"""----------------------------RECURSION TOP 10---------------------------------"""

# Funcion que modifica la lista de tiempos de cada nivel
# para colocar el nuevo record
def decidir_aux(lista, tiempo, contador, tiempo_string):

    # Caso base 1
    if contador == len(lista):

        return lista

    # Caso base 2: el tiempo es mayor que la
    # ultima posicion
    if tiempo > lista[-1][1]:

        return lista

    
    # Se determina en que posicion debe colocarse
    if lista[contador][1] > tiempo:
   
        # Se quita el ultimo elemento
        lista.pop()
        name = nombre_jugador.get()
        # Se inserta el elemento
        lista.insert(contador, (name, tiempo_string))
        
        return lista

    # Llamada recursiva, se aumenta contador
    return decidir_aux(lista, tiempo, contador + 1, tiempo_string)


# Funcion que modifica la lista del top 10
# para colocar el nuevo record
def arreglar_top(lista, nivel, lista_nombres):

    # Se abre el archivo
    top10 = open("futoshiki2020top10.dat","rb")

    # Se sacan las listas del archivo
    top_10_facil = pickle.load(top10)
    top_10_intermedio = pickle.load(top10)
    top_10_dificil = pickle.load(top10)

    # Facil
    if nivel == 1:

        return arreglar_toop_aux(0, lista, top_10_facil, lista_nombres)

    # Intermedio
    if nivel == 2:
                
                
        return arreglar_toop_aux(0, lista, top_10_intermedio, lista_nombres)

    # Dificil
    if nivel == 3:

        return arreglar_toop_aux(0, lista, top_10_dificil, lista_nombres)       
                
    
    # Se cierra el archivo
    top10.close()

def arreglar_toop_aux(contador, lista, top, lista_nombres):

    if contador == len(top):

        return top

    if not(lista[contador][0] in lista_nombres):
        top.pop()
        top.insert(contador, lista[contador])
        
    return arreglar_toop_aux(contador + 1, lista, top, lista_nombres)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def update():
    
    # Se abre el archivo
    top10 = open("futoshiki2020top10.dat","rb")

    global top_10_facil, top_10_intermedio, top_10_dificil
    # Se sacan las listas del archivo
    top_10_facil = pickle.load(top10)
    top_10_intermedio = pickle.load(top10)
    top_10_dificil = pickle.load(top10)

    top10.close()

    # Se determina la lista con tiempos
    crea_tiempos()

    # Se actualiza el top 10
    top_actual = decidir_top(tiempo_final)

    # Nivel Facil
    if nivel.get() == 1:

        # Si hubo un cambio en el top facil
        # se actualiza
        if top_actual != top_10_facil:
            
            top_10_facil = top_actual

    # Nivel Intermedio
    if nivel.get() == 2:

        # Si hubo un cambio en el top intermedio
        # se actualiza
        if top_actual != top_10_intermedio:

            top_10_intermedio = top_actual

    # Nivel Dificil
    if nivel.get() == 3:

        # Si hubo un cambio en el top dificil
        # se actualiza
        if top_actual != top_10_dificil:

            top_10_dificil = top_actual
    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def open_top():

    top = Tk()
    top.title("Top 10")
    
    TopFrame = Frame(top, width = 500, height= 700)
    TopFrame.pack()
    top.resizable(0,0)
    Label(TopFrame, text="Top 10", bg="gold", fg="white",font=("Copperplate Gothic Bold",30),
              bd=1, relief="solid").place(x=170, y=0)

    Label(TopFrame, text = "Nivel facil", bg = "gold", font=("Copperplate Gothic Bold",12),
          bd = 1, relief="solid").place(x=20, y=100)

    Label(TopFrame, text = "Nivel Intermedio", bg = "gold", font=("Copperplate Gothic Bold",12),
          bd = 1, relief="solid").place(x=20, y=390)

    Label(TopFrame, text = "Nivel Dificil", bg = "gold", font=("Copperplate Gothic Bold",12),
          bd = 1, relief="solid").place(x=250, y=100)

    boton_imprimir = Button(TopFrame, text="IMPRIMIR\n TOP", bg= "gold",
                       font=("Aharoni",10))
    boton_imprimir.place(x=380, y=640, height=50, width=100)
    
    # Se imprimen los jugadores
    
    """TOP 10 FACIL"""
    x_pos = 30
    y_pos = 130
    no = 1
    for i in range(len(top_10_facil)):
        numero = str(no) + "." + "  "
        nombre = str(top_10_facil[i][0]) + "  "
        tiempo = str(top_10_facil[i][1])
        jugador = Label(TopFrame, text = numero + nombre + tiempo, font=("Arial",12)
                  ).place(x = x_pos, y = y_pos)
        y_pos += 25
        no += 1
        
    """TOP 10 INTERMEDIO"""
    x_pos = 30
    y_pos = 420
    no = 1
    for i in range(len(top_10_intermedio)):
        numero = str(no) + "." + "  "
        nombre = str(top_10_intermedio[i][0]) + "  "
        tiempo = str(top_10_intermedio[i][1])
        jugador = Label(TopFrame, text = numero + nombre + tiempo, font=("Arial",12)
                  ).place(x = x_pos, y = y_pos)
        y_pos += 25
        no += 1

    """TOP 10 DIFICIL"""
    x_pos = 250
    y_pos = 130
    no = 1
    for i in range(len(top_10_dificil)):
        numero = str(no) + "." + "  "
        nombre = str(top_10_dificil[i][0]) + "  "
        tiempo = str(top_10_dificil[i][1])
        jugador = Label(TopFrame, text = numero + nombre + tiempo, font=("Arial",12)
                  ).place(x = x_pos, y = y_pos)
        y_pos += 25
        no += 1
        
    # Se cierra el archivo
    top10.close()
    
    top.mainloop()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def iniciar2():

    global juego_iniciado
    juego_iniciado = True

    try:
        
        if nombre_registrado == False:
            messagebox.showinfo(message = 'Debe introducir el nombre del jugador')
        
    except NameError:
        messagebox.showinfo(message = 'Debe introducir el nombre del jugador')


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def botones_principales(lugar, board):

    if reloj.get() == 2:

        boton_iniciar2 = Button(lugar, text="INICIAR\n JUEGO", bg= "VioletRed1",
                           font=("Aharoni",10), command = iniciar2).place(x = 50, y = 500, height=50, width=100)

        # Se agrega boton top 10
        boton_top2 = Button(lugar, text="TOP\n 10", bg= "gold",
                    font=("Aharoni",10), command= open_top).place(x = 530, y = 500, height=50, width=100)
    
        # Se agrega boton borrar jugada
        boton_borrar_jugada = Button(lugar, text="BORRAR\n JUGADA", bg= "SkyBlue1",
                       font=("Aharoni",10), command = lambda: borrar_jugada(board))
        boton_borrar_jugada.place(x=170, y=500, height=50, width=100)

        # Se agrega boton rehacer jugada
        boton_rehacer_jugada = Button(lugar, text="REHACER\n JUGADA", bg= "coral1",
                       font=("Aharoni",10), command = lambda: rehacer_jugada(board))
        boton_rehacer_jugada.place(x=650, y=500, height=50, width=100)


        # Se agrega boton terminar juego
        boton_terminar = Button(lugar, text="TERMINAR\n JUEGO", bg= "pale green",
                       font=("Aharoni",10), command = terminar_juego)
        boton_terminar.place(x=290, y=500, height=50, width=100)

        # Se agrega boton borrar juego
        boton_borrar_juego = Button(lugar, text="BORRAR\n JUEGO", bg= "MediumPurple1",
                       font=("Aharoni",10), command = clicked_borrar)
        boton_borrar_juego.place(x=410, y=500, height=50, width=100)

        # Se agrega boton guardar juego
        boton_guardar = Button(lugar, text="Guardar Juego",font=("Aharoni",10), command = lambda: guardar(board))
        boton_guardar.place(x=300, y=600, width=150)

        # Se agrega boton cargar juego
        boton_cargar = Button(lugar, text="Cargar Juego",font=("Aharoni",10), command = cargar)
        boton_cargar.place(x=500, y=600, width=150)

        # Solucionar juego
        solucion = Button(lugar, text="SOLUCIONAR\n JUEGO", bg= "LightPink1",
                       font=("Aharoni",10))
        solucion.place(x=650, y=80, height=50, width=100)

    else:
        
        # Se agrega boton borrar jugada
        boton_borrar_jugada = Button(lugar, text="BORRAR\n JUGADA", bg= "SkyBlue1",
                       font=("Aharoni",10), command = lambda: borrar_jugada(board))
        boton_borrar_jugada.place(x=170, y=500, height=50, width=100)

        # Se agrega boton rehacer jugada
        boton_rehacer_jugada = Button(lugar, text="REHACER\n JUGADA", bg= "coral1",
                       font=("Aharoni",10), command = lambda: rehacer_jugada(board))
        boton_rehacer_jugada.place(x=650, y=500, height=50, width=100)

        # Se agrega boton terminar juego
        boton_terminar = Button(lugar, text="TERMINAR\n JUEGO", bg= "pale green",
                       font=("Aharoni",10), command = terminar_juego)
        boton_terminar.place(x=290, y=500, height=50, width=100)

        # Se agrega boton borrar juego
        boton_borrar_juego = Button(lugar, text="BORRAR\n JUEGO", bg= "MediumPurple1",
                       font=("Aharoni",10), command = clicked_borrar)
        boton_borrar_juego.place(x=410, y=500, height=50, width=100)

        # Se agrega boton guardar juego
        boton_guardar = Button(lugar, text="Guardar Juego",font=("Aharoni",10), command = lambda: guardar(board))
        boton_guardar.place(x=300, y=600, width=150)

        # Se agrega boton cargar juego
        boton_cargar = Button(lugar, text="Cargar Juego",font=("Aharoni",10), command = cargar)
        boton_cargar.place(x=500, y=600, width=150)

        solucion = Button(lugar, text="SOLUCIONAR\n JUEGO", bg= "LightPink1",
                       font=("Aharoni",10))
        solucion.place(x=650, y=80, height=50, width=100)
    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def imprimir_botones(ind, board, nivel):

    # PARTIDAS FACILES
    f = open("futoshiki2020partidasfaciles.dat", "rb")
    if nivel == 1:

        lista_partidas_faciles = pickle.load(f)

        # Se llena la matriz board
        for j in lista_partidas_faciles[ind]:

            if j[0] == "v" or j[0] == "^" or\
               j[0] == ">" or j[0] == "<":

                pass
                
            else:
                index = lista_partidas_faciles[ind].index(j)
                # Se obtiene el numero que hay que colocar en la casilla
                valor1 = int(lista_partidas_faciles[ind][index][0])
                # Se obtiene el primer indice
                indice1 = lista_partidas_faciles[ind][index][1]
                # Se obtiene el segundo indice
                indice2 = lista_partidas_faciles[ind][index][2]
                # Se llena la casilla con el valor
                # Esto se hace en la posicion segun los indices
                board[indice1][indice2] = str(valor1)


        # Se imprimen los botones
        # Se crea una lista que contenga los indices de los botones que son fijos
        global lista_indices
        lista_indices = []
        fila_pos = 200
        columna_pos = 150
        boton = 0
        x = 0
        y = 0
        for fila in range(0,5):
            for columna in range(0,5):
                             

                lista_botones[boton].place(x = fila_pos, y = columna_pos)

                if board[x][y] == "":
                    lista_botones[boton].config(text = "")

                if board[x][y] != "":
                    lista_botones[boton].config(text = board[x][y], font=("Calibri (Body)", 9, BOLD))
                    # Se agrega el indice del boton fijo a la lista
                    lista_indices += [boton]
                                                
                boton += 1
                y += 1
                fila_pos += 72

            x += 1
            y = 0
            columna_pos += 72
            fila_pos = 200

        # Se imprimen las restricciones segun el indice
        if ind == 0:
           restriccion_facil(ind, jugar)
            
        if ind == 1:
            restriccion_facil(ind, jugar)
            
        if ind == 2:
            restriccion_facil(ind, jugar)

    f.close()

    # PARTIDAS INTERMEDIAS

    f2 = open("futoshiki2020partidasintermedias.dat","rb")
    
    if nivel == 2:

        
        lista_partidas_intermedias = pickle.load(f2)

        for j in lista_partidas_intermedias[ind]:

            if j[0] == "v" or j[0] == "^" or\
               j[0] == ">" or j[0] == "<":

                pass
                
            else:
                index = lista_partidas_intermedias[ind].index(j)
                # Se obtiene el numero que hay que colocar en la casilla
                valor2 = int(lista_partidas_intermedias[ind][index][0])
                # Se obtiene el primer indice
                indice1 = lista_partidas_intermedias[ind][index][1]
                # Se obtiene el segundo indice
                indice2 = lista_partidas_intermedias[ind][index][2]
                # Se llena la casilla con el valor
                # Esto se hace en la posicion segun los indices
                board[indice1][indice2] = str(valor2)

        # Se crea una lista que contenga los indices de los botones que son fijos
        lista_indices = []

        fila_pos = 200
        columna_pos = 150
        boton = 0
        x = 0
        y = 0

        for fila in range(0,5):
            for columna in range(0,5):
                             

                lista_botones[boton].place(x = fila_pos, y = columna_pos)

                if board[x][y] == "":
                    lista_botones[boton].config(text = "")

                if board[x][y] != "":
                    lista_botones[boton].config(text = board[x][y], font=("Calibri (Body)", 9, BOLD))
                    # Se agrega el indice del boton fijo a la lista
                    lista_indices += [boton]
                                                
                boton += 1
                y += 1
                fila_pos += 72

            x += 1
            y = 0
            columna_pos += 72
            fila_pos = 200
        
        # Se imprimen las restricciones segun el indice
        if ind == 0:   
            restriccion_intermedio(ind, jugar)

        if ind == 1:
            restriccion_intermedio(ind, jugar)

        if ind == 2:
            restriccion_intermedio(ind, jugar)


    f2.close()


    # PARTIDAS DIFICILES
    
    f3 = open("futoshiki2020partidasdificiles.dat","rb")
    
    if nivel == 3:

        
        lista_partidas_dificiles = pickle.load(f3)

        for j in lista_partidas_dificiles[ind]:

            if j[0] == "v" or j[0] == "^" or\
               j[0] == ">" or j[0] == "<":

                pass
                
            else:
                index = lista_partidas_dificiles[ind].index(j)
                # Se obtiene el numero que hay que colocar en la casilla
                valor3 = int(lista_partidas_dificiles[ind][index][0])
                # Se obtiene el primer indice
                indice1 = lista_partidas_dificiles[ind][index][1]
                # Se obtiene el segundo indice
                indice2 = lista_partidas_dificiles[ind][index][2]
                # Se llena la casilla con el valor
                # Esto se hace en la posicion segun los indices
                board[indice1][indice2] = str(valor3)


        # Crear los botones
        # Se crea una lista que contenga los indices de los botones que son fijos
        lista_indices = []

        fila_pos = 200
        columna_pos = 150
        boton = 0
        x = 0
        y = 0

        for fila in range(0,5):

            for columna in range(0,5):
                             

                lista_botones[boton].place(x = fila_pos, y = columna_pos)

                if board[x][y] == "":
                    lista_botones[boton].config(text = "")

                if board[x][y] != "":
                    lista_botones[boton].config(text = board[x][y], font=("Calibri (Body)", 9, BOLD))
                    # Se agrega el indice del boton fijo a la lista
                    lista_indices += [boton]
                                                
                boton += 1
                y += 1
                fila_pos += 72

            x += 1
            y = 0
            columna_pos += 72
            fila_pos = 200

        # Se imprimen las restricciones segun el indice
        if ind == 0:
            restriccion_dificil(ind, jugar)

        if ind == 1:
            restriccion_dificil(ind, jugar)

        if ind == 2:
            restriccion_dificil(ind, jugar)

    f3.close()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def posibles_jugadas(fila, columna, board):

    # Lista que va a contener todos los elementos
    # de la fila y columna del boton que se presiono
    lista1 = []
    # Lista que va a contener posibles jugadas
    lista_posibles = ['1','2','3','4','5']

    # Saca los elementos de la fila

    for i in board[fila]:

        # Si no esta vacio se agrega
        if i != '':
            lista1 += [i]

    # Se sacan los elementos de la columna
    indice = 0
    for j in board:

        if board[indice][columna] != '':

            lista1 += [board[indice][columna]]

        indice += 1

    # Se elimina los numeros que no se pueden colocar
    for k in lista1:

        if k in lista_posibles:

            indice2 = lista_posibles.index(k)

            del lista_posibles[indice2]

    return lista_posibles


def jugadas(fila, columna, board):

    lista = posibles_jugadas(fila, columna, board)

    texto_jugadas = texto(lista)

    Label(jugar, text= texto_jugadas, bg = "light cyan").place(x=600, y=150)

# Funcion que devuelve lista como string
def texto(lista):

    resultado = ''
    for i in range(len(lista)):

        resultado += str(lista[i]) + ','

    return resultado

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Funcion para obtener la columna de una matriz  
def obtener_columna(board, numero):
    # Se obtiene la columna
    columna = [fila[numero] for fila in board]
    return columna

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

n = 1
def open_jugar(n):

    
    # Se valida que el usuario haya revisado las configuraciones, ya que
    # si esto no se valida entonces el juego no se va a imprimir de la manera
    # correcta
    if entro_configurar == False:
        messagebox.showinfo(message = 'Revise primero las configuraciones')

    # Si el usuario ya reviso la configuracion entonces se ejecuta todo
    if entro_configurar == True:

        global jugar

        jugar = Toplevel()
        
        # Tamaño
        miFrame = Frame(jugar, width = 800, height= 700)
        miFrame.pack()

        # El usuario no va a poder modificar el tamaño
        jugar.resizable(0,0)

        board = [["","","","",""],
                ["","","","",""],
                ["","","","",""],
                ["","","","",""],
                ["","","","",""]
                ]
        
        # Se agrega el nombre del juego
        Label(miFrame, text="Futoshiki", bg="red", fg="white",font=("Copperplate Gothic Bold",30),
              bd=1, relief="solid").place(x=300, y=0)

        # Labels
        
        # Se agrega la entrada del nombre del jugador
        global nombre_jugador
        nombre_jugador = Entry(jugar)
        nombre_jugador.place(x=250, y=100, width=300)

        # Se agrega texto
        nombreLabel= Label(jugar,text="Nombre del jugador:")
        nombreLabel.place(x=100,y=100)

        # Boton que de aceptar al nombre
        nombre_boton = Button(jugar, text="OK", bg= "lavender", font=("Aharoni",10), command= nombre)
        nombre_boton.place(x= 570, y = 98, height=25, width=25)    

        # Se llama a la funcion que imprime los botones principales
        botones_principales(jugar, board)

        
        # Se llama a la funcion que imprime los digitos dependiendo de la configuracion
        digitos(posicion.get(), jugar)

        # Se crea una variable para el reloj
        reloj2 = reloj.get()

        if reloj.get() == 1 or\
           reloj.get() == 3:
            
            # Se determina el tiempo
            tiempo(jugar, reloj2, '00:00:00')

        # Se imprimen las casillas
        casillas(jugar, board, False)
        
        # Se saca el indice de manera aleatoria
        global ind
        ind = random.randint(0,2)

        if nivel.get() == 4:
            global multi
            multi = 0
            imprimir_botones(ind, board, n)

        else:
            global nivel2
            nivel2 = nivel.get()
            # Se imprimen los botones
            imprimir_botones(ind, board, nivel2)
        
        print(board)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   
def abrir():
    wb.open_new(r'C:\Users\vchin\Dropbox\TEC\intro y taller\proyecto2.pdf')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
def open_ayuda():
    
    wb.open_new(r'C:\Users\vchin\Dropbox\TEC\intro y taller\MANUAL DE USUARIO.pdf')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def open_acerca():
    
    acerca = Toplevel()
    lbl = Label(acerca, text = "Acerca", bg="medium aquamarine", fg="white",font=("Aharoni",30),
      bd=1, relief="solid").pack()
    
    # Titulo
    acerca.title("Acerca")

    # Tamaño
    miFrame4 = Frame(acerca, width = 800, height= 500)
    miFrame4.pack()

    # Texto
    lbl1 = Label(acerca, text = "Futoshiki", font=("Aharoni",12))
    lbl1.place(x = 10, y= 125)
    
    lbl2 = Label(acerca, text = "Version: 1", font=("Aharoni",12))
    lbl2.place(x = 10, y= 150)
    
    lbl3 = Label(acerca, text = "Fecha de creacion: Martes, ‎June ‎30, ‎2020, ‏‎1:47:31 PM", font=("Aharoni",12))
    lbl3.place(x = 10, y= 175)

    lbl4 = Label(acerca, text = "Autor: Valeria Chinchilla Mejias", font=("Aharoni",12))
    lbl4.place(x = 10, y= 200)
    
    # Boton para salir
    btn5 = Button(acerca, text = "Salir", command = acerca.destroy)
    btn5.place(x = 750, y = 0)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def principal():
    
    ventana = Tk()

    ventana.title("Menú Principal")

    # Tamaño
    miFrame = Frame(ventana, width = 800, height= 600)
    miFrame.pack()
    ventana.resizable(0,0)
        
    # Se agrega el nombre del juego
    Label(miFrame, text="Futoshiki", bg="light coral", fg="white",font=("Copperplate Gothic Bold",30),
          bd=1, relief="solid").place(x=300, y=0)
    # Botones


    # Jugar
    boton_jugar = Button(ventana, text = "Jugar",bg= "pale green", command = lambda: open_jugar(n))
    # Se agrega
    boton_jugar.place(x = 80, y = 150, width = 300, height = 100)

    # Configurar
    boton_configurar = Button(ventana, text = "Configurar", bg= "light sky blue", command = open_configurar)
    # Se agrega
    boton_configurar.place(x = 450, y = 150, width = 300, height = 100)

    # Ayuda
    boton_ayuda = Button(ventana, text = "Ayuda", bg= "plum2", command = open_ayuda)
    # Se agrega
    boton_ayuda.place(x = 80, y = 300, width = 300, height = 100)

    # Acerca De
    boton_acerca = Button(ventana, text = "Acerca De", bg= "medium aquamarine", command = open_acerca)
    # Se agrega
    boton_acerca.place(x = 450, y = 300, width = 300, height = 100)

    # Salir
    boton_salir = Button(ventana, text = "Salir", bg= "pink1", command = ventana.destroy)
    # Se agrega
    boton_salir.place(x = 250, y = 450, width = 300, height = 100)

    ventana.mainloop()

principal()
