# 逻辑模拟
from collections import deque


# 1、流浪地球
def wanderingEarth():
    n, e = map(int, input().split())
    launches = [1001] * n

    for _ in range(e):
        t, p = map(int, input().split())
        launches[p] = t

    for i in range(n):
        for j in range(n):
            innerDis = abs(i - j)
            outerDis = n - innerDis
            minDis = min(innerDis, outerDis)
            launches[j] = min(launches[j], launches[i] + minDis)

    maxT = 0
    lastNum = []

    for p in range(n):
        t = launches[p]
        if t < maxT:
            continue
        if t > maxT:
            maxT = t
            lastNum.clear()
        lastNum.append(p)
    lastNum.sort()
    print(len(lastNum))
    print("".join(map(str, lastNum)))


# 2、一种字符串压缩表示的解压
def decompress(s):
    result = []
    i = 0
    n = len(s)

    while i < n:
        if s[i].isdigit():    # 当前是数字
            start = i
            while i < n and s[i].isdigit():
                i += 1
            num_str = s[start:i]
            if i < n and s[i].islower():
                count = int(num_str)
                if count > 2:    # 超过2的合法数字
                    result.append(s[i] * count)
                else:
                    return "!error"    # 小于等于2，输出错误
                i += 1    # 移动到下一个字母
            else:
                return "!error"    # 数字后面没有字母
        elif s[i].islower():    # 当前是字母，直接添加
            result.append(s[i])
            i += 1
        else:
            return "!error"    # 无效字符

    return ''.join(result)


# 3、螺旋数字矩阵
def creat_spiral_matrix(n, m):
    # 计算每行的列数
    cols = (n + m - 1) // m
    # 创建空矩阵
    matrix = [['*' for _ in range(cols)] for _ in range(m)]

    # 填充数字
    num = 1
    left, right = 0, cols - 1
    top, bottom = 0, m - 1

    while left <= right and top <= bottom:
        # 从左到右：
        for i in range(left, right + 1):
            if num <= n:
                matrix[top][i] = num
                num += 1
        top += 1

        # 从上到下
        for i in range(top, bottom + 1):
            if num <= n:
                matrix[i][right] = num
                num += 1
        right -= 1

        # 从右到左
        if top <= bottom:
            for i in range(right, left - 1, -1):
                if num <= n:
                    matrix[bottom][i] = num
                    num += 1
        bottom -= 1

        # 从下到上
        if left <= right:
            for i in range(bottom, top - 1, -1):
                if num <= n:
                    matrix[i][left] = num
                    num += 1
        left += 1
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(''.join(map(str, row)))


# 4、九宫格按键输入
def process_input(keys):
    # 数字与字母的映射
    key_map = {
        '1': '',
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
        '0': ' '
    }

    mode = 'number'    # 默认模式为数字
    output = []    # 保存输出结果
    current_key = None    # 当前按键
    count = 0    # 当前按键次数

    for char in keys:
        if char == '#':    # 切换模式
            mode = 'english' if mode == 'number' else 'number'
            if current_key and mode == 'number':    # 退出英文模式时输出剩余的数字
                # 处理当前输入
                output.append(current_key * count)
            current_key = None
            count = 0

        elif char == '/':
            if mode == 'english' and current_key:
                # 输出当前按键对应的字母，并重置计数
                output.append(key_map[current_key][(count - 1) % len(key_map[current_key])])
                current_key = None
                count = 0
        elif char.isdigit():
            if mode == 'number':
                output.append(char)  # 数字模式下，直接输出数字
            else:  # 英文模式下
                if current_key == char:
                    # 连续按相同的按键
                    count += 1
                else:
                    # 先处理之前的按键
                    if current_key:
                        output.append(key_map[current_key][(count - 1) % len(key_map[current_key])])
                    # 重置为新的按键
                    current_key = char
                    count = 1

    # 最后一次处理当前输入
    if current_key and mode == 'english':
        output.append(key_map[current_key][(count - 1) % len(key_map[current_key])])

    return ''.join(output)


def print_order(priorities):
    # 将输入的优先级转换为列表，并记录每个任务的初始位置
    queue = deque([(priority, idx) for idx, priority in enumerate(priorities)])
    result = []    # 保存打印顺序

    while queue:
        current = queue.popleft()
        # 检查队列中是否有比当前任务优先级高的任务
        if any(current[0] < item[0] for item in queue):
            queue.append(current)
        else:
            result.append(current[1])

    return result

if __name__ == '__main__':
    # wanderingEarth()

    # input_string = input().strip()
    # print(decompress(input_string))

    # n, m = map(int, input().strip().split())
    # spiral_matrix = creat_spiral_matrix(n, m)
    # print_matrix(spiral_matrix)

    # input_keys = input().strip()
    # print(process_input(input_keys))

    # 输入
    input_priorities = list(map(int, input().strip().split(',')))
    # 计算打印顺序
    order = print_order(input_priorities)
    # 输出打印顺序
    print(','.join(map(str, order)))


