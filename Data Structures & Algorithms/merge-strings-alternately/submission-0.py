class Solution:
    def mergeAlternately(self, word1, word2):
        first = 0
        second = 0
        result=""

        while first < len(word1) or second < len(word2):

            if first < len(word1):
                result += word1[first]
                first = first+1

            if second < len(word2):
                result +=word2[second]
                second = second+1

        return result  