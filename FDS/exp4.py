arr = []
def sortStart() :
    leng = int(input("enter number of students :" ))
    for i in range(1,leng+1):
        new = float(input(f"enter marks of student of roll number {i} : "))
        arr.append(new)

def bubbleSort(arr) :
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    print("after sorting marks of students using bubble sort : " , arr)
    for i in range(n-3,n) :
        print(f"topper {n-i} marks is : {arr[i]} ")
        
def selectionSort(arr) :
    n = len(arr)
    for i in range(n-1):
        minPos = i
        for j in range(i+1, n):
            if arr[minPos] > arr[j]:
                minPos = j
        temp = arr[i]
        arr[i] = arr[minPos]
        arr[minPos] = temp
    print("after sorting marks of students using selection sort : " , arr)

sortStart()
print("before sorting marks of students  : " , arr)
bubbleSort(arr)
selectionSort(arr)
