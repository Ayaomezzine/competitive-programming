class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        defanged_address = address.replace('.', '[.]')
        return defanged_address