class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        t= sorted(nums)
        res=[]
        for i in nums:
            res.append(t.index(i))
        return res