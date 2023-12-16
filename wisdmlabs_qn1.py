# write a function to find maximum product by multiplying 4 integers from an array.
# asc_arr=[]
# def max_prod_of_four(arr,size):
#     min=arr[0]
#     for i in range(0,size):
#         for j in range(i+1,size):
#             if arr[i]>=arr[j]:
#                 temp=arr[i]
#                 arr[i]=arr[j]
#                 arr[j]=temp   
#         asc_arr.append(min)     
#     print(asc_arr)       

# arr=[4,0,1,2,8,3]
# size=len(arr)
# max_prod_of_four(arr,size)


asc_arr=[]
def max_prod_of_four(arr,size):
    min = 0
    for i in range(size):
        for j in range(i+1, size):
            if arr[j] >= min:
                min = arr[j]
            else:
                pass
        print(min)
        asc_arr.append(min)
    print(asc_arr)

arr=[4,0,1,2,8,3]
size=len(arr)
max_prod_of_four(arr,size)
