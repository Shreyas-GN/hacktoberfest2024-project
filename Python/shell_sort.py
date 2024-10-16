def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # Start with a big gap, then reduce the gap

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

# Example usage
data = [12, 34, 54, 2, 3]
shell_sort(data)
print("Sorted array is:", data)
