class Solution:
    def isPalindrome(self, s: str) -> bool:
        #0,-1
        #1,-2
        #2,-3
        s = s.lower()
        s =''.join(filter(str.isalnum, s))
        print(s)
        l = list(s)
        midpoint = int(len(s)/2)
        # if midpoint == 0:
        #     return True
        i = 0
        while i < midpoint:
            neg = -1*(i+1)
            if l[i] == l[neg]:
                i = i+1
            else:
                return False
        return True
