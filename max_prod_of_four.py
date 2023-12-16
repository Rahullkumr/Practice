def max_prod_of_four(arr,size):
    # sorting the array in ascending order
    for i in range(size):
        min = arr[i]
        for j in range(i+1, size):
            if arr[j] < min:
                arr[i], arr[j] = arr[j], arr[i]
                min = arr[i]
            else:
                pass

    print(f'sorted array: {arr}')


    pdt = 1
    for i in range(-1,-5,-1):
        pdt *= arr[i]
    print(f'Maximum product = {pdt}')


# arr=[4,0,1,2,8,3]
arr=[12, -5, 9, 0, 3, 7, -2, 4, 6, 8]


print(f'Original array: {arr}')
size=len(arr)
max_prod_of_four(arr,size)
