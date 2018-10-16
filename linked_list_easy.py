
class LinkedList:

    def __init__(self):
        self.head = None

    def printList(self):
        p = self.head
        while p is not None:
            print(p.data)
            p = p.next

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node


    def deleteNode(self, key):

        cur = self.head

        if cur is not None:
            if cur.data == key:
                self.head = cur.next
                cur = None

        while cur is not None:
            if cur.data == key:
                break

            pre = cur
            cur = cur.next

        if cur is None:
            return

        pre.next = cur.next
        cur = None

    def reverseList(self):
        cur = self.head
        pre = None

        while cur is not None:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex

        self.head = pre


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def middleNode_876(self, head):
        """
        space 1, time 3n/2
        :type head: ListNode
        :rtype: ListNode
        """
        temp = head
        cnt = 0
        while temp is not None:
            cnt += 1
            temp = temp.next

        m = cnt // 2

        cntm = 0
        temp = head
        while cntm < m:
            temp = temp.next
            cntm += 1

        return temp

    def middleNode_876_2(self, head):
        '''
        brilliant
        '''
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def mergeTwoLists_21(self, l1, l2):
        """

        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode()
        cur = res
        temp1 = l1
        temp2 = l2

        while temp1 and temp2:
            if temp1.val <= temp2.val:
                cur.next = temp1
                temp1 = temp1.next
            else:
                cur.next = temp2
                temp2 = temp2.next
            cur = cur.next

        if temp1:
            cur.next = temp1

        if temp2:
            cur.next = temp2

        return res

    def deleteDuplicates_83(self, head):
        """
        init
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None or head.next is None:
            return head
        cur = head
        nex = cur.next
        while nex:
            if cur.val == nex.val:
                temp = nex
                nex = nex.next
                cur.next = nex
                temp.next = None
            else:
                cur = cur.next
                nex = ext.next
        return head

    def deleteDuplicates_83_2(self, head):
        '''
        a concise solution
        '''

        cur = head
        while cur:
            while cur.next and cur.val == cur.next.val:
                cur.next = cur.next.next
            cur = cur.next
        return head

    def deleteDuplicates_83_3(self, head):
        '''
        a recursive solution
        '''

        if head is None or head.next is None:
            return head

        head.next = self.deleteDuplicates_83_3(head.next)

        if head.val == head.next.val:
            return head.next
        else:
            return head







solver = Solution()

lis = LinkedList()
lis.push(1)
lis.push(2)
lis.push(3)
# lis.push(4)
# lis.push(5)
# lis.printList()
res = solver.middleNode_876_2(lis.head)
print(res.data)

print('well done')

