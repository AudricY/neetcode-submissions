# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next
        l = len(nodes)
        i = 0
        j = l-1
        dummy = ListNode(0)
        cur = dummy
        while i<=j:
            cur.next=nodes[i]
            cur = cur.next
            if i!=j:
                cur.next=nodes[j]
                cur = cur.next
            i+=1
            j-=1
        cur.next = None
        # return dummy.next

        