# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

    def createLinkedList(self, nums, n):
        if n == 0:
            return None
        self.head = ListNode(nums[0])
        curNode = self.head
        for i in range(1,n):
            curNode.next = ListNode(nums[i])
            curNode = curNode.next
        return self.head

    def printLinkedList(self, head):
        curNode = head;
        while(curNode != None):
            print(curNode.val, ' -> ', end='');
            curNode = curNode.next
        print('NULL')


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        cur = head
        while cur != None:
            next = cur.next

            cur.next = pre
            pre = cur
            cur = next
        return pre

if __name__ == '__main__':
    nums = [1,2,3,4,5]
    n = len(nums)
    head = LinkedList().createLinkedList(nums,n)
    LinkedList().printLinkedList(head)
    head2 = Solution().reverseList(head)
    LinkedList().printLinkedList(head2)
