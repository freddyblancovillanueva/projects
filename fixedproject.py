empleados = []
clientes = []
trabajos = []
# esta funciones son para el ingresado de los empleados 
def ingresar_empleado():
    nombre = input("Nombre del empleado: ")
    especialidad = input("Especialidad del empleado: ")
    sexo = input("Sexo del empleado: ")
    empleados.append({'nombre': nombre, 'especialidad': especialidad, 'sexo del empleado': sexo})
    print("Empleado ingresado exitosamente")
def borrar_empleado():
    nombre = input("Nombre : ")
    for empleado in empleados:
        if empleado['nombre'] == nombre:
            empleados.remove(empleado)
            print("Empleado borrado correctamente")
            return
    print("El empleado que buscas no encontrado")
def ver_empleados():
    print("Lista de empleados:")
    for empleado in empleados:
        print("Nombre: {}, Especialidad: {}, Sexo: {}".format(empleado['nombre'], empleado['especialidad'], empleado['sexo']))
def ingresar_cliente():
    nombre = input("Nombre del cliente: ")
    cedula = input("Cédula del cliente: ")
    telefono = input("Teléfono del cliente : ")
    clientes.append({'nombre': nombre, 'cedula': cedula, 'telefono': telefono})
    print("Cliente ingresado correctamente")
def modificar_cliente():
    nombre = input("Nombre del cliente a modificar: ")
    for cliente in clientes:
        if cliente['nombre'] == nombre:
            cliente['cedula'] = input("Nueva cédula: ")
            cliente['telefono'] = input("Nuevo número de teléfono: ")
            print("Cliente ha sido modificado exitosamente")
            return 
    print("Los datos ingresados no son correctos ")
def ver_clientes():
    print("Lista de clientes:")
    for cliente in clientes:
        print("Nombre: {}, Cédula: {}, Teléfono: {}".format(cliente['nombre'], cliente['cedula'], cliente['telefono']))
def brindar_servicio():
    fecha = input("Fecha del trabajo: ")
    cliente = input("Nombre del cliente: ")
    servicio = input("Servicio a realizar: ")
    empleado = input("Nombre del empleado que realizará el trabajo: ")
    trabajos.append({'fecha': fecha, 'cliente': cliente, 'servicio': servicio, 'empleado': empleado})
    print("Fecha de trabajo ingresada exitosamente")
def ver_servicios():
    print("Lista de trabajos realizados:")
    for trabajo in trabajos:                                       #format es un tipo de cadena
        print("Fecha: {}, Cliente: {}, Servicio: {}, Empleado: {}".format(trabajo['fecha'], trabajo['cliente'], trabajo['servicio'], trabajo['empleado']))
def empleado_disponible():
    especialidad = input("Especialidad que busca: ")
    disponibles = []
    for empleado in empleados:
        if empleado['especialidad'] == especialidad:
            trabajando = False
            for trabajo in trabajos:
                if trabajo['empleado'] == empleado['nombre']:
                    trabajando = True
                    break
            if not trabajando:
                disponibles.append(empleado['nombre'])
    if len(disponibles) > 0:
        print("Empleados disponibles:")
        for empleado in disponibles:
            print(empleado)
    else:
        print("No hay empleados disponibles para esa especialidad.")
while True:
    print("*******************bienvenido a maridos de alquiler**********************")
    print("  aqui se le muestra las opciones  ")
    print ("menu 1 ")
    print("1. Ingresar empleado")
    print("2. Borrar empleado")
    print("3. Ver empleados")
    print ("menu 2")
    print("4. Ingresar cliente")
    print("5. Modificar cliente")
    print("6. Ver clientes")
    print ("menu 3")
    print("7. Brindar servicio")
    print("8. Ver trabajos realizados")
    print("9. Ver empleados disponibles")
    print("10. Salir")
    opcion = input("que desea realizar: ")
    if opcion == "1":
        ingresar_empleado()
    elif opcion == "2":
        borrar_empleado()
    elif opcion == "3":
        ver_empleados()
    elif opcion == "4":
        ingresar_cliente()
    elif opcion == "5":
        modificar_cliente()
    elif opcion == "6":
        ver_clientes()
    elif opcion == "7":
        brindar_servicio()
    elif opcion == "8":
        ver_servicios()
    elif opcion == "9":
        empleado_disponible()
    elif opcion == "10":
        print("gracias por usar nuestros servicios")
        break
    else:
        print("esta opcion no existe ")
        

        #codigo comentado aqui 
        
  #profe el codigo  no me compilaba
  #entonces use la IA para fixear el problema 
  #no pude ordenar el menu en de primero 
  #tampoco pude aplicar los diccionarios bien
  #si la sintaxis no era asi avisame para aserla bien ya que no entendi muy claro la idea 
  #funciones para los clientes
  # tambien use tipo de cadena format 
  #corchetes como marcadores de valor
  #un bucle para el menu principal