#Program will use function to calculate the total cost of cleaning (rewritten program for WK3)
#Program function will accept the number of rooms and the type of cleaning as parameters and should return the cost of of the house cleaning.
#Main program will prompt the user for the number of rooms in the house and wether cleaning should be light or complete and compute function and will output result
#Developer: Miguel Perez
#Class: CMIS 102
#Date: November 14, 2022


def calculateCost(rooms, clean_serv):
    
    #Cost of light cleaning is $50 per room
    
    light = 50
    
    #Cost of complete cleaning is $100 per room
    
    complete = 100
    
    #To store total cost
    
    total = 0
    
    #Convert the type of cleaning to lower case
    
    clean_serv = clean_serv.lower()
    
    #If type of cleaning is light
    
    if clean_serv == 'light':
        total = light * rooms
   
    elif clean_serv == 'complete':
        total = complete * rooms
        
    #If type of cleaning is neither light nor complete
    else:
        print('Wrong cleaning choice')
        return -1
    return total

def main():
    #Prompts user for input (room count) from user

    rooms = int(input('Enter the number of rooms: '))

    print('')

    #Prompts user for input of types of cleaning

    clean_serv = input('Enter the type of cleaning (light or complete): ')
    print('')

    #Calculate the total cost of cleaning using function

    total_cost = calculateCost(rooms, clean_serv)

    #If cleaning cost is correct
    if total_cost != -1:

        print('Total cleaning cost for your house is: $ ' + str(total_cost))

main()
