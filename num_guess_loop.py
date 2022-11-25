#!/usr/bin/env python3
#
# Created by: Peter Sobowale
# Created on: Nov 14, 2022
# This program asks the user to guess a number
# It then checks if they get it wrong, tells them so 
# and then asks for a number from 0 and 9 until they
# guess correctly
import random


def main():
    # declare the variable
    loop_counter = 0

    # generate a random number between 0 and 9
    random_number = random.randint(0, 9)
 
    # while true to keep asking for a number until they guess right
    while True:
        # Get the user number as string
        user_num_string = input("Enter a whole number between 0 and 9: ")
        try:
            # convert from string to integer
            user_num = int(user_num_string)
            # Check if they inputted a number from 0-9
            if user_num >= 0 and user_num <= 9:
                # Increment counter by 1
                loop_counter += 1
                # check if they guessed correctly
                if user_num == random_number:
                    # Display result to user
                    print(" ")
                    print("{} is correct, good job!".format(user_num))
                    # break out of loop
                    break
                else:
                    # if they are wrong, keep going
                    # Display result to user
                    print("{} is incorrect".format(user_num))
                    print(" ")
                    print("Tracking {0} times through the loop.".format(loop_counter))
                    print(" ")
            else:
                # display if the number isn't from 0-9
                print("This number is not between 0 and 9")
        # exception for erroneous/invalid input
        except Exception:
            print("{} is invalid.".format(user_num_string))
            print(" ")
 
 
if __name__ == "__main__":
    main()
