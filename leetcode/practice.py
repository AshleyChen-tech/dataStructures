#  5. 最长回文子串
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        max_len = 1
        begin = 0
        # dp[i][j] 表示 s[i..j] 是否是回文串
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        # 递推开始
        # 先枚举子串长度
        for L in range(2, n + 1):
            # 枚举左边界，左边界的上限设置可以宽松一些
            for i in range(n):
                # 由 L 和 i 可以确定右边界，即 j - i + 1 = L 得
                j = L + i - 1
                # 如果右边界越界，就可以退出当前循环
                if j >= n:
                    break

                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                # 只要 dp[i][L] == true 成立，就表示子串 s[i..L] 是回文，此时记录回文长度和起始位置
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i
        return s[begin:begin + max_len]


# ---------------------------------------- 分割线 ----------------------------------------
# 每日一题


# 2739. 总行驶距离
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        ans = 0
        while mainTank >= 5:
            mainTank -= 5
            ans += 50
            if additionalTank:
                additionalTank -= 1
                mainTank += 1
        return ans + 10 * mainTank


 # 1146. 快照数组（哈希表+二分查找）


# 2639.查询网格图中每一列的宽度


#1017. 负二进制转换
class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0 or n == 1:
            return str(n)
        res = []
        while n:
            remainder = n & 1
            res.append(str(remainder))
            n -= remainder
            n //= -2
        return ''.join(res[::-1])


# 1329. 将矩阵按对角线排序


# 2798. 满足目标工作时长的员工数目
class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        ans = 0
        max_value = max(hours)
        if target > max_value:
            return 0
        for i in range(len(hours)):
            if target <= hours[i]:
                ans += 1
        return ans


# 2462. 雇佣 K 位工人的总代价


# 857. 雇佣 K 名工人的最低成本


# 1235. 规划兼职工作


# 1652. 拆炸弹
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ans = [0] * n
        r = k + 1 if k > 0 else n
        k = abs(k)
        s = sum(code[r - k: r])
        for i in range(n):
            ans[i] = s
            s += code[r % n] - code[(r - k) % n]
            r += 1
        return ans



