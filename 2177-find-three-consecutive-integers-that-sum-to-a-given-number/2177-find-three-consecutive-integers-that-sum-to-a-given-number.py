class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num%3==0:
           number=num/3
           number_before=number-1
           number_after=number+1
           return[number_before,number,number_after]
        else:
             return []
        