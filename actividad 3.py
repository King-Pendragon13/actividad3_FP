# Inicia el programa
suma = 0
continuar = 's'  # Variable de control para el bucle

while continuar.lower() == 's':
    # Solicita un número al usuario
    try:
        numero = float(input("Ingrese un número: "))
        suma += numero  # Sumar el número ingresado a la suma total
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue  # Vuelve a solicitar el número si hay un error

    # Preguntar si desea continuar
    continuar = input("¿Desea ingresar otro número? (s/n): ")

# Mostrar el resultado final
print(f"La suma total de los números ingresados es: {suma}")
