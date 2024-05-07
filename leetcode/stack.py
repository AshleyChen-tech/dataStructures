# **************************栈************************** #


# 20. 有效的括号
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'{': '}',  '[': ']', '(': ')', '?': '?'}
        stack = ['?']
        for c in s:
            if c in dic:
                stack.append(c)
            elif dic[stack.pop()] != c:
                return False
        return len(stack) == 1


# 71. 简化路径
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split('/')
        for item in path:
            if item == '..':
                if stack:
                    stack.pop()
            elif item and item != '.':
                stack.append(item)
        return '/' + '/'.join(stack)


# 155. 最小栈
class MinStack:

    def __init__(self):
        self.items = []


    def push(self, val: int) -> None:
        if not self.items:
            self.items.append((val, val))
        else:
            self.items.append((val, min(val, self.items[-1][1])))


    def pop(self) -> None:
        return self.items.pop()


    def top(self) -> int:
        return self.items[-1][0]


    def getMin(self) -> int:
        return self.items[-1][1]


# 150. 逆波兰表达式求值
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            try:
                stack.append(int(token))
            except:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(self.evaluate(num1, num2, token))
        return stack[0]
    def evaluate(self, num1, num2, op):
        if op == "+":
            return num1 + num2
        elif op == '-':
            return num1 - num2
        elif op == '*':
            return num1 * num2
        elif op == '/':
            return int(num1 / float(num2))


# 224. 基本计算器
class Solution(object):
    def calculate(self, s):
        res, num, sign = 0, 0, 1
        stack = []
        for c in s:
            if c.isdigit():
                num = 10 * num + int(c)
            elif c == "+" or c == "-":
                res += sign * num
                num = 0
                sign = 1 if c == "+" else -1
            elif c == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ")":
                res += sign * num
                num = 0
                res *= stack.pop()
                res += stack.pop()
        res += sign * num
        return res


# 141. 环形链表
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast is slow:
                return True
        return False


# 138. 随机链表的复制


# 741. 摘樱桃


# 1463. 摘樱桃 II


