class Solution:
    def flipgame(self, front: List[int], back: List[int]) -> int:
        check = set()
        for i in range(len(front)):
            if front[i] == back[i]:
                check.add(front[i])
        result = float("inf")
        for num in (front + back):
            if num not in check:
                result = min(result, num)
        return result if result != float("inf") else 0