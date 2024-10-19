# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Shell Sort
def shell_sort(arr):
    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

percentages = [76.2, 84.1, 72.8, 91.5, 87.3, 79.4, 95.6, 89.2, 68.7]

# Insertion Sort
insertion_sorted = percentages.copy()
insertion_sort(insertion_sorted)
print("Top 5 scores (Insertion Sort):", insertion_sorted[-5:])

# Shell Sort
shell_sorted = percentages.copy()
shell_sort(shell_sorted)
print("Top 5 scores (Shell Sort):", shell_sorted[-5:])
