# 数学问题
from collections import defaultdict
import math

# 1、正方形个数
def count_squares(coords):
    N = len(coords)
    count = 0
    coord_set = set(coords)  # 使用 set 来快速查找坐标是否存在

    # 遍历所有点对 (A, B)
    for i in range(N):
        for j in range(i + 1, N):
            # 获取 A 和 B 点
            x1, y1 = coords[i]
            x2, y2 = coords[j]

            # 计算向量 AB 的方向向量
            dx, dy = x2 - x1, y2 - y1

            # 根据 AB 的向量，计算可能的两个对称点 C 和 D
            # 对称点 C 和 D 通过旋转向量 AB 90度顺时针或逆时针得到
            cx1, cy1 = x1 - dy, y1 + dx
            cx2, cy2 = x2 - dy, y2 + dx

            # 检查点 C 和 D 是否存在于原始点集中
            if (cx1, cy1) in coord_set and (cx2, cy2) in coord_set:
                count += 1

            # 再次旋转得到另外一组对称点 C 和 D
            cx1, cy1 = x1 + dy, y1 - dx
            cx2, cy2 = x2 + dy, y2 - dx

            # 检查另一组点 C 和 D 是否存在于原始点集中
            if (cx1, cy1) in coord_set and (cx2, cy2) in coord_set:
                count += 1

    # 每个正方形被计算了两次，因此需要除以 2
    return count // 2


# 2、矩形相交的面积
def rectangle_intersection_area(rects):
    # 解压矩形坐标
    (x1_a, y1_a, w_a, h_a), (x1_b, y1_b, w_b, h_b), (x1_c, y1_c, w_c, h_c) = rects

    # 计算每个矩形的右下角坐标
    x2_a, y2_a = x1_a + w_a, y1_a - h_a
    x2_b, y2_b = x1_b + w_b, y1_b - h_b
    x2_c, y2_c = x1_c + w_c, y1_c - h_c

    # 计算交集区域的左右边界和上下边界
    x_left = max(x1_a, x1_b, x1_c)
    x_right = min(x2_a, x2_b, x2_c)

    y_top = min(y1_a, y1_b, y1_c)
    y_bottom = max(y2_a, y2_b, y2_c)

    # 判断是否有交集
    if x_left < x_right and y_bottom < y_top:
        # 存在交集，计算面积
        area = (x_right - x_left) * (y_top - y_bottom)
        return area
    else:
        # 没有交集
        return 0


# 3、工号问题
def minimum_digits(X, Y):
    # 字母组合数量
    letter_combinations = 26 ** Y

    # 计算所需的数字组合数量
    if letter_combinations >= X:
        return 0

    # 计算Z下界
    required_combinations = X / letter_combinations
    Z = math.ceil(math.log10(required_combinations))

    return Z


if __name__ == '__main__':
    # # 输入部分
    # N = int(input())
    # coords = []
    # for _ in range(N):
    #     x, y = map(int, input().split())
    #     coords.append((x, y))  # 用 list 存储输入的坐标
    #
    # # 输出结果
    # print(count_squares(coords))

    # # 输入部分
    # rects = []
    # for _ in range(3):
    #     x, y, w, h = map(int, input().split())
    #     rects.append((x, y, w, h))
    #
    # # 输出结果
    # print(rectangle_intersection_area(rects))

    # 输入
    X, Y = map(int, input().split())

    # 输出
    print(minimum_digits(X, Y))



