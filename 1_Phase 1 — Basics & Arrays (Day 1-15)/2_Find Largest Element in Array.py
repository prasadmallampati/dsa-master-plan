# Find Largest Element in Array


# approach 
'''
step 1 initialize element largest 

step 2 traverse loop from the second element to the end

step 3 compare each element with current max

step 4 after completion traverse hold largest value

step 5 return value 


'''


# code


'''

Step 1: Initialize max to first element
Step 2: Traverse array from second element
Step 3: Compare with current max 
      Update max if current element is larger
Step 4 & 5: Return the largest element

'''

def funLargest(arr):
    # arr not provided case
    if not arr:
        return None
    large = arr[0] 
    # arr provided case 
    for i in arr:
        if i>large:
            large = i
    return large
arr = list(map(int,input("Enter arr:").split()))
print("largest=",funLargest(arr))
    