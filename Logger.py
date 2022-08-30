# This is a logger
# every line you add
# gets added to a file
# in this case is called log.txt
# and to exit you need to write exit
# 

datawr = input("Data log: ")
while True:
    if datawr == "exit" or datawr == "quit":
        break
    else:
        f = open("log.txt", "a")
        f.write(datawr + "\n")
        f.close()    
        datawr = input("Data log: ")


