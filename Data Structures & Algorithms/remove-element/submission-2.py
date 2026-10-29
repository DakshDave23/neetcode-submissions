class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums.sort()
        end = len(nums) - 1
        i = 0
        while(i < end):
            if nums[i] == val:
                nums[i],nums[end] = nums[end],nums[i]
                end-=1
            i+=1
        for i in range(len(nums)):
            if(nums[i] == val):
                return i
        return len(nums)

            
        