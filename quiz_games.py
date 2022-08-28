from time import sleep, time


print("Bienvenido a mi quiz!")

sleep(1)

playername = input("Como te llamas? ")

sleep(1)

is_playing = input("Ok " + playername + ", Quieres hacer este quiz? ")

sleep(1)

if is_playing.lower() != "si":
    quit()

print("Juguemos entonces!!")
pts = 0

# Pregunta 1
sleep(1)

answer = input("Cual es el nombre del programador? ")
print("Y la respuesta es...")
sleep(1)
if answer.lower() == "jesus":
    print("Correcta")
    pts += 1

else:
    print("Incorrecta")

# Pregunta 2
sleep(1)

answer = input("Cual es el color favorito del programador? ")
print("Y la respuesta es...")
sleep(1)
if answer.lower() == "verde":
    print("Correcta")
    pts += 1

else:
    print("Incorrecta")


# Pregunta 3
sleep(1)

answer = input("cuanto es la suma de 5+9? ")
print("Y la respuesta es...")
sleep(1)
if answer.lower() == "14":
    print("Correcta")
    pts += 1

else:
    print("Incorrecta")

# Pregunta 4
sleep(1)

answer = input("Cuanto es el valor de la gravedad? ")
print("Y la respuesta es...")
sleep(1)

if answer.lower() == "10":
    print("Correcta")
    pts += 1

else:
    print("Incorrecta")

sleep(1)
print ("Obtuviste " + str(pts) + " /4 puntos")

