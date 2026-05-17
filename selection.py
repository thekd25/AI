def selection_sort(arr):
    n= len(arr)

    for i in range(n):
        min_index=i
        for j in range (i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j

        arr[i],arr[min_index]=arr[min_index], arr[i]

    print(arr)

#min element dundhkar usko swap krta hai i index se (in each pass)
arr=[]
n= int(input("Enter no. of e:"))
for i in range(n):
    x=int(input("Enter the element in arr:"))
    arr.append(x)

selection_sort(arr)