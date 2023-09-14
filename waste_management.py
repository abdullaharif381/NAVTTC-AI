import numpy as np

def bin_size(box, shopper):   
    bins = np.zeros((shopper, box), dtype=int)
    counter = np.zeros(box, dtype=int)
    return bins, counter

def add_to_can(box, shopper, bins, counter): 
    box_num = None
    while box_num is None or box_num >= box:
        try:
            box_num = int(input("Choose the trashcan: "))
            if box_num >= box:
                print("Invalid trashcan number. Please choose again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    row = shopper - counter[box_num] - 1
    col = box_num

    if counter[box_num] < shopper:
        counter[box_num] += 1
    bins[row][col] = counter[box_num]

def display(box, shopper, bins, counter):
    for row in bins:
        print("|", end=" ")
        print(" | ".join(map(str, row)), end=" |\n")
    print("_" * (box * 5))
    print("Counter:", counter)
    return
