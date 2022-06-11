# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        root=l3=ListNode(0)
        carry=0
        while l1 or l2 or carry:#防止carry==1时，即有进位到一个比l1，l2都更高的位数。如999+9999=10998而不是0998
            numl1=numl2=0
            if l1:
                numl1=l1.val
                l1=l1.next
            if l2:
                numl2=l2.val
                l2=l2.next
            carry,val=divmod(carry+numl1+numl2,10)
            l3.next=ListNode(val)
            l3=l3.next
        return root.next #写入是从第二个节点开始的