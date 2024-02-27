class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        n = {i: x for x, i in enumerate(nums)}
        l, r = 0, len(nums) - 1
        print(n)
        for ind, val in enumerate(nums):
            t = target - val
            if t in n and ind != n[t]:
                return [ind, n[t]]
