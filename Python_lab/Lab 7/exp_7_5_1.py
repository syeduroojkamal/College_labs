arr = [4,5,6,3,7,2,1,11,15]
key = int(input('enter element to search: '))
flag = 0
for i in range(len(arr)):
    if key == arr[i]:
        print(f'{key} found at {i+1} location')
        flag += 1
if flag == 0 :
    print('element not found')