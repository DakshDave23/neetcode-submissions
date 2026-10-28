class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        hashset = [0 for i in range(26)]
        for x in s:
            hashset[ord(x)- ord('a')]+=1
        for x in t:
            hashset[ord(x) - ord('a')]-=1
        
        for x in hashset:
            if(x != 0):
                return False
        return True
        
        
        