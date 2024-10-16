def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n  # Output array
    count = [0] * 10  # Count array for digits 0-9

    # Count occurrences of digits
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # Update count[i] so that it contains actual position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build output array
    for i in range(n - 1, -1, -1):
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1

    # Copy the output array to arr[]
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max1 = max(arr)  # Get maximum number

    # Do counting sort for every digit
    exp = 1
    while max1 // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Example usage
data = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(data)
print("Sorted array is:", data)
