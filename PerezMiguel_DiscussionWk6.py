#Program will accepts a string as input. It should analyze some characteristic of that string and display the result of that analysis.
#Program will also determine if my initials (M,m,P,p), in any case combination, are inside the string.
#Developer: Miguel Perez
#Class: CMIS 102
#Date: 11/26/2022


def main():

    print("Hi, My name is Miguel Perez. Welcome! This program will display the number of spaces that are in your video game title and captialize your title. \nIt will also determine if any of my initials were used. M,P,m,p")
    print('')
    
    # Prompt user for favorite video game
    
    print("Let's see how many spaces are in the title of your video game! \n")
    print('')

    fav_game = input("What is your favorite video game? \n")
    print('')

    # Captialize video game title 

    game = fav_game.title()
    
    print("Your favorite video game is: ", game)
    print('')
    
    # Count number of spaces in title
    
    count = 0
    for letter in game:
        if letter == " ":
            count = count + 1
    
    print("Your video game title contains ", count, " spaces! \n")
    print('')

    # Check for initials in video game title + Display results
    
    print("Now let's check to see if your favorite video game title contains my initials! \n")
    print('')
    
    count = 0
    for initial in game:
        if initial == "m" or initial == "M":
            count = count + 1
    print("Your video game title contains a M from my initials M.P ", count, " times! \n")
    print('')
    
    
    count = 0
    for initial in game:
        if initial == "p" or initial == "P":
            count = count + 1
    print("Your video game title contains a P from my initials M.P ", count, " times! \n")
    print('')

    
    


main()
    
