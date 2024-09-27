# 逻辑模拟


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
        if s[i].isdigit():
            start = i
            while i < n and s[i].isdigit():
                i += 1
            num_str = s[start:i]
            if i < n and s[i].islower():
                count = int(num_str)
                if count > 2:
                    result.append(s[i] * count)
                else:
                    return "!error"
                i += 1
            else:
                return "!error"
        elif s[i].islower():
            result.append(s[i])
            i += 1
        else:
            return "!error"

    return ''.join(result)


# 3、螺旋数字矩阵



if __name__ == '__main__':
    # wanderingEarth()

    input_string = input().strip()
    print(decompress(input_string))

