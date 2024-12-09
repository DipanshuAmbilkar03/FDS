# 4.1.0 bubble sort
# 4.1.1
arr = []
def sortStart() :
    leng = int(input("enter number of students :" ))
    # 4.1.2
    for i in range(1,leng+1):
        new = float(input(f"enter marks of student of roll number {i} : "))
        arr.append(new)
    print("Marks of Student's before sorting => ", arr)

def bubbleSort(arr) :
    n = len(arr)
    print("before sorting marks of students  : " , arr)
    # 4.1.3
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    print("after sorting marks of students using bubble sort : " , arr)
    # 4.1.4
    for i in range(n-3,n) :
        print(f"topper {n-i} marks is : {arr[i]} ")

# 4.2.0 selection sort 
def selectionSort(arr) :
    n = len(arr)
    print("before sorting marks of students  : " , arr)
    # 4.2.1
    for i in range(n-1):
        minPos = i
        for j in range(i+1, n):
            if arr[minPos] < arr[j]:
                minPos = j
        # Swap the found maximum element with the first element of the unsorted portion
        temp = arr[i]
        arr[i] = arr[minPos]
        arr[minPos] = temp
    
    print("after sorting marks of students using selection sort : " , arr)
    # 4.2.3
    for i in range(1,(len(arr)-1)) :
        print(f"topper {i} marks is : {arr[i]} ")

flag = 0;
while flag == 0 :
    print("""choose number 1 ,2, 3 or 4 for performing following tasks =>
          1) Enter student's Marks
          2) bubble sort
          3) selection sort 
          4) exit/quit
""")
    # enter choise 
    ch = int(input("Enter choise : "))
    if ch == 1 :
        sortStart()

    if ch == 2 :
        bubbleSort(arr)
        arr = []
        remind = input("Choose Y/N to continue bubble sorting.")
    
        if remind == 'Y' :
            print("enter marks again.")
            flag = 2
        if remind == 'N' :
            print("THANK YOU")
            flag = 4
        elif remind!='Y' or remind!='N' :
            print("Write Y or N")
            flag = 0
    
    if ch == 3 :
        selectionSort(arr)
        arr = []
        remind = input("Choose Y/N to continue Selection sorting.")
        if remind == 'Y' :
            print("enter marks again.")
            flag = 3
        if remind == 'N' :
            print("THANK YOU")
            flag = 4
        elif remind!='Y' or remind!='N' :
            print("Write Y or N")
            flag = 0
    
    elif ch == 4 :
        print("THANK YOU")
        break

# <---------------- NICE ONE :) ----------------->    
