# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sta=[]
        temp=head
        while temp:
            sta.append(temp)
            temp=temp.next
        c=0
        while sta:
            d=sta[-1].val*2+c
            c=d//10
            sta[-1].val=d-c*10
            sta.pop(-1)
        if c==1:
            newNode=ListNode(c)
            newNode.next=head
            head=newNode
        return head