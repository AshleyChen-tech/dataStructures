import sys


# HJ12 字符串反转(切片)
def backword1(str1):
    return str1[::-1]


def backword(str1):
    slen = len(str1)
    sstr = ""
    for i in range(slen):
        sstr += str1[slen - i - 1]
    return sstr


# HJ11 数字颠倒
def convertnum(num):
    return num[::-1]


# HJ54 表达式求值
def calculate(str1):
    return eval(str1)


# HJ106 字符逆序
def convertString(str1):
    # return str1[::-1]
    slen = len(str1)
    sstr = ""
    for i in range(slen):
        sstr += str1[slen - i - 1]
    return sstr


# HJ76 尼科彻斯定力
def nikechesi(num):
    """等差数列"""
    reslist = [str(i) for i in range(num**2-num+1, num**2+num, 2)]
    return '+'.join(reslist)


# 最后一个字符串长度
def lastString(str1):
    strlist = str1.split(' ')
    return strlist[-1]


# HJ75 公共子串计算
def publicString(str1, str2):
    num = 0
    for i in range(len(str1)):
        if str1[i-num:i+1] in str2:
            num += 1
    return num


# HJ86 求最大连续bit数
def continuousBit(num):
    toString = str(bin(num))
    toString = toString[2:].split('0')
    numList = []
    for i in range(len(toString)):
        numList.append(len(toString[i]))
    result = max(numList)
    return result


# HJ85 最长回文子串
def longPalindrome(str1):
    for length in range(len(str1), -1, -1):
        for index in range(0, len(str1)-length+1):
            substr = str1[index:index+length]
            if substr == substr[::-1]:
                return len(substr)


# HJ100 等差数列
def arithmeticSequence(num):
    return 2*num + num*(num-1)*3//2


# HJ87 密码强度等级
def classOfpassword(password):
    num, up_char, down_char, other, score = 0, 0, 0, 0, 0
    srt_data = password.strip()
    for char in srt_data:
        if char.isdigit():    # 判断是否是数字
            num += 1
        elif char.isalpha():    # 判断是否是字母
            if char.upper() == char:
                up_char += 1    # 大写字母
            else:
                down_char += 1    # 小写字母
        else:
            other += 1    # 符号
    # 密码长度
    if len(srt_data) < 5:
        score += 5
    elif len(srt_data) < 8:
        score += 10
    else:
        score += 25
    # 密码大小写
    if up_char == 0 and down_char == 0:
        pass
    elif (up_char != 0 and down_char == 0) or (up_char == 0 and down_char != 0):
        score += 10
    else:
        score += 20
    # 密码数字个数
    if num == 0:
        pass
    elif num == 1:
        score += 10
    else:
        score += 20
    # 符号个数
    if other == 0:
        pass
    elif other == 1:
        score += 10
    else:
        score += 25
    # 奖励
    if num != 0 and (up_char + down_char) != 0 and other == 0:
        score += 2
    elif num != 0 and up_char != 0 and down_char != 0 and other != 0:
        score += 5
    elif num != 0 and (up_char + down_char) != 0 and other != 0:
        score += 3
    if score >= 90:
        return ('VERY_SECURE')
    elif score >= 80:
        return 'SECURE'
    elif score >= 70:
        return 'VERY_STRONG'
    elif score >= 60:
        return 'STRONG'
    elif score >= 50:
        return 'AVERAGE'
    elif score >= 25:
        return 'WEAK'
    else:
        return 'VERY_WEAK'


if __name__ == '__main__':
    inputstr1 = input('Enter a string: ')
    # inputstr2 = input('Enter a string: ')
    # inputnum = int(input('Enter a number: '))
    print(classOfpassword(inputstr1))
    # lastWord = lastString(inputstr)
    # length = len(lastWord)
    # if inputstr.isalpha() and inputstr.lower():
    # print(f"last string is {lastWord}\n"
    #       f"length is {length}")

    # 持续运行&捕获异常
    # while True:
    #     try:
    #         inputstr = input('Enter a string: ')
    #         # inputnum = int(input('Enter a number: '))
    #         # if inputstr.isalpha() and inputstr.lower():
    #         print('last string is', lastString(inputstr),
    #               'length is', len(lastString(inputstr)))
    #     except:
    #         print('Invalid')

