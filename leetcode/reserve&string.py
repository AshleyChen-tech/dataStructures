import collections
from random import choice


# **************************数组&字符串************************** #
# 88. 合并两个有序数组
class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        p1, p2, p = m - 1, n - 1, m + n - 1
        while p2 >= 0:  # nums2 还有要合并的元素
            # 如果 p1 < 0，那么走 else 分支，把 nums2 合并到 nums1 中
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]  # 填入 nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]  # 填入 nums2[p1]
                p2 -= 1
            p -= 1  # 下一个要填入的位置


# 27. 移除元素
class Solution:
    def removeElement(self, nums, val: int) -> int:
        a = 0
        b = 0

        while a < len(nums):
            if nums[a] != val:
                nums[b] = nums[a]
                b += 1
            a += 1

        return b


# 26. 删除有序数组中的重复项
class Solution:
    def removeDuplicates(self, nums) -> int:
        if not nums:
            return 0

        n = len(nums)
        fast = slow = 1
        while fast < n:
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        return slow


# 80. 删除有序数组中的重复项 II
class Solution(object):
    def removeDuplicates(self, nums):
        slow = 0
        for fast in range(len(nums)):
            if slow < 2 or nums[fast] != nums[slow - 2]:
                nums[slow] = nums[fast]
                slow += 1
        return slow


# 169. 多数元素
class Solution:
    def majorityElement(self, nums) -> int:
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)


# 189.轮转数组
class Solution:
    def rotate(slef, nums, k):
        # 方法一
        for _ in range(k):
            nums.insert(0, nums.pop())

        # 方法二
        # k = k % len(nums)
        # nums[:] = nums[-k:] + nums[:-k]


# 121. 买卖股票的最佳时机 I
class Solution:
    def maxProfit(self, prices) -> int:
        # 方法一
        minprice = float('inf')
        maxprofit = 0
        for price in prices:
            minprice = min(minprice, price)
            maxprofit = max(maxprofit, price - minprice)
        return maxprofit


# 122. 买卖股票的最佳时机 II
class Solution:
    def maxProfit(self, prices) -> int:
        profit = 0
        for i in range(1, len(prices)):
            tmp = prices[i] - prices[i-1]
            if tmp > 0:
                profit += tmp
        return profit


# 55. 跳跃游戏
class Solution:
    def canJump(self, nums) -> bool:
        end = 0
        n = len(nums)
        for i in range(n-1):
            step = nums[i]
            if i > end:
                return False
            end = max(end, i+step)
        return end >= n-1


# 45. 跳跃游戏 II
class Solution:
    def jump(self, nums) -> int:
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1

        return step


# 274. H 指数
class Solution:
    def hIndex(self, citations) -> int:
        n = len(citations)
        cnt = [0] * (n + 1)
        for c in citations:
            cnt[min(c, n)] += 1
        s = 0
        for i in range(n, -1, -1):
            s += cnt[i]
            if s >= i:
                return i


# 13. 罗马数字转整数
class Solution:
    SYMBOL_VALUES = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def romanToInt(self, s: str) -> int:
        ans = 0
        n = len(s)
        for i, ch in enumerate(s):
            value = Solution.SYMBOL_VALUES[ch]
            if i < n - 1 and value < Solution.SYMBOL_VALUES[s[i + 1]]:
                ans -= value
            else:
                ans += value

        return ans


# 58. 最后一个单词的长度
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # 方法一
        # return len(s.strip().split()[-1])

        # 方法二
        ans = 0
        for c in s[::-1]:
            if c == ' ':
                if ans:
                    break
                continue
            ans += 1
        return ans


# 14. 最长公共前缀
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not str: return " "
        length, count = len(strs[0]), len(strs)
        for i in range(length):
            c = strs[0][i]
            if any(i == len(strs[j]) or strs[j][i] != c for j in range(1, count)):
                return strs[0][:i]
        return strs[0]


# 28. 找出字符串中第一个匹配项的下标
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Func：计算偏移表
        def calShiftMat(st):
            dic = {}
            for i in range(len(st) - 1, -1, -1):
                if not dic.get(st[i]):
                    dic[st[i]] = len(st) - i
            dic["ot"] = len(st) + 1
            return dic

        # 其他情况判断
        if len(needle) > len(haystack):
            return -1
        if needle == "":
            return 0

        # 偏移表预处理
        dic = calShiftMat(needle)
        idx = 0

        while idx + len(needle) <= len(haystack):
            # 待匹配字符串
            str_cut = haystack[idx:idx + len(needle)]

            # 判断是否匹配
            if str_cut == needle:
                return idx
            else:
                # 边界处理
                if idx + len(needle) >= len(haystack):
                    return -1

                # 不匹配情况下，根据下一个字符的偏移量，移动idx
                cur_c = haystack[idx + len(needle)]
                if dic.get(cur_c):
                    idx += dic[cur_c]
                else:
                    idx += dic['ot']
        return -1 if idx + len(needle) >= len(haystack) else idx


