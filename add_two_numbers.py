# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        carry = 0
        cont = True
        i1=l1
        i2=l2
        while (cont):
            x = i1.val + i2.val + carry
            if x > 9:
                carry = 1
                i1.val = x % 10
            else:
                carry = 0
                i1.val = x
            if (i1.next == None):
                i1.next = i2.next
                cont = False
            elif (i2.next == None):
                cont = False
            else:
                i1 = i1.next
                i2 = i2.next
        while (carry>0) and (i1.next != None):
            i1=i1.next
            x = i1.val + carry
            if x > 9 :
                carry =1
                i1.val = x % 10
            else:
                carry = 0
                i1.val = x
        if carry>0:
            node = ListNode(carry)
            i1.next = node
        return l1

if __name__ == '__main__':
    i1= ListNode(4)
    i2 = ListNode(9)
    i3 = ListNode(9)
    i1.next = i2
    i2.next = i3
    j1= ListNode(3)
    j2 = ListNode(2)
    j1.next = j2
    s = Solution()
    l=s.addTwoNumbers(i1,j1)
    while l != None:
        print(l.val)
        l = l.next