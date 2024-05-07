# **************************数学************************** #


# 9. 回文数
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


# 66. 加一
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            digits[i] += 1
            if digits[i] < 10:
                return digits
            else:
                digits[i] %= 10
        return [1] + digits


# 69. x 的平方根
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r, ans = 0, x, -1
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans


# 172. 阶乘后的零
class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        while n >= 5:
            n //= 5
            ans += n
        return ans


# 50. Pow(x, n)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0.0:
            return 1.0
        res = 1
        if n < 0:
            x, n = 1 / x, -n
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res


# 149. 直线上最多的点数
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n, ans = len(points), 1
        for i, x in enumerate(points):
            for j in range(i + 1, n):
                y = points[j]
                cnt = 2
                for k in range(j+1, n):
                    p = points[k]
                    s1 = (y[1] - x[1]) * (p[0] - y[0])
                    s2 = (p[1] - y[1]) * (y[0] - x[0])
                    if s1 == s2: cnt += 1
                ans = max(ans, cnt)
        return ans


#




