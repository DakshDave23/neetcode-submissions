class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        mapp = {}

        for idx,val in enumerate(nums):
            mapp[val] = idx
        
        for idx,val in enumerate(nums):
            look = target - val
            if look in mapp and mapp[look] != idx:
                return [idx,mapp[look]]
        return []

        