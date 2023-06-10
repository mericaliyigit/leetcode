# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def printll(n):
    while (n):
        print(n.val)
        n = n.next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = head
        current = head
        pointer = head
        while current:
            pointer = current.next
            # if node is not null and it has the same value as current
            # increment our pointer futher
            while pointer and pointer.val == current.val:
                pointer = pointer.next
            # assign the next of our current to this position
            # essentially chopping of in betweens
            current.next = pointer
            # iterate
            current = current.next

        return start


ll = ListNode(1, ListNode(1, ListNode(
    2, ListNode(2, ListNode(2, ListNode(2, None))))))


printll(Solution().deleteDuplicates(ll))
