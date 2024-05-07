# **************************哈希表************************** #
import collections


# 1. 两数之和
class Solution:
    def twoSum(self, nums, target: int):
        for i, x in enumerate(nums):
            for j in range(i + 1, len(nums)):
                if x + nums[j] == target:
                    return [i, j]


# 383. 赎金信
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt = collections.Counter(magazine)
        for c in ransomNote:
            cnt[c] -= 1
            if cnt[c] < 0:
                return False
        return True


# 205. 同构字符串
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2t, t2s = {}, {}
        for a, b in zip(s, t):
            if (a in s2t and s2t[a] != b or
                    b in t2s and t2s[b] != a):
                return False
            s2t[a], t2s[b] = b, a
        return True


# 290. 单词规律
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word2ch = dict()
        ch2word = dict()
        words = s.split()
        if len(pattern) != len(words):
            return False
        for ch, word in zip(pattern, words):
            if (word in word2ch and word2ch[word] != ch) or (ch in ch2word and ch2word[ch] != word):
                return False
            word2ch[word] = ch
            ch2word[ch] = word

        return True


# 242. 有效的字母异位词
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic = collections.defaultdict(int)
        for c in s :
            dic[c] += 1
        for c in t:
            dic[c] -= 1
        for val in dic.values():
            if val != 0:
                return False
        return True


# 49. 字母异位词分组
class Solution:
    def groupAnagrams(self, strs):
        d = collections.defaultdict(list)
        for s in strs:
            d[''.join(sorted(s))].append(s)
        return list(d.values())


# 202. 快乐数
class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit ** 2
            return total_sum

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)

        return n == 1


# 219. 存在重复元素 II
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        s = set()
        for i in range(n):
            if i > k:
                s.remove(nums[i - k - 1])
            if nums[i] in s:
                return True
            s.add(nums[i])
        return False

# 128. 最长连续序列
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        num_set = set(nums)
        for num in num_set:
            if num - 1 not in num_set:
                seq_len = 1
                while (num + 1) in num_set:
                    seq_len += 1
                    num += 1
                res = max(res, seq_len)
        return res