# 380. O(1) 时间插入、删除和获取随机元素
class RandomizedSet:
    def __init__(self):
        self.nums = []
        self.indices = {}


    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False
        self.indices[val] = len(self.nums)
        self.nums.append(val)
        return True


    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        id = self.indices[val]
        self.nums[id] = self.nums[-1]
        self.indices[self.nums[id]] = id
        self.nums.pop()
        del self.indices
        return True


    def getRandom(self) -> int:
        return choice(self.nums)


# 238. 除自身以外数组的乘积
class Solution:
    def productExceptSelf(self, nums):
        ans, tmp = [1] * len(nums), 1
        for i in range(1, len(nums)):
            # 下三角
            ans[i] = ans[i - 1] * nums[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            # 上三角
            tmp *= nums[i + 1]
            ans[i] *= tmp
        return ans


# 134. 加油站
class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        # 方法一
        # n = len(gas)
        # cur_sum = 0
        # min_sum = float('inf')

        # for i in range(n):
        #     cur_sum += gas[i] - cost[i]
        #     min_sum = min(min_sum, cur_sum)

        # if cur_sum < 0: return -1
        # if min_sum >= 0: return 0

        # for j in range(n - 1, 0, -1):
        #     min_sum += gas[j] - cost[j]
        #     if min_sum >= 0:
        #         return j

        # return -1

        # 方法二
        have = gas[0] - cost[0]
        minnum = [have, 0]
        for i in range(1, len(gas)):
            have = gas[i] - cost[i] + have
            if have <= minnum[0]:
                minnum = [have, i]
        if have < 0:
            return -1
        return (minnum[1] + 1) % len(gas)


# 135. 分发糖果
class Solution:
    def candy(self, ratings) -> int:
        left = [1 for _ in range(len(ratings))]
        right = left[:]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
        count = left[-1]
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right[i] = right[i + 1] + 1
            count += max(left[i], right[i])
        return count

#42. 接雨水
class Solution:
    def trap(self, height) -> int:
        # 单调栈
        ans = 0
        st = []
        for i, h in enumerate(height):
            while st and h >= height[st[-1]]:
                bottom_h = height[st.pop()]
                if not st:
                    break
                left = st[-1]
                dh = min(height[left], h) - bottom_h
                ans += dh * (i - left - 1)
            st.append(i)
        return ans


#12. 整数转罗马数字
class Solution:
    def intToRoman(self, num: int) -> str:
        # 暴力匹配
        # M  = ["", "MM", "MMM", "MMM"] # 1000, 2000, 3000
        # C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"] #100~900
        # X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"] # 10~90
        # I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"] # 1~9
        # return M[num//1000] + C[(num%1000)//100] + X[(num%100)//10] + I[num%10]

        # 贪心（使用哈希表，从小到大排序）
        hashmap = {1000: 'M',
                   900: 'CM',
                   500: 'D',
                   400: 'CD',
                   100: 'C',
                   90: 'XC',
                   50: 'L',
                   40: 'XL',
                   10: 'X',
                   9: 'IX',
                   5: 'V',
                   4: 'IV',
                   1: 'I'
                   }
        res = ''
        for key in hashmap:
            if num // key != 0:
                count = num // key
                res += hashmap[key] * count
                num %= key
        return res


# 151. 反转字符串中的单词
class Solution:
    def reverseWords(self, s: str) -> str:
        # s = s.strip()
        # sList = s.split()
        # sList.reverse()
        # return " ".join(sList)

        # 双指针
        s = s.strip()
        i = j = len(s) - 1
        res = []
        while i >= 0:
            # 搜索首个空格
            while i >= 0 and s[i] != " ":
                i -= 1
            res.append(s[i + 1: j + 1])
            # 跳过中间空格
            while i >= 0 and s[i] == " ":
                i -= 1
            j = i  # j指向下个单词的尾字符
        return ' '.join(res)


# 6. Z 字形变换
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1:
                flag = -flag
            i += flag
        return "".join(res)


# 68. 文本左右对齐



if __name__ == '__main__':
    citations = [3, 0, 6, 1, 5]
    print(Solution().hIndex(citations))


# **************************矩阵************************** #



# **************************二叉树层次遍历************************** #


# **************************二叉搜索树************************** #


# **************************图************************** #


# **************************图的广度优先搜索************************** #


# **************************字典树************************** #


# **************************回溯************************** #


# **************************分治************************** #


# **************************Kadane 算法************************** #



# **************************堆************************** #



# **************************位运算************************** #




# **************************多维动态规划************************** #

