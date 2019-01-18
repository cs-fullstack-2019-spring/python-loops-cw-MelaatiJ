def main():
    # Exercise1()
    # Exercise2()
    # Exercise3()
    Exercise4()



def Exercise1():
    for randomnumbers in range(-20,51):
        print(randomnumbers)
    # Print -20 to and including 50.
    # Use any loop you want.


def Exercise2():
    for randomnumbers in range(0,21):
        if (randomnumbers %2==0):
            print(randomnumbers)

    # Create a loop that prints even numbers from 0 to and including 20.


def Exercise3():
    num1 = int(input("Enter a number"))
    num2 = int(input("Enter another number"))
    num3 = int(input("Enter one last number"))
    sumofNumbers = (num1 + num2 + num3)
    theAverage = (sumofNumbers/3)
    print("The average of ",num1,",",num2,"and",num3, "is", theAverage)


    # Prompt the user for 3 numbers.
#         Then print the 3 numbers along with their average after the 3rd number is entered.
#         Refer to example below replacing ```NUMBER1```, ```NUMBER2```, ```NUMBER3```, and ```THEAVERAGE``` with the actual values.
#
# Ex.Output
# ```
# The average of NUMBER1, NUMBER2, and NUMBER3 is THEAVERAGE
# ```
#
#
#


def Exercise4():
    userPassword = input("Enter your a password")
    userConfirm = input("confirm your password")
    while(userPassword != userConfirm):
        userquit = input("enter 'quit' to if you dont know your password")
        if(userquit == "quit"):
            break


    # Password Checker - Ask the user to enter a password.
    # Ask them to confirm the password.
    # If it's not equal, keep asking until it's correct or they enter 'Q' to quit.




























if __name__ == '__main__':
    main()