from array import *

arr = []

def average(score):
    total = sum(score)
    average = total/len(score)
    print("The Average of the Array is: ",average)

def getArray(n):
    for i in range(n):
        x = int(input("Enter Value if Array: "))
        arr.append(x)

getArray(int(input("Enter Length of Array: ")))

average(arr)


