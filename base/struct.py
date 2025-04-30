from typing import List, Optional


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

    def print_self(self) -> str:
        current = self
        s = ""
        while current:
            s += f"{current.val} -> "
            current = current.next
        s += "None"
        return s

    @staticmethod
    def from_list(values: List[int]) -> Optional['ListNode']:
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head
