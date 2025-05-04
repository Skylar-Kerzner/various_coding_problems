#Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] 
#if and only if either (a == c and b == d), or (a == d and b == c) 
# that is, one domino can be rotated to be equal to another domino.

#Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

 #Example 1:
#Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
#Output: 1

#Example 2:
#Input: dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2], [2, 2]]
#Output: 4

def numEquivDominoPairs(dominos: list[list[int]]) -> int:
    count = 0
    for i in range(len(dominos)-1):
        for j in range(i+1,len(dominos)):
            if set(dominos[i])==set(dominos[j]):
                count+=1
    return count



assert 1 == numEquivDominoPairs(dominos = [[1,2],[2,1],[3,4],[5,6]])

assert 4 == numEquivDominoPairs(dominos = [[1,2],[1,2],[1,1],[1,2],[2,2], [2,2]])

print("Tests passed")

from collections import defaultdict

def numEquivDominoPairsEfficient(self, dominoes: list[list[int]]) -> int:
        count = 0
        freq = defaultdict(int)
        
        for a, b in dominoes:
            key = tuple(sorted((a, b)))  # normalize so [1,2] and [2,1] are treated the same
            count += freq[key]          # each time we see this key again, it forms a new pair with each previous
            freq[key] += 1
        
        return count

assert 1 == numEquivDominoPairs(dominos = [[1,2],[2,1],[3,4],[5,6]])

assert 4 == numEquivDominoPairs(dominos = [[1,2],[1,2],[1,1],[1,2],[2,2], [2,2]])

print("Tests passed efficiently")

