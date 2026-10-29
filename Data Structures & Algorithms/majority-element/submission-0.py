class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        majel = nums[0]
        for i in nums:
            if cnt == 0:
                majel = i
                cnt = 1
                continue
            if i == majel:
                cnt+=1
            else:
                cnt-=1
        return majel
            
