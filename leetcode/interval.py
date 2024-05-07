# **************************区间************************** #


# 228. 汇总区间
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        def f(i, j):
            return str(nums[i]) if i == j else f'{nums[i]}->{nums[j]}'

        i = 0
        n = len(nums)
        ans = []
        while i < n:
            j = i
            while j < n - 1 and nums[j + 1] == nums[j] + 1:
                j += 1
            ans.append(f(i, j))
            i = j + 1
        return ans


# 56. 合并区间
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged


# 57. 插入区间
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def merge(intervals):
            intervals.sort()
            ans = [intervals[0]]
            for interval in intervals[1:]:
                if ans[-1][1] < interval[0]:
                    ans.append(interval)
                else:
                    ans[-1][1] = max(ans[-1][1], interval[1])
            return ans

        intervals.append(newInterval)
        return merge(intervals)


# 452. 用最少数量的箭引爆气球
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        cur, ans = points[0][1], 1
        for point in points:
            if point[0] > cur:
                ans += 1
                cur = point[1]
        return ans


# class Solution:
#     def findMinArrowShots(self, points: List[List[int]]) -> int:
#         points.sort()
#         arrow = 0
#         start, end = points[0]
#         for point in points:
#             if point[0] > end:
#                 arrow += 1
#                 start, end = point[0], point[1]
#             else:
#                 start = max(start, point[0])
#                 end = min(end, point[1])
#         arrow += 1
#         return arrow








