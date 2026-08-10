class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr=''
        for c in s:
            if c.isalnum():
                newstr+=c.lower()

        # s=[ i for i in s.lower() if i.isalnum()]
        return newstr==newstr[::-1]

       

        