class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs is None:
            return []

        
        groups = defaultdict(list)
        for word in strs: 
            counts = [0] * 26

            for ch in word:
                counts[ord(ch) - ord('a')] += 1

            signature = tuple(counts)
            groups[signature].append(word)
        return list(groups.values())