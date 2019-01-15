# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head

        result = ListNode(0)
        cur = head
        pre = result
        next = None
        while cur:
            next = cur.next
            while pre.next and pre.next.val < cur.val:
                pre = pre.next
            cur.next = pre.next
            pre.next = cur
            pre = result
            cur = next
        return result.next


if __name__ == '__main__':
    head = [4, 2, 1, 3]
    print(Solution().insertionSortList(head))
