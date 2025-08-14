# two sum



'''
Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target. It is assumed there is exactly one solution, and you may not use the same element twice.

Common Approaches to Solve Two Sum
1. Brute Force (Nested Loops)
Iterate over every pair of elements.

Check if their sum equals the target.

Time complexity: O(n²), Space complexity: O(1).

'''



def twoSum(num,target):
    n = len(num)
    for i in range(n):
        for j in range(i+1,n):
            if num[i] + num [j] == target:
                return [num[i],num[j]]  
    return None
num = list(map(int,input("enter num values:").split()))
target = int(input("Enter target value:"))
print("two sum=",twoSum(num,target))