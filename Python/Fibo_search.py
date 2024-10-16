def fibonacci_search(arr, x):
    fib_m2 = 0  # (m-2)'th Fibonacci number
    fib_m1 = 1  # (m-1)'th Fibonacci number
    fib_m = fib_m2 + fib_m1  # m'th Fibonacci number

    while fib_m < len(arr):
        fib_m2 = fib_m1
        fib_m1 = fib_m
        fib_m = fib_m2 + fib_m1

    offset = -1

    while fib_m > 1:
        i = min(offset + fib_m2, len(arr) - 1)

        if arr[i] < x:
            fib_m = fib_m1
            fib_m1 = fib_m2
            fib_m2 = fib_m - fib_m1
            offset = i
        elif arr[i] > x:
            fib_m = fib_m2
            fib_m1 = fib_m1 - fib_m2
            fib_m2 = fib_m - fib_m1
        else:
            return i

    if fib_m1 and offset + 1 < len(arr) and arr[offset + 1] == x:
        return offset + 1

    return -1

# Example usage
data = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90]
x = 85
result = fibonacci_search(data, x)
if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")
