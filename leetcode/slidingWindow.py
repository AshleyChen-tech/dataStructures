# **************************滑动窗口************************** #
from collections import Counter, defaultdict


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


# 209. 长度最小的子数组
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = n + 1
        s = left = 0
        for right, x in enumerate(nums):    # 枚举子数组右端点
            s += x
        #     while s - nums[left] >= target:    # 缩短子数组长度
        #         s -= nums[left]
        #         left += 1
        #     if s >= target:
        #         ans = min(ans, right-left+1)
        # return ans if ans <= n else 0
            while s >= target:    # 满足要求
                ans = min(ans, right - left + 1)
                s -= nums[left]
                left += 1
        return ans if ans <= n else 0


# 30. 串联所有单词的子串
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        from collections import Counter
        if not s or not words:
            return []
        one_word = len(words[0])
        word_num = len(words)
        n = len(s)
        if n < one_word:
            return []
        words = Counter(words)
        res = []
        for i in range(0, one_word):
            cur_cnt = 0
            left = i
            right = i
            cur_Counter = Counter()
            while right + one_word <= n:
                w = s[right:right + one_word]
                right += one_word
                if w not in words:
                    left = right
                    cur_Counter.clear()
                    cur_cnt = 0
                else:
                    cur_Counter[w] += 1
                    cur_cnt += 1
                    while cur_Counter[w] > words[w]:
                        left_w = s[left:left + one_word]
                        left += one_word
                        cur_Counter[left_w] -= 1
                        cur_cnt -= 1
                    if cur_cnt == word_num:
                        res.append(left)
        return res


# 76. 最小覆盖子串
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = defaultdict(int)
        for c in t:
            need[c] += 1
        needCnt = len(t)
        i= 0
        res = (0, float('inf'))
        for j, c in enumerate(s):
            if need[c] > 0:
                needCnt -= 1
            need[c] -= 1
            if needCnt == 0:
                while True:
                    c = s[i]
                    if need[c] == 0:
                        break
                    need[c] += 1
                    i += 1
                if j - i < res[1] - res[0]:
                    res = (i, j)
                need[s[i]] += 1
                needCnt += 1
                i += 1
        return '' if res[1] > len(s) else s[res[0]:res[1]+1]
