# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        ans = ListNode(0,head)
        List = ans
        while List:
            while List.next and List.next.val == val:
                List.next = List.next.next
            List = List.next
        return ans.next
        
        