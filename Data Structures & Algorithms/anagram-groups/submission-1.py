class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return []
        
        groups = {}

        for word in strs:
            chars_list = list(word)
            chars_list.sort()

            key = "".join(chars_list)

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        result: List[List[str]] = []

        for key in groups:
            result.append(groups[key])
        
        return result