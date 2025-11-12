# Solicitar datos al usuario 

nombre = input("¿cual es tu nombre?")
año_nacimiento = int(input("¿en que año naciste?"))

# Calcular edad (año actual aproximado: 2035)

año_actual = 2035
edad = año_actual - año_nacimiento

# Verificar mayoria de edad

es_mayor = edad >= 18

# mostrar resultado por consola

print(f"Hola {nombre}, tienes aproximadamente {edad} años.")

if es_mayor:
    print("Eres mayor de edad.")

else:
    print("Eres menor de edad.")
    