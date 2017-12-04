#  File: sorting.py
#  Description: Compares the sorting time for various sorting algorithms 
#  Student's Name: Trace Tschida
#  Student's UT EID: TRT729
#  Course Name: CS 313E 
#  Unique Number: 51465
#
#  Date Created: 11/21/2017
#  Date Last Modified: 11/27/2017


import random
import time
import math
import copy
import sys
sys.setrecursionlimit(10000)

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp


def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            alist[position] = alist[position-1]
            position = position-1

        alist[position] = currentvalue


def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1


def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    if first < last:
        splitpoint = partition(alist,first,last)
        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):

    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False

    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark

def timesAverage(alist):

    average = float(sum(alist)) / float(len(alist))

    return average


def sortList(alist, bubble_times, insertion_times, merge_times, quick_times):

    for trial in range(5):

        # create a temporary list to sort
        temp_list = copy.deepcopy(alist)

        # start the timer
        start_time = time.clock()

        # run bubble sort
        bubbleSort(temp_list)

        # end the timer
        end_time = time.clock()

        # get the elasepd time
        elasped_time = end_time - start_time

        # add the time to the bubble list
        bubble_times.append(elasped_time)
            
    for trial in range(5):

        # create a temporary list to sort
        temp_list = copy.deepcopy(alist)

        # start the timer
        start_time = time.clock()

        # run bubble sort
        insertionSort(temp_list)

        # end the timer
        end_time = time.clock()

        # get the elasepd time
        elasped_time = end_time - start_time

        # add the time to the bubble list
        insertion_times.append(elasped_time)

    for trial in range(5):

        # create a temporary list to sort
        temp_list = copy.deepcopy(alist)

        # start the timer
        start_time = time.clock()

        # run bubble sort
        mergeSort(temp_list)

        # end the timer
        end_time = time.clock()

        # get the elasepd time
        elasped_time = end_time - start_time

        # add the time to the bubble list
        merge_times.append(elasped_time)

    for trial in range(5):

        # create a temporary list to sort
        temp_list = copy.deepcopy(alist)

        # start the timer
        start_time = time.clock()

        # run bubble sort
        quickSort(temp_list)

        # end the timer
        end_time = time.clock()

        # get the elasepd time
        elasped_time = end_time - start_time

        # add the time to the bubble list
        quick_times.append(elasped_time)


