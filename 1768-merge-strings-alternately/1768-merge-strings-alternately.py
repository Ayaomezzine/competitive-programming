class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged = ""
        i, j = 0, 0

        while i < len(word1) and j < len(word2):
            merged += word1[i] + word2[j]
            i += 1
            j += 1

        # Append any remaining characters from word1
        while i < len(word1):
            merged += word1[i]
            i += 1

        # Append any remaining characters from word2
        while j < len(word2):
            merged += word2[j]
            j += 1

        return merged