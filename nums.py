# File:    nums.py
# Started: by Dr. Gibson
# Author:  Uzoma Uwanamodo
# Date:    10/26/2016
# Section: 05
# E-mail:  uu3@umbc.edu
# Description:
#   This file contains python code that uses functions to 
#   allow a user to get basic information about a number
#   they've entered.

MIN_VAL = -1000000
MAX_VAL =  1000000

# evenOrOdd() takes in a number and returns whether it's even or odd
# Input:      number, an integer
# Output:     a string -- either "even" or "odd" should be returned
def evenOrOdd(number):
    ####################################################################
    # your function to determine if the number's even or odd goes here #
    ####################################################################
    # return "even" if the remainder of the number divided by 2 is even, otherwise return "odd"
    return ["even","odd"][number % 2]

# posNegZero() takes in a number and returns its sign
# Input:      num, an integer
# Output:     a string -- either "negative", "positive", or "zero" 
#                         should be returned
def posNegZero(num):
    ##########################################################
    # your function to determine the number's sign goes here #
    ##########################################################
    # return "negative" if x is less than 0, "postive" if x is greater than 0, otherwise return 0
    return "negative" if num < 0 else "postive" if num > 0 else "zero"

# getValidInt() takes in a minn and maxx, and gets a number from the
#               user between those two numbers (inclusive)
# Input:      minn and maxx, two integers
# Output:     an integer, between minn and maxx inclusive
def getValidInt(minn, maxx):
    message = "Please enter a number between " + str(minn) + " and " + \
        str(maxx) + " (inclusive): "

    newInt = int(input(message))
    #######################################
    # your code that loops until the user # 
    # enters a valid number goes here     #
    #######################################
    while newInt not in range (minn, maxx):
        newInt = int(input(message))
    
    # while loop exited, return the user's choice
    return newInt




def main():

    print("Welcome to the number program!")

    # get a valid number from the user
    ##########################################################
    # your code to call the function getValidInt() goes here #
    # ** use the constants MIN_VAL and MAX_VAL in your call  #
    ##########################################################
    userNum = getValidInt(MIN_VAL, MAX_VAL)

    # call the posNegZero function and print out the result to the user
    #########################################################
    # your code to call the function posNegZero() goes here #
    #########################################################
    print("The number", userNum, "is", posNegZero(userNum))

    # call the evenOrOdd function and print out the result to the user
    ########################################################
    # your code to call the function evenOrOdd() goes here #
    ########################################################
    print("The number", userNum, "is", evenOrOdd(userNum))

    # say goodbye and exit the program
    print("Thank you for using the number program!  Come again!")


main()