def main():

    # generate a list containing n integers in random order
    num_ints = [10, 100, 1000]

    # dictionary to hold the times
    time_dict = {"random": {"bubble": {10:0, 100:0, 1000:0}, "insertion": {10:0, 100:0, 1000:0}, "merge": {10:0, 100:0, 1000:0}, "quick": {10:0, 100:0, 1000:0}},
    "sorted": {"bubble": {10:0, 100:0, 1000:0}, "insertion": {10:0, 100:0, 1000:0}, "merge": {10:0, 100:0, 1000:0}, "quick": {10:0, 100:0, 1000:0}},
    "reverse": {"bubble": {10:0, 100:0, 1000:0}, "insertion": {10:0, 100:0, 1000:0}, "merge": {10:0, 100:0, 1000:0}, "quick": {10:0, 100:0, 1000:0}},
    "almost": {"bubble": {10:0, 100:0, 1000:0}, "insertion": {10:0, 100:0, 1000:0}, "merge": {10:0, 100:0, 1000:0}, "quick": {10:0, 100:0, 1000:0}}}

    # hold the times for each type of sort
    bubble_times = []
    insertion_times = []
    merge_times = []
    quick_times = []

    # go through each number of integrers to create random list
    # random list
    for n in num_ints:

        # create the random lists
        random_list = [i for i in range(n)]
        random.shuffle(random_list)

        # sort the list
        sortList(random_list, bubble_times, insertion_times, merge_times, quick_times)

        # get the averages
        bubble_average = timesAverage(bubble_times)
        insertion_average = timesAverage(insertion_times)
        merge_average = timesAverage(merge_times)
        quick_average = timesAverage(quick_times)

        # add the times to the dictionary 
        time_dict["random"]["bubble"][n] = bubble_average
        time_dict["random"]["insertion"][n] = insertion_average
        time_dict["random"]["merge"][n] = merge_average
        time_dict["random"]["quick"][n] = quick_average

        # print(bubble_times)
        # print(insertion_times)
        # print(merge_times)
        # print(quick_times)

        # clear the times
        bubble_times.clear()
        insertion_times.clear()
        merge_times.clear()
        quick_times.clear()


    # sorted list
    for n in num_ints:

        # create a sorted list
        sorted_list = [i for i in range(n)]

        # sort the list
        sortList(sorted_list, bubble_times, insertion_times, merge_times, quick_times)

        # get the averages
        bubble_average = timesAverage(bubble_times)
        insertion_average = timesAverage(insertion_times)
        merge_average = timesAverage(merge_times)
        quick_average = timesAverage(quick_times)

        # add the times to the dictionary 
        time_dict["sorted"]["bubble"][n] = bubble_average
        time_dict["sorted"]["insertion"][n] = insertion_average
        time_dict["sorted"]["merge"][n] = merge_average
        time_dict["sorted"]["quick"][n] = quick_average

        # clear the times
        bubble_times.clear()
        insertion_times.clear()
        merge_times.clear()
        quick_times.clear()

    # reverse sorted
    for n in num_ints:

        # create a reverse sorted list 
        reverse_list = [i for i in range(n, 0, -1)]

        # sort the list
        sortList(reverse_list, bubble_times, insertion_times, merge_times, quick_times)

        # get the averages
        bubble_average = timesAverage(bubble_times)
        insertion_average = timesAverage(insertion_times)
        merge_average = timesAverage(merge_times)
        quick_average = timesAverage(quick_times)

        # add the times to the dictionary 
        time_dict["reverse"]["bubble"][n] = bubble_average
        time_dict["reverse"]["insertion"][n] = insertion_average
        time_dict["reverse"]["merge"][n] = merge_average
        time_dict["reverse"]["quick"][n] = quick_average

        # clear the times
        bubble_times.clear()
        insertion_times.clear()
        merge_times.clear()
        quick_times.clear()

    # almost sorted
    for n in num_ints:

        # create a almost sorted list
        almost_sorted = [i for i in range(n)]

        # randomly swap 10% of the elements
        num_swaps = int(n * 0.10)
        for i in range(num_swaps):

            # get 2 random indexes to swap with
            randomIdx1 = random.randint(0, n - 1)
            randomIdx2 = random.randint(0, n - 1)

            # swap the numbers
            temp = almost_sorted[randomIdx1]
            almost_sorted[randomIdx1] = almost_sorted[randomIdx2]
            almost_sorted[randomIdx2] = temp
        
        # sort the list
        sortList(almost_sorted, bubble_times, insertion_times, merge_times, quick_times)

        # get the averages
        bubble_average = timesAverage(bubble_times)
        insertion_average = timesAverage(insertion_times)
        merge_average = timesAverage(merge_times)
        quick_average = timesAverage(quick_times)

        # add the times to the dictionary 
        time_dict["almost"]["bubble"][n] = bubble_average
        time_dict["almost"]["insertion"][n] = insertion_average
        time_dict["almost"]["merge"][n] = merge_average
        time_dict["almost"]["quick"][n] = quick_average

        # clear the times
        bubble_times.clear()
        insertion_times.clear()
        merge_times.clear()
        quick_times.clear()

    # print the results

    print("Input type = Random")
    print("\t\t\t avg time   avg time   avg time")
    print("   Sort function\t  (n=10)    (n=100)    (n=1000)")
    print("------------------------------------------------------------")
    print("      bubbleSort\t {:f}   {:f}   {:f}".format(time_dict["random"]["bubble"][10],time_dict["random"]["bubble"][100],time_dict["random"]["bubble"][1000]))
    print("   insertionSort\t {:f}   {:f}   {:f}".format(time_dict["random"]["insertion"][10],time_dict["random"]["insertion"][100],time_dict["random"]["insertion"][1000]))
    print("       mergeSort\t {:f}   {:f}   {:f}".format(time_dict["random"]["merge"][10],time_dict["random"]["merge"][100],time_dict["random"]["merge"][1000]))
    print("       quickSort\t {:f}   {:f}   {:f}".format(time_dict["random"]["quick"][10],time_dict["random"]["quick"][100],time_dict["random"]["quick"][1000]))
    print()

    # sorted
    print("Input type = Sorted")
    print("\t\t\t avg time   avg time   avg time")
    print("   Sort function\t  (n=10)    (n=100)    (n=1000)")
    print("------------------------------------------------------------")
    print("      bubbleSort\t {:f}   {:f}   {:f}".format(time_dict["sorted"]["bubble"][10],time_dict["sorted"]["bubble"][100],time_dict["sorted"]["bubble"][1000]))
    print("   insertionSort\t {:f}   {:f}   {:f}".format(time_dict["sorted"]["insertion"][10],time_dict["sorted"]["insertion"][100],time_dict["sorted"]["insertion"][1000]))
    print("       mergeSort\t {:f}   {:f}   {:f}".format(time_dict["sorted"]["merge"][10],time_dict["sorted"]["merge"][100],time_dict["sorted"]["merge"][1000]))
    print("       quickSort\t {:f}   {:f}   {:f}".format(time_dict["sorted"]["quick"][10],time_dict["sorted"]["quick"][100],time_dict["sorted"]["quick"][1000]))
    print()

    # reverse
    print("Input type = Reverse")
    print("\t\t\t avg time   avg time   avg time")
    print("   Sort function\t  (n=10)    (n=100)    (n=1000)")
    print("------------------------------------------------------------")
    print("      bubbleSort\t {:f}   {:f}   {:f}".format(time_dict["reverse"]["bubble"][10],time_dict["reverse"]["bubble"][100],time_dict["reverse"]["bubble"][1000]))
    print("   insertionSort\t {:f}   {:f}   {:f}".format(time_dict["reverse"]["insertion"][10],time_dict["reverse"]["insertion"][100],time_dict["reverse"]["insertion"][1000]))
    print("       mergeSort\t {:f}   {:f}   {:f}".format(time_dict["reverse"]["merge"][10],time_dict["reverse"]["merge"][100],time_dict["reverse"]["merge"][1000]))
    print("       quickSort\t {:f}   {:f}   {:f}".format(time_dict["reverse"]["quick"][10],time_dict["reverse"]["quick"][100],time_dict["reverse"]["quick"][1000]))
    print()

    # almost
    print("Input type = Almost sorted")
    print("\t\t\t avg time   avg time   avg time")
    print("   Sort function\t  (n=10)    (n=100)    (n=1000)")
    print("------------------------------------------------------------")
    print("      bubbleSort\t {:f}   {:f}   {:f}".format(time_dict["almost"]["bubble"][10],time_dict["almost"]["bubble"][100],time_dict["almost"]["bubble"][1000]))
    print("   insertionSort\t {:f}   {:f}   {:f}".format(time_dict["almost"]["insertion"][10],time_dict["almost"]["insertion"][100],time_dict["almost"]["insertion"][1000]))
    print("       mergeSort\t {:f}   {:f}   {:f}".format(time_dict["almost"]["merge"][10],time_dict["almost"]["merge"][100],time_dict["almost"]["merge"][1000]))
    print("       quickSort\t {:f}   {:f}   {:f}".format(time_dict["almost"]["quick"][10],time_dict["almost"]["quick"][100],time_dict["almost"]["quick"][1000]))
    print()
main()
