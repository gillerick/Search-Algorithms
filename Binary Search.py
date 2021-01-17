def binarySearch(arr, item):
    # The first step is to sort the array items
    arr.sort()
    start_index = 0
    end_index = len(arr) - 1

    while start_index <= end_index:
        mid = start_index + (end_index - start_index) // 2
        mid_item = arr[mid]
        if mid_item == item:
            return f"{item} was found at position {mid}"
        elif item < mid_item:
            end_index = mid - 1
        else:
            start_index = mid + 1
    return f"{item} not found in the array"


if __name__ == "__main__":
    print(binarySearch([3, 6, 7, 1, 9, 10, 4, 30], 20))
    print(binarySearch([3, 6, 7, 1, 9, 10, 4, 30], 9))
