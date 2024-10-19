# Function to perform Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

percentages = [78.5, 82.0, 69.3, 90.1, 85.5, 74.8, 88.9, 92.3, 70.4]

sorted_percentages = quick_sort(percentages)

print("Top 5 scores:", sorted_percentages[-5:])
