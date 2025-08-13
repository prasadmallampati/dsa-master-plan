#  input are two types static and dynamic ::---

# output will use print, f string

# loops are two type for(finite loop ),while(infinite)

# sum of n natural numbers ::

'''
algorithm ::---

step 1 read n value which is an integer 
step 2 initialize  sum = 0
step 3 use loop from 1 to n , add each number to sum
step 4 output result  

'''


# code 

n = int(input("Enter n value:="))
sum = 0 
for i in range(1,n+1):
    sum += i
print("sum=",sum)
