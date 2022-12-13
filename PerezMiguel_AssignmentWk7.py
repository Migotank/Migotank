#Program will collect all the data of a road trip and calculate each person's share of the cost.
#Prompt the user for the number of people on trip number of days and prompt the user for the number of days on trip
#Prompt the user for each day of the trip the cost of cost of food and the cost of gas
#Developer: Miguel Perez
#Class: CMIS 102
#Date: November 30, 2022


def main():
    # Welcome message

    print(" Welcome this program will collect all the data of your trip and help you calculate each person's share Current Currency for this trip is in USD $ ")
    print('')
    
    # Prompt the user for number of people on trip and days of the trip
    
    num_of_people = int(input("Please enter the number of people going on the trip: "))
    print('')

    num_of_days = int(input("Please enter the number of days of trip: "))
    print('')

    # Initialize

    l_food = []
    total_food = 0
    total_gas = 0

    # Prompt user for cost of Food per day of trip (1st Array)

    print("Enter the cost of Food per day of trip: ")
    print('')
    
    
    for i in range(0, num_of_days):
        food_cost = int(input())

    l_food.append(food_cost)

    # Prompt user for cost of Gas per day of trip (2nd Array)
    
    print('')
    print("Enter the cost of Gas per day of trip: ")
    print('')

    l_gas = []

    for i in range(0, num_of_days):
        gas_cost = int(input())

    l_gas.append(gas_cost)

    for ele in range(0, len(l_food)):
        total_food = total_food + l_food[ele]

    for elem in range(0, len(l_gas)):
        total_gas = total_gas + l_gas[elem]

    # Calculate total of trip and each persons share

    total_cost_trip = (total_food * num_of_days) + (total_gas * num_of_days)

    person_cost = total_cost_trip/num_of_people

    #Display results

    print('')

    print("The total cost of Each Category")
    print('')

    print("Food:", str(total_food * num_of_days))
    print("Gas:", str(total_gas * num_of_days))
    print('')

    print("The total cost of the trip: ", total_cost_trip)
    print('')

    print("Each person's share: %.2f" % person_cost)
    

main()
