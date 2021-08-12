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
    

    
