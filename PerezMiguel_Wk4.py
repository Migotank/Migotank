#Program will calculate the average speed of two trains 
#Developer: Miguel Perez
#Class: CMIS 102
#Date: November 10, 2022

def main():
    #Prompt user for two numerical values
    
    train1 = int(input("Enter the speed of the first train in MPH: \n "))
    print('')
    train2 = int(input("Enter the speed of second train in MPH: \n "))

    def averageSpeed(trian1, train2):
        #Calculate average speed from input
        print('')
        average = (train1+train2)/2;
        return average
    
    #Display the result

    print("The average speed of the two trains is ", averageSpeed(train1, train2)," mph")

main()
