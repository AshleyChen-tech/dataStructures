# **************************链表************************** #


# 21. 合并两个有序链表
class Solution:
    def mergeTwoLists(self, list1, list2):
        cur = dum = ListNode(0)
        while list1 and list2:
            if list1.val < list2.val:
                cur.next, list1 = list1, list1.next
            else:
                cur.next, list2 = list2, list2.next
            cur = cur.next
        cur. next = list1 if list1 else list2
        return dum.next


# 2. 两数相加
class Solution:
    def addTwoNumbers(self, l1, l2):
        cur = dummy = ListNode()  # 哨兵节点
        carry = 0  # 进位
        while l1 or l2 or carry:  # 有一个不是空节点，或者还有进位，就继续迭代
            carry += (l1.val if l1 else 0) + (l2.val if l2 else 0)  # 节点值和进位加在一起
            cur.next = ListNode(carry % 10)  # 每个节点保存一个数位
            carry //= 10  # 新的进位
            cur = cur.next  # 下一个节点
            if l1: l1 = l1.next  # 下一个节点
            if l2: l2 = l2.next  # 下一个节点
        return dummy.next  # 哨兵节点的下一个节点就是头节点


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
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        p0 = dummy = ListNode(next=head)
        for _ in range(left - 1):
            p0 = p0.next
        pre = None
        cur = p0.next
        for _ in range(right - left + 1):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        p0.next.next = cur
        p0.next = pre
        return dummy.next


# 19. 删除链表的倒数第 N 个结点


# 82. 删除排序链表中的重复元素 II
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode(next=head)
        while cur.next and cur.next.next:
            val = cur.next.val
            if cur.next.next.val == val:
                while cur.next and cur.next.val == val:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next


# 61. 旋转链表
class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next: return head
        # 求链表长度
        _len = 0
        cur = head
        while cur:
            _len += 1
            cur = cur.next
        # 对长度取模
        k %= _len
        if k == 0: return head
        # 让 fast 先向后走 k 步
        fast, slow = head, head
        while k:
            fast = fast.next
            k -= 1
        # 此时 slow 和 fast 之间的距离是 k；fast 指向第 k+1 个节点
        # 当 fast.next 为空时，fast 指向链表最后一个节点，slow 指向倒数第 k + 1 个节点
        while fast.next:
            fast = fast.next
            slow = slow.next
        # newHead 是倒数第 k 个节点，即新链表的头
        newHead = slow.next
        # 让倒数第 k + 1 个节点 和 倒数第 k 个节点断开
        slow.next = None
        # 让最后一个节点指向原始链表的头
        fast.next = head
        return newHead


# 86. 分隔链表
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        sml_hummy, big_dummy = ListNode(0), ListNode(0)
        sml, big = sml_hummy, big_dummy
        while head:
            if head.val < x:
                sml.next = head
                sml = sml.next
            else:
                big.next = head
                big = big.next
            head = head.next
        sml.next = big_dummy.next
        big.next = None
        return sml_hummy.next






