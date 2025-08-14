# check if array is sorted or not...


'''
To check if an array is sorted in data structures and algorithms (DSA),
the common approach is to verify whether every element is less than or equal to the next one. 
This check ensures the array is in non-decreasing order (sorted ascendingly). 
If any element is found greater than its next element, the array is not sorted.

'''



def is_sorted(arr):
    for i in range(1,len(arr)):
        if arr[i] < arr[i-1]:
            return False
    return True
arr = list(map(int,input().split()))
print(is_sorted(arr))