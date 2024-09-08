class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l3 = ListNode(0)
        current = l3
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            soma = val1 + val2 + carry
            carry = soma // 10
            current.next = ListNode(soma % 10)
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return l3.next
