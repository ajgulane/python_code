arr = []
def average(arr):
    getArr()
    total = sum(arr)
    average = total/len(arr)
    print("The average is ", average )

def getArr():
    n = int(input("Enter number of Array: "))

    for i in  range(n):
        x = float(input("Enter Value: "))
        arr.append(x)
average(arr)

    