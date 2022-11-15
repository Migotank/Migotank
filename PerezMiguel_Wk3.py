#This program will help decide what type of pet fish you want
#Program perform two different computations value of the first input.
#Developer: Miguel Perez
#Class: CMIS 102
#Date: 11/04/2022


def main ():
    #Display welcome message
    print(' Welcome to Pik-a-Fish!! What pet fish might you be interested in today? ')
    print('')

    #Prompt user for answer to questions
    troporcold = input(' For starters, Would you like a cold water or tropical fish? \n')
    if (troporcold == 'cold water'):
        print('')
        print('Great choice!')
        gchoice= input(' Now, which of these are you most interested in: catfish or goldfish? \n')
        if (gchoice == 'catfish'):
          print('')
          print(' Congratulations, they’re relatively low-maintenance, can come in many shapes and sizes \n and are reasonably inexpensive. Thank you for visiting us today :)' )
        else:
            print('')
            print(' Awesome, We are sure you will enjoy your new pet fish!! Thank you for visiting us today.')

    else:
         print('')
         print('Awesome!')
         awechoice = input('Now, which of these fish are you most interested in: betta or guppie ? \n')
         if (awechoice == 'betta'):
             print('')
             print(' Super sorry for the inconvenience :( but unfortunately we have none in stock, come back tomorrow')
         else:
                 print('')
                 print('Guppies are amazing fish and very popular, Congrualations on your new pet!')


main()
