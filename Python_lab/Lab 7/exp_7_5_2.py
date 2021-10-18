def BinarySearch(arr,low,high,key):
  if high <= low:
    print('not found')
    return 
  elif high == low:
    if arr[low] == key:
      print('found')
      return 
    else:
      print('not found')
      return 
  mid = (low+high)//2
  if key == arr[mid]:
    print('found')
    return 
  elif key > arr[mid]:
    BinarySearch(arr,mid+1,high,key)
  else:
    BinarySearch(arr,0,mid,key)
    
arr = [1,2,3,4,5,6,7]
n = int(input('enter the no. to search in array: '))
BinarySearch(arr,0,len(arr),n)
