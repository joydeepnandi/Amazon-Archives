
def countPairDivK(array, k):
    modFreq = [0]*k
    for i in array:
        modFreq[i%k]+=1
    
    count = (modFreq[0] * (modFreq[0]  -1) )/2
    i=1
    while i<=(k//2) and i!=(k-1):
        count+= modFreq[i]*modFreq[k-i]
        i+=1
    if k%2 == 0:
        count+= (modFreq[k//2] + modFreq[k//2] -1)/2
    
    return count
