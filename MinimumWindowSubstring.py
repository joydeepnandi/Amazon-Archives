#leetcode 76

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        p1, p2 = 0, 0
        minlength = float("inf")
        head = 0
        count = 0
        letter = [0]*256
        
        for char in t:
            key = ord(char)
            letter[key]+=1
        
        while p2<len(s):
            char = s[p2]
            if letter[ord(char)]>0:
                count+=1
            letter[ord(char)]-=1
            p2+=1
            
            while count == len(t):
                
                if p2-p1<minlength:
                    head = p1
                    minlength = p2-p1
                
                if letter[ord(s[p1])]==0:
                    count-=1
                letter[ord(s[p1])]+=1
                p1+=1
        if minlength == float("inf"):
            return ""
        return s[head:head+minlength]
