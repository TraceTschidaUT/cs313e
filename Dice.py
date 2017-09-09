#  File: Dice.py
#  Description: A simulator for dice throws 
#  Student's Name: Trace Tschida
#  Student's UT EID: TRT729
#  Course Name: CS 313E 
#  Unique Number: XXXXX
#
#  Date Created: 9/8/2017
#  Date Last Modified: 9/8/2017

import random
import math



def main():

    # seed the random function 
    random.seed(1314)

    # ask the user for how many trial
    str_trials = input("How many times do you want to roll the dice? ")

    # convert str_trails into an in 
    num_trails = int(str_trials)

    dct_results = {
        2:0,
        3:0,
        4:0,
        5:0,
        6:0,
        7:0,
        8:0,
        9:0,
        10:0,
        11:0,
        12:0
    }

    # loop through the trials and produce the results
    for i in range(num_trails):

        # have a running total
        int_roll_total = 0

        # do the rolls and add to total
        int_roll_total += random.randint(1,6)
        int_roll_total += random.randint(1,6)

        # add the value to the key 
        dct_results[int_roll_total] += 1
 
    # print the result
    print(list(dct_results.values()))
    print()

    # check to see if number of trials is over 100
    if num_trails > 100:

        # set the constant reducer
        int_reducer = 100 / num_trails

        # reduce the results for formating by 100/trials
        for num in dct_results.keys():
            int_scaled_num = round(dct_results[num] * int_reducer)
            dct_results[num] = int_scaled_num

    print(dct_results.keys())

    # format the information 
    while sum(list(dct_results.values())) > 0:

        # print the side bar 
        print("|  ", end='')

        # find the max in the list
        int_max = max(list(dct_results.values()))
        
        # go through each number in the list and print the information 
        for i in (dct_results.keys()):

            # check to see if the number is greater than zero 
            if dct_results[i] >= int_max:

                # print the star
                print("*  ", end='')

                # reduce the number in the list
                dct_results[i] -= 1
            
            # just print a space
            else:
                print("   ", end='')
            
        # add the line break 
        print("")

    # print the bottom information
    print("+--+--+--+--+--+--+--+--+--+--+--+-")
    print("   2  3  4  5  6  7  8  9 10 11 12")

    #

# call main
main()



