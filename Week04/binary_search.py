arr = [4, 5, 6, 7, 0, 1, 2]
arr2 = [6, 7, 8, 1, 2, 3, 4, 5]


def find_point(arr):

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[left] > arr[mid] and arr[right] > arr[mid]:
            return mid

        if arr[mid] > arr[right]:
            left = mid

        if arr[mid] < arr[left]:
            right = mid

print(arr, " => ", find_point(arr))
print(arr2, " => ", find_point(arr2))
