# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        else:
            arr=[]
            cur=head
            while cur is not None:
                arr.append(cur.val)
                cur=cur.next
            for i in range(len(arr)):
                if i%2==1:
                    temp=arr[i-1]
                    arr[i-1]=arr[i]
                    arr[i]=temp
            head=cur=ListNode(0)
            for i in arr:
                cur.next=ListNode(i)
                cur=cur.next
            return head.next
                
                
                