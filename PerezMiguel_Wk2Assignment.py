#Program that computes the weekly pay for a paper carrier
#Program prompts the user for the following numeric values:
#Number of papers on the route, the amount of tips received for the week
#Number of days the paper is delivered per week
#Program will also define the cost of each newspaper and a percentage rate for commission.
#Program will output the total number of papers delivered for the week, the weekly salary,
#Also the tips for the week and the total pay for the week.

#Developer: Miguel Perez
#Class: CMIS 102
#Date: October 31, 2022

def main():
    #Prompts user for the number of papers on the route
    num_of_papers=int(input('Enter the number of papers on the route \n'))
    print('')
    
    #Prompts user for the number of days the paper is deliverd per week
    num_of_days=int(input('Enter the number of days the paper is delivered per week \n'))
    print('')

    #Prompts user for the amounts of tips recevied for the week
    tips=int(input('Enter the amount of tips received for the week \n'))
    print('')

    #Defining cost of each newpaper and a percentage rate for commission
    
    cost = 15
    percent = 20
    
    total_num_of_papers_delivered = num_of_papers * num_of_days
    
    weekly_salary = total_num_of_papers_delivered * (percent/100) * cost
    
    total_pay = weekly_salary + tips

    #Output total # of papers delivered for the week, weekly salary, tips and total pay for week

    print('The total number of papers delivered for the week = ', total_num_of_papers_delivered)
    print('')
    
    print('The weekly salary = ', weekly_salary)
    print('')

    print('Tips for the week = ', tips)
    print('')

    print('Total pay = ', total_pay)
    print('')

    

main()

    
