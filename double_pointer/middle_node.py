'''
给你单链表的头结点 head ，请你找出并返回链表的中间结点。

如果有两个中间结点，则返回第二个中间结点。
'''
from typing import Optional

from base.struct import ListNode


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #单指针
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        middle = head
        raw = head

        #获取长度
        length = 0
        while raw:
            length += 1
            raw = raw.next

        middle_index = length // 2
        while middle_index > 0:
            middle = middle.next
            middle_index -= 1

        return middle


    def middleNode_Ex(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # 遍历链表并打印每个节点的值
    def print_list(self, head: Optional[ListNode]) -> str:
        current = head
        s = ""
        while current:
            # print(current.val, end=" -> ")
            s += f"{current.val} -> "
            current = current.next
        s += "None"
        # print("None")  # 打印链表末尾
        return s



if __name__ == '__main__':
    solution = Solution()
    case1 = [
        ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5))))),
        ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,ListNode(6))))))
    ]
    case2 = [
        ListNode(3,ListNode(4,ListNode(5))),
        ListNode(4,ListNode(5,ListNode(6))),
    ]
    res = []
    for i in range(len(case1)):
        # r = solution.middleNode(case1[i])
        r = solution.middleNode_Ex(case1[i])
        print(f'expect: {solution.print_list(case2[i])}, res: {solution.print_list(r)}')
        res.append(r)
    print(res)