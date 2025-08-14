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
function findLargestElement(array A, integer n)
    max = A[0]       // Step 1: Initialize max to first element
    for i from 1 to n-1 do   // Step 2: Traverse array from second element
        if A[i] > max then   // Step 3: Compare with current max
            max = A[i]       // Update max if current element is larger
    return max            // Step 4 & 5: Return the largest element

'''


def largest(arr):
    large = arr[0]
    for i in arr[1:]:
        if  i>large:
            large = i
    return large
arr = list(map(int,input().split()))
print(largest(arr))
print("lergest ele",large)
    
    
    