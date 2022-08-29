#Logger
def logger():
    file = open("log.txt", "w")
    file.write(datainput + "/n")
    file.close()

while True:
    datainput = input("Data log: ")
    if datainput == "exit" or "Exit":
        break
    else:
        file = open("log.txt", "w")
        file.write(datainput + "/n")
        file.close()
    