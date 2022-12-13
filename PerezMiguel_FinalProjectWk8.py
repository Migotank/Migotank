#Yard service involves mowing, edging and shrub pruning.
#Program builds on the assignments for weeks 3 and 4, In addition to the house cleaning service from the previous assignments, the company will now offer yard service.
#Program will begin by asking the customer whether they are requesting house cleaning or yard service. If the user inputs an invalid choice, the user should be re-prompted until a valid choice is made
#Program depending upon the choice should then prompt the user for the information needed to determine the cost of the service.
#Program will output the cost of the requested service.
#Program will have one function to calculate the house cleaning cost, another to calculate the yard service cost and a third to determine the discount.
#Developer: Miguel Perez
#Class: CMIS 102
#Date: December 7, 2022

def welcomemsg():
    print(' Welcome to Miguels Cleaning Services where we offer in-house cleanings and yard touch ups ') 

#---------- First Function (House Cleaning Cost) ----------

def House_cleaning():
    
    # Setting price for cleaning
    
    light_cost = 80
    complete_cost = 100
    
    # Setting price point for house size
    
    small = 100
    medium = 150
    large = 200

    # House sizes: Small <=3 , Medium = 4, Large >= 5

    
    def TotalCleanCost(Houses, clean_type):
        
        if clean_type == 1:
            clean_cost = light_cost
        else:
            clean_cost = complete_cost
        if Houses <= 3:
            total_cost = small + Houses * clean_cost
        elif Houses == 4:
            total_cost = medium + Houses * clean_cost
        elif Houses >= 5:
            total_cost = large + Houses * clean_cost
        return total_cost

    # Prompt user for # of Houses service is needed for
    
    print('-House service estimate:')
    print('')
    
    Houses = eval(input('How many Houses would you want to be cleaned?\n'))
    print('')

    # Prompt the user for cleaning (light or complete)
    
    print('-Different levels of cleaning:')
    print('')
    print('(1) Light: includes sweeping and dusting')
    print('(2) Complete: includes light cleaning + mop, bathrooms & windows')
    print('')
    clean_type = eval(input('For light enter 1, for complete enter 2\n'))

    # Call the function to get the cost
    
    answer = TotalCleanCost(Houses, clean_type)

    # Print out the total of cleaning the house
    
    print('')
    print('The total cost to clean your house is $', answer)
    return answer

#---------- Second Function (Yard Service Cost) -------------

def Yard_Service():
    
    # Prices of Yard service:
    
    #-- Price per sq feet --
    cost_mowing = 30
    
    #-- Price per feet --
    
    cost_edging = 20

    #-- Price of pruning shurbs --
    
    cost_shrub_pruning = 40 

    print('-Yard Service estimate: ')
    print('')
    print('How many square feet of yard do you want to mowed?')
    print('')
    yard_sq_feet=eval(input())
    print('')
    print('How many feet of edging do you want to clean?')
    print('')
    yard_edging=eval(input())
    print('')
    print('How many shrubs do you want to trimmed?')
    yard_shrubs=eval(input())
    print('')
    
    # Calculate the total cost of yard servicing
    
    total_cost=yard_sq_feet*cost_mowing+yard_edging*cost_edging+yard_shrubs*cost_shrub_pruning

    print('')
    print('The total cost of yard cleaning is $',total_cost)
    return total_cost

#---------- Third Function (Discount) --------------

def Calculate_Discount(cost):
    
    discount_amt=0.30*cost # Provide a 30% discount
    price_after_discount=cost-discount_amt
    return  price_after_discount

def main():
    # Display Welcome Message
    welcomemsg()
    print('')
    total_cost=0
    service_choice=int(input('Which service are you currently requesting?\n\n(1) House cleaning\n(2) Yard Service\n'))
    print('')
    if service_choice==1:
        total_cost=House_cleaning() # Calls the House_cleaning function and stores the final cost
    elif service_choice==2:
        total_cost=Yard_Service() # Calls the Yard_Service function and stores the final cost
    else:
        print('Invalid input')
        print('')
        main()
    
    # To provide discount to senior citizens
    
    print('')
    is_senior=input('Are you a senior citizen?\n\n(Y/N)\n')
    print('')
    if is_senior=='Y' or is_senior=='y':
        print('You have a 30 percent discount')
        print('')
        print("You need to pay:$",Calculate_Discount(total_cost))
        
    else:
        print('')
        print("You need to pay:$",total_cost)

main()


