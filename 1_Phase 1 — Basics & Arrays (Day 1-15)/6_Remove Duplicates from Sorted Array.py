#
'''
Approach (In-Place, O(n) Time, O(1) Space)
Use one pointer i to track the position of the last unique element found.

Traverse the array with another pointer j starting from the second element.

Whenever you find an element arr[j] that is different from arr[i], 
increment i and update arr[i] to this new unique element.

After the loop finishes, i + 1 is the count of unique elements.

Elements beyond i can be ignored as they are duplicates or overwritten values.

'''


def removeDup(arr):
    if not arr:
        return 0
    i = 0
    for j in range(1,len(arr)):
        if arr[j]!=arr[i]:
            i+=1
            arr[i] = arr[j]
    return i+1
arr = list(map(int,input().split()))
print(removeDup(arr))


        