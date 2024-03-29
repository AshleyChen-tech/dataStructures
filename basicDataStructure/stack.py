# 用python实现栈
class Stack1:
    """尾部是顶端"""
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class Stack2:
    """头部是顶端"""

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items is None

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    s = Stack1()
    s.push(4)
    result = s.pop()
    print(result)
