# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ma=-float('inf')
        sta=[]
        temp=head
        while temp:
            if len(sta)==0:
                sta.append(temp.val)
                ma=sta[0]
            elif temp.val>ma:
                sta=[temp.val]
                ma=sta[0]
            elif temp.val>sta[-1]:
                while temp.val>sta[-1]:
                    sta.pop(-1)
                sta.append(temp.val)
            else:
                sta.append(temp.val)
            temp=temp.next
        r=ListNode(0)
        t=r
        for i in sta:
            t.next=ListNode(i)
            t=t.next
        return r.next

#2487