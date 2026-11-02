class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        n = len(nums)
        if(k == 0):
            return False
        mp = {}
        for i in range(min(k+1,n)):
            mp[nums[i]] = mp.get(nums[i],0) + 1
            if mp[nums[i]] > 1:
                return True
        i = 0
        j = k+1
        while j<n:
            mp[nums[i]] -= 1
            if mp[nums[i]] == 0:
                del mp[nums[i]]
            if(nums[j] in mp):
                return True
            else:
                mp[nums[j]] = mp.get(nums[j],0) + 1
            i+=1
            j+=1
        return False


        