# 1、流浪地球
if __name__ == '__main__':
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

