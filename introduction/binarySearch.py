def binarySearch(arr, target):
  low = 0
  high = len(arr) - 1
  while (low <= high):
    mid = (low+high)//2
    if (arr[mid] == target):
      return True
    elif (arr[mid] < target):
      low = mid + 1
    else:
      high = mid - 1
  return False

  
#Runtime is o(log n)
print(binarySearch([1, 2, 3, 4, 5], 6))
