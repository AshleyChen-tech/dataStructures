from basicDataStructure.stack import Stack1
import string


# 匹配括号
def parChecker1(symbolString):
    s = Stack1()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index += 1

    if balanced and s.isEmpty():
        return True
    else:
        return False


# 匹配符号
def parChecker2(symbolString):
    s = Stack1()

    balanced = True
    index = 0

    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False

        index += 1

    if balanced and s.isEmpty():
        return True
    else:
        return False


def matches(open, close):
    opens = "([{"
    closes = ")]}"

    return opens.index(open) == closes.index(close)


# 十进制转二进制
def divideBy2(decNumber):
    remstack = Stack1()

    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber //= 2

    binString = ""
    while not remstack.isEmpty():
        binString += str(remstack.pop())

    return binString


# 十进制转任意进制
def baseConverter(decNumber, base):
    digits = "0123456789ABCDEF"

    remstack = Stack1()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber //= base

    newString = ""
    while not remstack.isEmpty():
        newString += digits[remstack.pop()]

    return newString


# 中序到后序的转换
def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    opStack = Stack1()
    postfixList = []

    tokenList = infixexpr.split()

    for token in tokenList:
        if token in string.ascii_uppercase:
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return ''.join(postfixList)


# 实现后序表达式
def PostfixEval(infixexpr):
    operandStack = Stack1()
    postfixList = []

    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "0123456789":
            postfixList.append(token)
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token, operand1, operand2)
            operandStack.push(result)

    return operandStack.pop()


def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2


if __name__ == '__main__':
    result = baseConverter(2048, 16)
    print(result)
