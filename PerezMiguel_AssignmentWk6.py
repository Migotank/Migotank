#Program determine whether a password exactly meets the following requirements for a secure password
#Program will prompt the user for the candidate password and then each function and display either that the password is valid or the first reason it is invalid.
#Program will contain three functions
#Developer: Miguel Perez
#Class: CMIS 102
#Date: November 23, 2022


def main():
    #Welcome Message

    print("Welcome, Let's see if we can get you a secure password!")
    print("")
    
    #----- 1st Function to check length of the password-----
    
    def lengthOfPassword(password):
        #If password is less than 6 or greater than 15, return False
        
        #Else return True
        
        if(len(password) < 6 or len(password) > 15):
            return False
        return True

    #---- 2nd Function to check if password contains any spaces----
    
    def containsSpace(password):
        
        #Returns True if it contains spaces
        
        #Else returns False
        
        if(' ' in password):
            return True
        return False

    #---- 3rd Function to check if password contains both digits and alphabets-----
    
    def containsDigitAndAlpha(password):
        
        #First checks if length of password is valid
        
        if(lengthOfPassword(password) == False):
            return "Length of password should be greater than 6 and less than 15"

        #Check if it contains spaces or not

        elif(containsSpace(password)):
            return "password should not contain space"

        #If it does not contain spaces, then check if the string is all alphabets

        elif(password.isalpha()):
            return "Password should have at least one digit"

        #Check if the string is all digits

        elif(password.isdigit()):
            return "Password should have at least one aphabet"

        #If all conditions are False, return Secure Password
        
        return "Great! you just made a Secure Password"
    
#Prompt Password input from the user
    
    password = input("Please enter your password: ")
    print("")

#Calling function of password to validate it
    
    print (containsDigitAndAlpha(password))

main()
