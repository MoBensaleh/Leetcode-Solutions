class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        idx1 , idx2 = 0,0
        newStr = ""
        while idx1 < len(word1) and idx2 < len(word2):
            newStr += word1[idx1]
            newStr += word2[idx2]
            idx1 +=1
            idx2 +=1

        newStr += word1[idx1:]
        newStr += word2[idx2:]
        return newStr
