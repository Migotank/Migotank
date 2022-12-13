#Program that uses a while loop and prompts the user for a series of inputs. 
#Developer: Miguel Perez
#Class: CMIS 102
#Date: November 17, 2022


def main():
    
    print('Welcome! this program calculates the total number of absent days from school.')
    print('')
    
    #Initialize variable total
    
    total_absent_days = 0
    
    #infinite loop
    
    while True:
        
        #Prompt for days absent for this week
        
        days_absent = int(input('Enter days absent for this week (input a negative number to end): '))
        print('')
        
        #Break out of the loop when input value is negative
        
        if days_absent<0: break
        
        #Add to the total
        
        total_absent_days += days_absent
        
        #Display the total absent days
        
        print('Total absent days from school:', total_absent_days)
        print('')

main()
