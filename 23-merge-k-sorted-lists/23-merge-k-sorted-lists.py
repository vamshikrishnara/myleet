# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge2(l1,l2):
            head=cur=ListNode(0)
            while l1 and l2:
                if l1.val<=l2.val:
                    cur.next=l1
                    l1=l1.next
                else:
                    cur.next=l2
                    l2=l2.next
                cur=cur.next
            if not l1:
                cur.next=l2
            else:
                cur.next=l1
            return head.next
        l=len(lists)
        i=1
        while i < l:
            for j in range(0,l-i,i*2):
                lists[j]=merge2(lists[j],lists[j+i])
            i=i*2    
        return lists[0] if l>0 else None
                    
                