#Program will prompt user for the number of rooms in the house and type of cleaning.
#Program should output the cost of the house cleaning based on the number of rooms and the type of cleaning.
#Program program will output the cost of the house cleaning based on the number of rooms and the type of cleaning.
#Program will also define the cutoffs for what constitutes a small, medium and large number of rooms
#Developer: Miguel Perez
#Class: CMIS 102
#Date: November 07, 2022

def main():


    #Defining the cutoffs for what constitutes a small, medium, and large number of rooms
    
    small = 3
    medium = 4
    large = 5

    #Cost of house cleaning and two different cleanings offered (Standard, Dusting, and Windows.)
    
    standcleaning = 40
    dusting = 30
    windows = 20

    #---Prompts user for number of rooms in house and type of cleaning---
    
    #Prompt user for number of rooms

    rooms = eval(input("Please enter the number of rooms: \n "))
    print('')
 

    #Prompt user for type of service they desire

    print("What type of cleaning service would you like we offer: ")
    print("(1) standard clean")
    print("(2) dusting")
    print("(3) windows")
    print('')
    

    clean_serv = eval(input(" Please enter the number for type of cleaning you are interested in? 1, 2, or 3 \n"))

    #Output the cost of the house cleaning based on the number of rooms and the type of cleaning

    if clean_serv == 1:
        clean_cost = standcleaning
        if clean_serv == 2:
            clean_cost = dusting

    else:
        clean_cost = windows

    if rooms <= 3:
        total_cost = small * clean_cost
    elif rooms == 4:
        total_cost = medium * clean_cost
    elif rooms >= 5:
                total_cost = large * clean_cost

    print('')
    
    print(" The total cost to clean your house is $", total_cost)


    

main()
    
    


    
    
