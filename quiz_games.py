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

answer = input("Nombre del programador? ")
print("Y la respuesta es...")
sleep(1)
if answer.lower() == "jesus":
    print("Correcta")
    pts += 1

else:
    print("Incorrecta")

# Pregunta 2
sleep(1)

answer = input("Cual es mi color favorito? ")
print("Y la respuesta es...")
sleep(1)
if answer.lower() == "verde":
    print("Correcta")
    pts += 1

else:
    print("Incorrecta")


# Pregunta 3
sleep(1)

answer = input("Como se llama mi esposa? ")
print("Y la respuesta es...")
sleep(1)
if answer.lower() == "maria":
    print("Correcta")
    pts += 1

else:
    print("Incorrecta")

# Pregunta 4
sleep(1)

answer = input("Cual es el nombre de mi hijo? ")
print("Y la respuesta es...")
sleep(1)

if answer.lower() == "juan":
    print("Correcta")
    pts += 1

else:
    print("Incorrecta")

sleep(1)
print ("Tienes " + str(pts) + " /4 puntos")