class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        worlen = len(words[0])
        count = collections.Counter(words)
        ws = len(words) * worlen
        out = []
        for i in range(len(s) - ws + 1):
            temp = s[i:i+ws]
            temp = [temp[j:j+worlen] for j in range(0, ws, worlen)]
            if collections.Counter(temp) == count:
                out.append(i)
        return out