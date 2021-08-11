#jumpgame 1
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m=0
        for idx,n in enumerate(nums):
            if idx>m:
                return False
            m=max(m,idx+n)
        return True

#jumpgame2

class Solution:
    def jump(self, nums: List[int]) -> int:
        if nums[0] == 0:
            return 0
        if len(nums)==1:
            return 0
        
        dp = [0 for i in range(len(nums))]
        
        for i in range(len(nums)):
            dp[i] = nums[i] + i
        
        steps = 1
        maxRight = dp[0]
        nextIdx = -1
        
        for i in range(len(nums)-1):
            nextIdx = max(nextIdx, dp[i])
            
            if maxRight== i:
                steps+=1
                maxRight = nextIdx
        return steps
        
#jumpgame 3
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        vis=[False]*len(arr)
        return self.dfs(arr,vis,start)
    
    def dfs(self,arr,vis,start):
        n=len(arr)
        if start>=n or start<0 or vis[start]:
            return False
        if arr[start]==0:
            return True
        vis[start]=True
        return self.dfs(arr,vis,start+arr[start]) or self.dfs(arr,vis,start-arr[start])
        
