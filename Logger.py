#Logger

datawr = input("Data log: ")
while True:
    if datawr == "exit" or datawr == "quit":
        break
    else:
        f = open("log.txt", "a")
        f.write(datawr + "\n")
        f.close()    
        datawr = input("Data log: ")


