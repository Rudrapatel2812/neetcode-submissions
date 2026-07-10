# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head=ListNode(0)
        l=[]
        for i in lists:
            curr=i
            while curr:
                heapq.heappush(l,curr.val)
                curr=curr.next
        p=head
        while len(l):
            i=heapq.heappop(l)
            curr=ListNode(i)
            p.next=curr
            p=p.next

        return head.next