materias = []  #cremos lista vacia 

for i in range(5):
    materia = input("Ingrese el nombre de la primera materia: ") #input es para pedir datos al usuario
    materias.append(materia)    #append para terminar la lista 

print("Yo estoy estudiando:")

for materia in materias:
    print(materia)

notas = {}

for materia in materias:
    nota = input(f"Ingrese su nota en orden de materias solicitadas  {materia}: ")
    notas[materia] = nota

for materia, nota in notas.items():
    print(f"En {materia} has sacado {nota}")


repetir = []

for materia, nota in notas.items():
    if int(nota) > 70:
        repetir.append(materia)
    else:
        materias.remove(materia)

print("Materias que has aprobado:")
for materia in materias:
    print(materia)

if repetir:
    print("Materias que tienes que repetir:")
    for materia in repetir:
        print(materia)
else:
    print("No tienes materias para repetir. ¡Felicidades campeon!")
