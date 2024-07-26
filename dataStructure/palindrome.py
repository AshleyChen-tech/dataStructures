from dataStructure.deque import Deque


def palchecker(aString):
    chardeque = Deque()

    for char in aString:
        chardeque.addrear(char)

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removefront()
        last = chardeque.removerear()
        if first != last:
            stillEqual = False

    return stillEqual


if __name__ == '__main__':
    string = 'abcba'
    print(palchecker(string))