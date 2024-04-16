import math


# HJ10 字符个数统计
def numOfString(str1):
    sstr = str1.strip()
    Kword = ''
    for i in sstr:
        if i not in Kword and 0 <= ord(i) <= 127:
            Kword += i
    return len(Kword)


# HJ46 截取字符串
def interceptSrting(str1, num):
    sstr = str1.strip()
    length = len(sstr)
    if length >= num:
        return sstr[:num]
    else:
        return 'wrong number'


# HJ60 查找组成一个偶数最接近的两个素数
def evenToPrimenumber(num):
    def isPrime(x):    # 计算是否是素数
        for i in range(2, x//2+1):
            if x % i == 0:
                return False
        return True
    num = num
    list1 = []
    for i in range(num//2, num):
        if isPrime(i) and isPrime(num-i):
            list1.append(i)
            list1.append(num-i)
            return list1
        else:
            continue


# HJ40 统计字符
def statistics(str1):
    sstr = str1
    char, blanket, num, other = 0, 0, 0, 0
    for s in sstr:
        if s.isalpha():
            char += 1
        elif s == ' ':
            blanket += 1
        elif s.isdigit():
            num += 1
        else:
            other += 1
    return char, blanket, num, other


# HJ14 字符串排序
def sortString(num):
    strlist = []
    for _ in range(num):
        str1 = input('Enter a string: ')
        strlist.append(str1)
    strlist.sort()
    return strlist


# HJ5 进制转换
def hex(num):
    return int(num, base=16)


# 找出字符串中第一个只出现一次的字符
def onlyone(str1):
    for i in str1:
        if str1.count(i) == 1:
            return i
    else:
        return -1


# HJ58 输入n个整数，输出其中最小的K个
def printTwo(num1, num2):
    m, n = map(int, num1.split(' '))
    num = list(map(int, num2.split(' ')))
    num.sort()
    return ' '.join(map(str, num[:n]))


# HJ81 字符串字符匹配
def clusionstr(str1, str2):
    a, b = set(str1), set(str2)
    if a & b == a:
        return True
    else:
        return False


if __name__ == '__main__':
    inputStr1 = input('Enter a string: ')
    inputStr2 = input('Enter a string: ')
    # inputNum = int(input('Enter a number: '))
    result = clusionstr(inputStr1, inputStr2)
    print(result)

