class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle=="":
            return 0
        elif needle in haystack:
            j=haystack.index(needle)
            return j
        else:
            return -1