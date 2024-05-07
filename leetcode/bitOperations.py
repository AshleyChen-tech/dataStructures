# # **************************位运算************************** #
#
#
# # 67. 二进制求和
# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         x, y = int(a, 2), int(b, 2)
#         while y:
#             answer = x ^ y
#             carry = (x & y) << 1
#             x, y = answer, carry
#         return bin(x)[2:]
#
# # 136. 只出现一次的数字
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         x = 0
#         for num in nums:
#             x ^= num
#         return x
#
#
# # 190. 颠倒二进制位
# class Solution:
#     def reverseBits(self, n: int) -> int:
#         res = 0
#         for _ in range(32):
#             res = (res << 1) | (n & 1)
#             n >>= 1
#         return res
#
#
# # 191. 位1的个数
# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         # n = bin(n)
#         # return n.count('1')
#         res = 0
#         # while n:
#         #     res += n & 1
#         #     n >>= 1
#         # return res
#         while n:
#             res += 1
#             n &= n - 1
#         return res
#
#
# # 137. 只出现一次的数字 II
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         ones, twos = 0, 0
#         for num in nums:
#             ones = ones ^ num & ~twos
#             twos = twos ^ num & ~ones
#         return ones


# 数字范围按位与
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        while left < right:
            left = left >> 1
            right = right >> 1
            shift += 1
        return left << shift
        # while left < right:
        #     left = left & (left - 1)
        # return n


if __name__ == '__main__':
    solution = Solution()
    result = solution.rangeBitwiseAnd(12, 14)
    print(result)