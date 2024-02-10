class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        limit = len(nums) // 3
        result = []
        for num, count in Counter(nums).items():
            if count > limit:
                result.append(num)
        return result
        