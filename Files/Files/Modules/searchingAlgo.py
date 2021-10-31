import math
## linear search
def linear_search(A,key):
    occurences = []
    for i in range(len(A)):
        if A[i] == key:
            occurences.append(i)
    return occurences
### Binary Search
##
#
def binary_search_counter(A,low,high,key):
    occur_binary = []
    index = binary_search(A,low,high,key)
    if index == -1:
        return None
    
    occur_binary.append(index)
    left = index-1
    while left>=0 and A[left]==key:
        occur_binary.append(left)
        left-=1
    
    right = index+1
    while right<len(A) and A[right]==key:
        occur_binary.append(right)
        right+=1
    occur_binary.sort()
    return occur_binary


def binary_search(A,low,high,key):
    if low!=high or key == A[low]:
        mid = (low+high)//2
        if A[mid] == key:
            return mid
        elif key<A[mid]:    
            return binary_search(A,low,mid,key)
        else:
            return binary_search(A,mid+1,high,key)
    
    return -1
### Jump Search
##
#
def linearJump_search(A,end,key):
    occurences = []
    for i in range(end+1):
        if A[i] == key:
            occurences.append(i)
    return occurences

def jump_search(A,key):
    jumpsize = int(math.sqrt(len(A)))
    #print("jump:",jumpsize)
    end = 0
    found = False
    i = 0
    while i<=len(A)-1 and found == False:
        
        if A[i]>key and i>=jumpsize: 
            end = i
            found = True
        i+=jumpsize
        print(i)
        
    if found == False:
        if A[len(A)-1]==key:
            end = len(A)-1
            found = True

    return linearJump_search(A,end,key)