class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsj = len(nums)
        for i in range(numsj) :
            for j in range(i+1,numsj) :
                if nums[i] + nums[j] == target :
                    return [i,j]
