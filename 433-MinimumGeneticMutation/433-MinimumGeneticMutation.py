# Last updated: 5/12/2025, 6:46:18 PM
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:

        bank_set = set(bank)
        visited = set(startGene)
        genes = ['A', 'C', 'G', 'T']
        q = deque([(startGene, 0)])
        if startGene == endGene:
            return 0
        if endGene not in bank_set:
            return -1

        while q: 
            gene, mutations = q.popleft()
            for i in range(len(gene)):
                for c in genes:
                    if c in gene[i]: continue
                    newGene = gene[:i] + c + gene[i+1:]
                    if newGene not in visited and newGene in bank_set:
                        if newGene == endGene:
                            return mutations + 1
                        visited.add(newGene)
                        q.append((newGene, mutations+1))
        return -1
        
        
        