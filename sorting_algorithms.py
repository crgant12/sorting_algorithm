#Purpose: Implement insertion sort, quicksort(with the random selection of pivot) and mergesort
import math
import random

#Initalizing the global variable that will be used for all of the comparisons
comparisons = 0

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
    
def mergeSort(a):
    #Input: An array of numbers a[]
    #Output: a sorted version of this array

    q = Queue()
    
    for i in a:
        q.enqueue([i])
    while(q.size() > 1):
        q.enqueue(merge(q.dequeue(), q.dequeue()))
    return q.dequeue()
   
   
   
def merge(x, y):
    #Input: Two sorted arrays x and y
    #Ouput: A sorted arry obtained from merging x and y
    
    mergedList = []
    x_pointer = 0
    y_pointer = 0
    
    while(x_pointer < len(x) and y_pointer < len(y)):
        #increasing the number of comparisons by one
        global comparisons
        comparisons += 1      
        
        if(x[x_pointer] <= y[y_pointer]):
            mergedList.append(x[x_pointer])
            x_pointer += 1
        else:
            mergedList.append(y[y_pointer])
            y_pointer += 1
    if(x_pointer < len(x)):
        for i in range(x_pointer, len(x)):
            mergedList.append(x[x_pointer])
            x_pointer += 1
    elif(y_pointer < len(y)):
        for i in range(y_pointer, len(y)):
            mergedList.append(y[y_pointer])
            y_pointer += 1
          
    return mergedList
    
    
def insertionSort(a):
    #Input: An array of numbers 
    #Output: a sorted version of this array
    
    #initalizing the global variable for the number of comparisons
    global comparisons
    for i in range(1, len(a), 1):
        #initalizing the index and the 
        k = i - 1
        x = a[i]
        countOnce = False
        comparisons += 1
        while(x < a[k] and k >= 0): 
            #adding one to the number of comparisons
            if(countOnce == False):
                countOnce = True
            else:                
                comparisons += 1
            
            #switching variables
            a[k + 1] = a[k] 
            k = k - 1
        a[k+1] = x
    return a

  
def quickSort(a):
    #Input: An aray of numbers
    #Output: a sorted version of this array
    
    global comparisons
    if(len(a) <= 50):
        return insertionSort(a[:])
    
    #Initalizing the arrays for the partition and the pivot that will decide the value of the partition
    pivot = random.randrange(0, len(a) - 1)
    beforePivotArray = []
    pivotArray = []
    afterPivotArray = []
    
    for i in range(0, len(a), 1):
        #adding one to the number of comparisons
        comparisons += 1
        
        if(a[i] < a[pivot]):
            beforePivotArray.append(a[i])
        elif(a[i] > a[pivot]):
            afterPivotArray.append(a[i])
        else:
            pivotArray.append(a[i])
    
    return quickSort(beforePivotArray[:]) + pivotArray + quickSort(afterPivotArray[:])  
  
    
def main():
    #initalizing the array that will store the pre-sorted list
    numsToSort = []

    complete = False
    
    print("This is the first part of the assignment where you can pick which algorithm and which array you want to sort")
    print("Enter 1 for Insertion Sort")
    print("Enter 2 for Quick Sort")
    print("Enter 3 for Merge Sort")
    answer = str(input("Enter the algorithm that you want to sort with: "))
    while(complete == False):
        if(answer != "1" and answer != "2" and answer != "3"):
            print()
            print("Sorry that isn't a valid entry")
            answer = input("Please enter a valid entry: ")
        else:
            complete = True

    print()
    complete = False
    
    print("Please enter the numbers that you want to sort and enter a letter to stop: ")
    while(complete != True):
        entry = input("")
        if(entry.isnumeric()):
            entry = int(entry)
            numsToSort.append(entry)
        else:
            complete = True
    print("Here is the array that will be sorted")
    print(numsToSort)
    
    global comparisons
    #making sure that the comparison counter begins at zero each time one of the algorithms is called
    comparisons = 0
    
    #initalizng the amount of numbers that will be in each sorting algorithm
    rangeOfNums = [100, 200, 400, 800, 1600, 3200, 6400]    
    
    if(answer == "1"):
        print("Your sorted array:")
        print(insertionSort(numsToSort[:]))
        print("With Insertion Sort, there were ", comparisons, "comparisons made.")

    elif(answer == "2"):
        print("Your sorted array:")
        print(quickSort(numsToSort[:]))
        print("With Quick Sort, there were ", comparisons, "comparisons made.")

    else:
        print("Your sorted array:")
        print(mergeSort(numsToSort[:]))
        print("With Merge Sort, there were ", comparisons, "comparisons made.")      
    
    print("This part of the assignment is where the starting array is in decending order")
    for algo in range(0, 3, 1): 
        if(algo == 0):
            print("Using Insertion Sort:")
        elif(algo == 1):
            print("Using Quick Sort:")
        else:
            print("Using Merge Sort:")
            
        for number in rangeOfNums:
            numsToSort = []
            for i in range(number, 0, -1):
                numsToSort.append(i)
            #making sure that the comparison counter begins at zero each time one of the algorithms is called
            comparisons = 0
            
            if(algo == 0):
                sortedArray = insertionSort(numsToSort[:])
                print("The sorted list of ", number, "numbers is:")
                print(sortedArray)
                print("Using insertionSort, it took ", comparisons, "comparisons for ", number, "numbers")
                print()
            elif(algo == 1):
                sortedArray = quickSort(numsToSort[:])
                print("The sorted list of ", number, "numbers is:")
                print(sortedArray)
                print("Using Quick Sort, it took ", comparisons, "comparisons for ", number, "numbers") 
                print()
            else:
                sortedArray = mergeSort(numsToSort[:])
                print("The sorted list of ", number, "numbers is:")
                print(sortedArray)
                print("Using Merge Sort, it took ", comparisons, "comparisons for ", number, "numbers") 
                print()

    print("This final part of the assignment is where the starting array is in the form [6, 5, 4, 3, 2, 1, 7, 8, 9, . . . , n − 4, n − 3, n, n − 1, n − 2]")
    
    for algo in range(0, 3, 1):         
        if(algo == 0):
            print("Using Insertion Sort")
        elif(algo == 1):
            print("Using Quick Sort")
        else:
            print("Using Merge Sort")

        for number in rangeOfNums:
            #initalizing the beginning array
            numsToSort = [6, 5, 4, 3, 2, 1]
            
            #completing the array that has to be added together
            for i in range(7, number - 2, 1):
                numsToSort.append(i)
            numsToSort.append(number)
            numsToSort.append(number - 1)
            numsToSort.append(number - 2)
            
            #making sure that the comparison counter begins at zero each time one of the algorithms is called
            comparisons = 0
            if(algo == 0):
                sortedArray = insertionSort(numsToSort[:])
                print("The sorted list of ", number, "numbers is:")
                print(sortedArray)
                print("Using insertionSort, it took ", comparisons, "comparisons for ", number, "numbers")
                print()
            elif(algo == 1):
                sortedArray = quickSort(numsToSort[:])
                print("The sorted list of ", number, "numbers is:")
                print(sortedArray)
                print("Using Quick Sort, it took ", comparisons, "comparisons for ", number, "numbers") 
                print()
            else:
                sortedArray = mergeSort(numsToSort[:])
                print("The sorted list of ", number, "numbers is:")
                print(sortedArray)
                print("Using Merge Sort, it took ", comparisons, "comparisons for ", number, "numbers") 
                print()
    print("Complete")
main()