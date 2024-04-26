# aList = [1, 3, 5, 7, 9]
# print(aList[2:])
#
# print(1+2+3+4)
#
# astring = '38$@NoNoN'
# for i in astring:
#     print(i)
#     print(i.lower())


# num_list = [10, 11, 21, 19, 21, 17, 21, 16, 21, 18, 15]
# num_list.sort()
# print(num_list)

import sys
import collections

# for line in sys.stdin:
a = input()
a = a.split(' ')
num_list = []
for i in range(len(a)):
    num_list.append(int(a[i]))
num_list.sort()
num_key = {}
for i in num_list:
    num = collections.counter(i)
    num_key[num_list[i]] = num
print(num_key)

