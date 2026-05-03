class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_chars = set()

        left = 0

        longest_length = 0

        for right in range(len(s)):
            curr_char = s[right]

            while curr_char in window_chars:
                window_chars.remove(s[left])
                left += 1
            
            window_chars.add(curr_char)
            current_length = right-left+1
            if current_length > longest_length:
                longest_length = current_length
        return longest_length