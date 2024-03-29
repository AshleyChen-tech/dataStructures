# 双端队列
class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addfront(self, item):
        self.items.append(item)

    def addrear(self, item):
        self.items.insert(0, item)

    def removefront(self):
        return self.items.pop()

    def removerear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    d = Deque()
    d.addfront(4)
    d.addrear('cat')
    d.addrear('dog')
    d.addrear(8.4)
    print(d.removefront())