# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution(object):
#     def removeNthFromEnd(self, head, n):
#         """
#         :type head: ListNode
#         :type n: int
#         :rtype: ListNode
#         """
#         count = 0
#         node1 = head
#         while(node1 != None):
#             node1 = node1.next
#             count += 1
#         l = count - n
#         if l == 0:
#             return head.next
#         else:
#             node2 = head
#             for i in range(l-1):
#                 node2 = node2.next
#             delNode = node2.next
#             node2.next = delNode.next
#             return head

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummyHead = ListNode(0)
        dummyHead.next = head
        p = dummyHead
        q = dummyHead
        for i in range(n+1):
            q = q.next

        while q != None:
            p = p.next
            q = q.next
        delNode = p.next
        p.next = delNode.next
        delNode = None
        return dummyHead.next
