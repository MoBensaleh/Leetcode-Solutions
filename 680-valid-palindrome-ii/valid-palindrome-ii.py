class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r =0 , len(s)-1

        while l<r:
            if s[l] != s[r]:
                sR, sL= s[l+1:r+1], s[l:r]
                return (sR == sR[::-1]) or (sL == sL[::-1])   
            l+=1
            r-=1     
        return True
