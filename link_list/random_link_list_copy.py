
from typing import Optional


class Node:
    def __init__(self, x: int, random: 'Node' = None, next: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

        # 遍历链表并打印每个节点的值
    def print_list(self) -> str:
        current = self
        s = ""
        while current:
            s += f"[{current.val},{current.random}] -> "
            current = current.next
        s += "None"
        return s

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        copyList = []
        copyRandomList =[]
        cur = head
        posList = []
        while cur:
            posList.append(cur)
            copyNode = Node(cur.val)
            copyList.append(copyNode)
            copyRandomList.append(cur.random)
            cur = cur.next
        l = len(copyList)
        for i in range(l):
            randomIndex = -1
            if copyRandomList[i] is not None:
                randomIndex = posList.index(copyRandomList[i])
            if randomIndex == -1:
                copyList[i].random = None
            else:
                copyList[i].random = copyList[randomIndex]
            if i != l - 1:
                copyList[i].next = copyList[i+1]
            else:
                copyList[i].next = None
        return copyList[0]

    def copyRandomList_hashtable(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        old_to_new = {}
        cur = head
        while cur:
            old_to_new[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            old_to_new[cur].next = old_to_new.get(cur.next)
            old_to_new[cur].random = old_to_new.get(cur.random)
            cur = cur.next
        return old_to_new[head]

    def copyRandomList_split(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        cur = head
        while cur:
            temp = Node(cur.val)
            temp.next = cur.next
            cur.next = temp
            cur = temp.next
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        cur = res = head.next
        pre = head
        while cur.next:
            pre.next = pre.next.next
            cur.next = cur.next.next
            pre = pre.next
            cur = cur.next
        pre.next = None
        return res


if __name__ == '__main__':
    solution = Solution()
    case1 = [
        Node(7,None,Node(13))
    ]


'''
给你一个长度为 n 的链表，每个节点包含一个额外增加的随机指针 random ，该指针可以指向链表中的任何节点或空节点。

构造这个链表的 深拷贝。 深拷贝应该正好由 n 个 全新 节点组成，其中每个新节点的值都设为其对应的原节点的值。新节点的 next 指针和 random 指针也都应指向复制链表中的新节点，并使原链表和复制链表中的这些指针能够表示相同的链表状态。复制链表中的指针都不应指向原链表中的节点 。

例如，如果原链表中有 X 和 Y 两个节点，其中 X.random --> Y 。那么在复制链表中对应的两个节点 x 和 y ，同样有 x.random --> y 。

返回复制链表的头节点。

用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：

val：一个表示 Node.val 的整数。
random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。
你的代码 只 接受原链表的头节点 head 作为传入参数。
'''