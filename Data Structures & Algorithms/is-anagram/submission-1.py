class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ls = list(s)
        lt = list(t)
        while len(ls) > 0:
            letter = ls.pop(0)
            print(letter)
            if letter in lt:
                lt.remove(letter)
            else:
                return False
        return True