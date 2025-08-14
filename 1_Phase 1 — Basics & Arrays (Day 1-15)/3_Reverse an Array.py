# Reverse an Array
'''
Reversing an array in data structures and algorithms (DSA)
means rearranging its elements such that the first element becomes the last,
the second element becomes the second-last, and so on. 
The array is modified in place so that its order is reversed.


Common Approach to Reverse an Array (In-Place)
------------------------------------------------
Two pointers method:===

Use two pointers/indexes: one starting at the beginning (start), and the other at the end (end) of the array.

Swap the elements at these pointers.

Move start forward by 1 and end backward by 1.

Repeat this until start is greater than or equal to end.

This approach typically runs in O(n) time complexity,
where n is the size of the array, and uses O(1) extra space since the reversal is done in-place.
'''



# using slicing 
def revArray(arr):
    return arr[::-1]
arr = list(map(int,input("Enter arr").split()))
print("reversed arr=",revArray(arr))




# using two pointers (start,end)
def revArr(arr1):
    start,end=0,len(arr1)-1
    while start<end:
        # we know swap
        arr1[start],arr1[end] =  arr1[end],arr1[start]
        start+=1
        end-=1
arr1 = list(map(int,input("enter arr1").split()))
print("arr1 reversed=",revArr(arr1),arr1)


