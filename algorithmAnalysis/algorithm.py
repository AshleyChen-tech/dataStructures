# --------utf-8--------
import time


def sumOfN(n):
    theSum = 0
    for i in range(1, n+1):
        theSum += i

    return theSum

def foo(tom):
    """
    可读性差，不简洁
    """
    fred = 0
    for bill in range(1, tom+1):
        barney = bill
        fred = fred + barney

    return fred

def sumOfN2(n):
    """
    计算运行时间
    """
    start = time.time()

    theSum = 0
    for i in range(1, n+1):
        theSum += i

    end = time.time()

    return theSum, end-start

def sumOfN3(n):
    return (n*(n+1))/2

# 异序词的检测
def anagramSolution1(s1, s2):
    """
    清点法
    """
    alist = list(s2)
    pos1 = 0
    stillOk = True

    while pos1 < len(s1) and stillOk:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 += 1

        if found:
            alist[pos2] = None
        else:
            stillOk = False

        pos1 += 1

    return stillOk

def anagramSolution2(s1, s2):
    """
    排序法
    """
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True
    while pos < len(s1) and matches:
        if alist1[pos] == alist2[pos]:
            pos += 1
        else:
            matches = False

    return matches

def anagramSolution3(s1, s2):
    """
    计数法
    """
    c1 = [0] * 26
    c2 = [0] * 26

    for i in range(len(s1)):
        pos = ord(s1[i] - ord('a'))
        c1[pos] += 1

    for i in range(len(s2)):
        pos = ord(s2[i] - ord('a'))
        c2[pos] += 1

    j = 0
    stillOk = True
    while j < 26 and stillOk:
        if s1[j] == s2[j]:
            j += 1
        else:
            stillOk = False

    return stillOk


print(ord('c')-ord('a'))

# 生成列表的四种方式
def test1(n):
    l = []
    for i in range(n):
        l += [i]
    return l

def test2(n):
    l = []
    for i in range(n):
        l.append(i)
    return l

def test3(n):
    l = [i for i in range(n)]
    return l

def test4(n):
    return list(range(n))


if __name__ == '__main__':
    result = test4(10000)
    print(result)

