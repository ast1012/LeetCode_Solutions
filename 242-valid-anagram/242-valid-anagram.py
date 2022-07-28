class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        flag = 0
        a = sorted(s)
        b = sorted(t)
        if a==b:
            flag = 1
        else:
            flag = 0
        if flag==1:
            return bool(flag)
        elif flag==0:
            return bool(flag)