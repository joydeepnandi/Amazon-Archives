#Rotate Matrix// Rotate Array
def Solve(array):
    array.reverse()
    for i in range(len(array)):
        for j in range(1,len(array)):
            array[i][j], array[j][i] = array[j][i], array[i][j]
    return array
    

# Max Contagious SubArray

def Solve(array):
    currentSum = array[0]
    finalSum = array[0]
    
    for i in range(1,len(array)):
        currentSum = max(array[i], currentSum + array[i])
        finalSum = max(finalSum, currentSum)
    return finalSum
    
#Find Dublicate Number

def repeatedNumber(self, A):
        A = list(A)
        if not A:
            return -1
        for i in range(len(A)):
            if A[abs(A[i])] < 0:
                return abs(A[i])
            else:
                A[abs(A[i])] = -A[abs(A[i])]
        return -1
        
#Spiral Traversal
def spiralOrder(self, A):
    sr=0
    er=len(A)-1
    sc=0
    ec=len(A[0])-1
    res=[]
    while sr<=er and sc<=ec:
        
        for col in range(sc,ec+1):
            res.append(A[sr][col])
        
        for row in range(sr+1,er+1):
            res.append(A[row][ec])
        
        for col in reversed(range(sc,ec)):
            if sr==er:
                break
            res.append(A[er][col])
        for row in reversed(range(sr+1,er)):
            if sc==ec:
                break
            res.append(A[row][sc])
        
        sc+=1
        ec-=1
        sr+=1
        er-=1
    return res
    
#merge Intervals

def merge(self, intervals):
        if not intervals:
            return intervals
        intervals = sorted(intervals, key = lambda x:x[0])
        res = []
        for i in range(len(intervals)):
            if res and res[-1][1]>=res[i][0]:
                res[-1][1] = max(res[-1][1],res[i][1])
            else:
                res.append(intervals[i])
        return res
        
#spiral traversal 2

def traversal(a):
    res = [[0 for i in range(A)] for _ in range(A)]
    p=1
    startRow = 0
    startCol = 0
    endRow = A-1
    endCol = A-1
    k = 1
    while startRow<=startCol and endRow<=endCol:
        if p==1:
            for col in range(startCol,endCol+1):
                res[startRow][col] = k
                k+=1
            startRow+=1
        elif p==2:
            for row in range(startRow,endRow+1):
                res[row][endCol] = k
                k+=1
            endCol -= 1
        elif p==3:
            for col in range(endCol,startCol-1,-1):
                res[endRow][col] = k
                k+=1
            endRow -= 1
        else:
            for row in range(endRow,starRow,-1):
                res[row][startCol] = k
                k += 1
            startCol += 1
        p+=1
        p%=4
    return res
