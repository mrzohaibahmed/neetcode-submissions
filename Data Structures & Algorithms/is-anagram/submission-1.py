class Solution:
    def isAnagram(self,s,t):
        if len(s)!=len(t):
            return False
        
        Counts, Countt ={},{}


        for i in range(len(s)):
            Counts[s[i]]=Counts.get(s[i],0)+1
            Countt[t[i]]=Countt.get(t[i],0)+1
        return Counts==Countt
