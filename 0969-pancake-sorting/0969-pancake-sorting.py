class Solution(object):
    def pancakeSort(self, arr):
        result = []
        n = len(arr)
        
        for i in range(n, 0, -1):
            idx = arr.index(i)
            if idx != i - 1:
                result.append(idx + 1)
                arr[:idx + 1] = reversed(arr[:idx + 1])
                result.append(i)
                arr[:i] = reversed(arr[:i])
        return result           
                
                
            
            
            
            
        