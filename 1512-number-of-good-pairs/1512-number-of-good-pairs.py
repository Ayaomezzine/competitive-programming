class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        good_pairs = 0
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    good_pairs += 1

        return good_pairs