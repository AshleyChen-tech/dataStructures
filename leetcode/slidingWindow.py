# **************************滑动窗口************************** #


# 3. 无重复字符的最长子串
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        record = {}
        res, start = 0, 0
        for end in range(len(s)):
            if s[end] in record:
                start = max(start, record[s[end]] + 1)
            record[s[end]] = end
            res = max(res, end - start + 1)
        return res