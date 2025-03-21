segundos = int(input("Introduce el número de segundos: "))

# Convierte los segundos a horas, minutos y segundos

# Imprime el resultado en formato de horas, minutos y segundos

hs =int(segundos/3600)

restoh = ((-hs*3600)+segundos)

minutos = int(restoh/60)

restom = (-minutos*60+restoh)

print("horas: ",hs,"minutos: ",minutos,"segundos: ",restom)


