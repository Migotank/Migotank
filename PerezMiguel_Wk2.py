#Program that prompts the user and accepts at least two numeric values as input.
#Performs some computation with the two numbers and displays the result.
#Program will display the total of days and weeks are in a month (four weeks)
#Developer: Miguel Perez
#Class: CMIS 102
#Date: October 28, 2022


def main():
    #Prompt user for the number of days in a week
    Daysinwk = eval(input('How many days are in a week ? \n'))
    print('')

    #Prompt user for the number of weeks in a month
    WksinMon = int(input('How many weeks are in a month ? \n'))
    print('')

    #Compute how many days are in four weeks
    totaldays = 4 * (Daysinwk)
    print('')

    print('The total amount of days in four weeks is ', totaldays)

main()
