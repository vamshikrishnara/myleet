/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode head= new ListNode();
        ListNode merge= new ListNode();
        head=merge;
        while(list1!=null && list2!=null){
            if(list1.val <= list2.val){
                ListNode k=new ListNode();
                k.val=list1.val;
                merge.next=k;
                merge=merge.next;
                list1=list1.next;
            }
            else{
                ListNode k=new ListNode();
               k.val=list2.val;
                merge.next=k;
                merge=merge.next;
                list2=list2.next; 
            }
        }
        while(list1!=null){
            ListNode k=new ListNode();
            k.val=list1.val;
            merge.next=k;
            merge=merge.next;
            list1=list1.next;
        }
        while(list2!=null){
            ListNode k=new ListNode();
            k.val=list2.val;
            merge.next=k;
                merge=merge.next;
                list2=list2.next;
        }
    return head.next;   
    }
}