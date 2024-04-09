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

t = Turtle()
myWin = t.getscreen()
t.left(90)
t.up()
t.backward(300)
t.down()
t.color('green')
tree(110, t)


# 汉诺塔
def moveTower(height, fromPole, toPole, withPole):
    if height > 1:
        moveTower(height-1, fromPole, toPole, withPole)
        moveDisk(fromPole, toPole)
        moveTower(height-1, fromPole, toPole, withPole)

def moveDisk(fp, tp):
    print("moving disk from", fp, "to", tp)


'**********************动态规划**********************'



# if __name__ == '__main__':
#     aList = [1, 3, 5, 7, 9]
#     toStr1(111, 2)
#     items = rStack.items
#     result = ''
#     for item in items:
#         result += item
#     print(result)
