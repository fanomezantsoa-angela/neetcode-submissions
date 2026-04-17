class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashdiff = {}
        for i in range(len(nums)):
            difference = target - nums[i]

            if difference in hashdiff:
                print(hashdiff)
                return [hashdiff[difference], i]
            hashdiff[nums[i]] = i
                
        