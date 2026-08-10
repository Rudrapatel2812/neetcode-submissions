class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result =[]
        m=len(word1)
        n=len(word2)

        for i in range(min(m,n)):
            result.append(word1[i])
            result.append(word2[i])
        
        if m>n:
            result.append(word1[n:])
        else:
            result.append(word2[m:])

        return "".join(result)


        