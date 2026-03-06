#Codigo para Número más Grande (Overflow)
v = 1.0 # Vector inicio
contador = 0 # Contador de iteraciones

while v != float("inf"): #Ciclo While pa que opere HASTA que x sea igual a inf
    h = v # Guardo el valor anterior
    v = v * 2 # Multiplico por 2
    contador += 1 # contador para las veces que se repite el proceso

print(contador, h) # Imprimo el resultado en pantalla

# Codigo para el Número más pequeño. (Underflow)
x = 1.0 # Vector inicio
contador = 0 # Contador de iteraciones

while x != 0.0: #Ciclo While pa que opere HASTA que x sea igual a 0
    x = x / 2 # Divido por 2
    contador += 1 # contador para las veces que se repite el proceso
    if x == 0.0: # Condicional para que cuando sea 0 pare, diga que número da y cuantas veces se repitió el proceso
        print(contador, j) # Imprimo el resultado en pantalla
        break # Para
    else: # si no es cero guardo el valor
      j = x
