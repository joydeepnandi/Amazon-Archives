#Maximum Ones After Modification

def solve(arr,B):
    zerocount=0
    start = 0
    ans=0
    for end in range(len(arr)):
        if A[end]==0:
            zerocount+=1

        while zerocount>B:
            if A[start]==0:
                zerocount-=1
            start+=1
        
        if end-start+1>ans:
            ans=end-start+1
    return ans

#counting subarray
#ind the number of subarrays in arr having sum less than B. We may assume that there is no overflow.
def solve(arr,B):
    start,end =0,0
    sums=0
    Count=0
    
    while end<len(arr):
        if (sums + arr[end])>B:
            sums+=arr[end]
            count+=end-start+1
            end+=1
        else:
            sums-=arr[start]
            start+=1
    return count
        
#Subarrays with distinct integers!
#Given an array A of positive integers,call a (contiguous,not necessarily distinct) 
#subarray of A good if the number of different integers in that subarray is exactly B.

def solve(arr,B):
    return countSubArray(arr,B) - countSubArray(arr,B-1)

def countSubArray(arr,B):
    look = collections.defaultdict(int)
    start,end, count, res=0,0,0,0
    
    while end<len(arr):
        look[arr[end]]+=1
        if look[arr[end]==1:
            count+=1
        end+=1
        
        while end>start and count>B:
            look[arr[start]]-=1
            if look[arr[start]]==0:
                count-=1
            start+=1
        
        res += end-1
    return res
    
# Max Continuous Series of 1s
'''
Find the position of zeros which when flipped will produce maximum continuous series of 1s.

For this problem, return the indices of maximum continuous series of 1s in order.

Example:

Input : 
Array = {1 1 0 1 1 0 0 1 1 1 } 
M = 1

Output : 
[0, 1, 2, 3, 4] 
'''

def solve(arr,M):
    start = 0
    maxIdx = [0,0]
    zerocount = 0
    for end in range(len(arr)):
        if arr[end]==0:
            zerocount+=1
        while zerocount>M:
            if arr[start]==0:
                zerocount-=1
            start+=1
        if end - start + 1 > maxIdx[1] - maxIdx[0] +1:
            arr[0] = start
            arr[1] = end
    res = [i for i in range(maxIdx[0],maxIdx[1]+1)]
    return res
        
#Array 3 Pointers
'''
Find i, j, k such that :
max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i])) is minimized.
'''
def solve(A,B,C):
    i,j,k = 0,0,0
    while i<len(A) and j<len(B) and k<len(C):
        ans = min(ans, max(A[i],B[j],C[k]) - min(A[i],B[j],C[k]))
        minElem =  min(A[i],B[j],C[k])
        if minElem == A[i]:
            i+=1
        elif minElem == B[j]:
            j+=1
        else:
            k+=1
    return ans

    
