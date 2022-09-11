# This is a logger
# For every line you write and press enter
# The line gets written to a file
# In this case is called log.txt
# To exit the program you can write quit or exit


print("Hello, welcome to my logger.\n"+"this was made to save anything txt by only writting in it and pressing enter")

#Main data saver for 2 or more lines
def save_data():
    for i in input_lst:                    
            f = open("log.txt", "a")
            f.writelines(str(i))
            if input_lst[-1] != i:
                f.writelines(" | ")
            else:
                continue
    f = open("log.txt", "a")
    f.writelines("\n")
    f.close()    
    
# The starting point a infinite while loop
while True:
    datawr = input("Write anything to log in a file: ")
    input_lst = datawr.split()

    # This is the way to exit the program
    if datawr == "exit" or datawr == "quit": break
    
    # The loop for more than 2 words/numbers
    if len(input_lst) >= 2 :
        save_data() 
        continue
    
    # If not more then 2 words/numbers
    else:   
        f = open("log.txt", "a")
        f.write(datawr + "\n")
        f.close()
        continue    



