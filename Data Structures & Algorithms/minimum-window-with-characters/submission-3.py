class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        need={}
        for i in range(len(t)):
            need[t[i]]=need.get(t[i],0)+1

        i = 0
        start = 0
        man = float("inf")

        window = {}

        have = 0
        need_count = len(need)

        for j in range(len(s)):
            window[s[j]]=window.get(s[j],0)+1

            if s[j] in need and window[s[j]] == need[s[j]]:
                have += 1

            while have == need_count:
                if (j-i+1)<man:
                    man=j-i+1
                    start=i

                window[s[i]]-=1
                if s[i] in need and window[s[i]] < need[s[i]]:
                    have -= 1
                i+=1

        if man == float('inf'):
            return ""

        return s[start:start+man]
            

                

                
            
                



