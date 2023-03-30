numeros_premiados = []  #creamos la lista vacia

for i in range(6):

    numero = int(input(f"Ingrese el número ganador {i+1}: "))

    numeros_premiados.append(numero)

numeros_premiados.sort()   #funcion para ordenar los numeros 

numeros_premiados = [str(numero) for numero in numeros_premiados]

separados = ",".join(numeros_premiados)

print("Los números ganadores son:", separados, "felicudades si fuieste uno de los ganadores ")
