class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        max_len = 0
        l = 0
        r = 0
        while r < len(s):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            max_len = max(max_len, r - l + 1)
            r += 1
        return max_len