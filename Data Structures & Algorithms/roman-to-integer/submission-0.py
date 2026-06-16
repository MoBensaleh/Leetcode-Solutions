class Solution:
    def romanToInt(self, s: str) -> int:
        # XLIX -> {X: 10, L: 50, I: 1}

        # index 0: -10
        # index 1: 40 
        # index 2: 39
        # index 3: 49 

        if s is None or len(s) == 0:
            return 0

        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0

        for i in range(len(s)):
            curr_value = values[s[i]]
            if i + 1 < len(s):
                next_value = values[s[i+1]]

                if curr_value < next_value:
                    total = total - curr_value

                else:
                    total = total +curr_value

            else:
                total = total+ curr_value
        return total


