class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        carry = 1
        while i >= 0 and carry > 0:
            new_val = digits[i] + carry
            digits[i] = new_val % 10
            carry = new_val // 10
            i -= 1
        
        if carry > 0:
            digits.insert(0, carry)
        return digits