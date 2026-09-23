class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        col=set()
        postdia=set()
        negdia=set()

        board=[["."]*n for i in range(n)]

        def backtrack(r):

            if r==n:
                copy=["".join(row) for row in board]
                res.append(copy)
                return 

            for c in range(n):
                if c in col or (r+c) in postdia or (r-c) in negdia:
                    continue
                
                col.add(c)
                postdia.add(r+c)
                negdia.add(r-c)
                board[r][c]="Q"


                backtrack(r+1)

                col.remove(c)
                postdia.remove(r+c)
                negdia.remove(r-c)
                board[r][c]="."
        backtrack(0)
        return res
        
