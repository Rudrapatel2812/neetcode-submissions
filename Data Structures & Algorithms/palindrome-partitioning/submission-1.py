class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]

        def is_pali(curr):
            return curr==curr[::-1]

        def backtrack(start,path):
            if start==len(s):
                res.append(path.copy())
                return 

            for end in range(start+1,len(s)+1):
                if is_pali(s[start:end]):
                    backtrack(end, path+[s[start:end]])
        
        backtrack(0,[])

        return res

                


        