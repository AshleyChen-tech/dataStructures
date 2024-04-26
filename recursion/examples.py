from basicDataStructure.stack import Stack1


# 循环求和
def listSum(numlist):
    theSum = 0
    for num in numlist:
        theSum += num
    return theSum


# 递归求和
def listSum1(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        print(numList[0] + listSum1(numList[1:]))
        return numList[0] + listSum1(numList[1:])


# 转换进制
def toStr(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n//base, base) + convertString[n % base]


rStack = Stack1()

def toStr1(n, base):
    convertString = "0123456789"
    if n < base:
        rStack.push(convertString[n])
    else:
        rStack.push(convertString[n % base])
        toStr1(n // base, base)


# 绘制螺旋线
from turtle import *
# myTurtle = Turtle()
# myWin = myTurtle.getscreen()

def drawspiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawspiral(myTurtle, lineLen-5)

# drawspiral(myTurtle, 250)
# myWin.exitonclick()

# 绘制分形树
def tree(branchLen, t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15, t)
        t.left(40)
        tree(branchLen-10, t)
        t.right(20)
        t.backward(branchLen)

# t = Turtle()
# myWin = t.getscreen()
# t.left(90)
# t.up()
# t.backward(300)
# t.down()
# t.color('green')
# tree(110, t)


# 汉诺塔
def moveTower(height, fromPole, toPole, withPole):
    if height > 1:
        moveTower(height-1, fromPole, toPole, withPole)
        moveDisk(fromPole, toPole)
        moveTower(height-1, fromPole, toPole, withPole)

def moveDisk(fp, tp):
    print("moving disk from", fp, "to", tp)


# **********************动态规划**********************
# 找零钱问题（递归）
def recDC(coinValueList, change, knownResults):
    minCoins = change
    if change in coinValueList:
        knownResults[change] = 1
        return 1
    elif knownResults[change] > 0:
        return knownResults[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recDC(coinValueList, change - i,
                                 knownResults)    # 边界条件
            if numCoins < minCoins:
                minCoins = numCoins
                knownResults[change] = minCoins

        return minCoins


# 找零钱问题（动态规划）
def dpMakeChange(coinValueList, change, minCoins, coinUsed):
    for cents in range(change+1):
        coinCount = cents
        newCoin = 1
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
                newCoin = j
        minCoins[cents] = coinCount
        coinUsed[cents] = newCoin
    return minCoins[change]

def printCoins(coinUsed, change):
    coin = change
    while coin > 0:
        thisCoin = coinUsed[coin]
        print(thisCoin)
        coin -= thisCoin


if __name__ == '__main__':
    cl = [1, 5, 10, 21, 25]
    coinsUsed = [0] * 64
    coinCount = [0] * 64
    result = dpMakeChange(cl, 63, coinsUsed, coinCount)
    # print(result)
    # printCoins(coinsUsed, 52)
#     aList = [1, 3, 5, 7, 9]
#     toStr1(111, 2)
#     items = rStack.items
#     result = ''
#     for item in items:
#         result += item
#     print(result)
