from os.path import getsize

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minStack) == 0:
            self.minStack.append(val)
        else:
            if val <= self.minStack[-1]:
                self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop(-1)
        self.minStack.pop(-1)

    def top(self) -> int:
        if self.getSize() == 0:
            return -1
        return self.stack[-1]

    def getMin(self) -> int:
        if self.getSize() == 0:
            return -1
        return self.minStack[-1]

    def getSize(self) -> int :
        return len(self.stack)

'''
class MinStack:

    def __init__(self):
        self.stackList = []
        self.sortList = []
        self.lastInsertIndex = -1

    def push(self, val: int) -> None:
        self.stackList.append(val)

        #insert sort list
        size = len(self.sortList)
        if size == 0:
            self.sortList.append(val)
            self.lastInsertIndex = 0
        elif size == 1:
            if val > self.sortList[0]:
                self.sortList.append(val)
                self.lastInsertIndex = 1
            else:
                self.sortList.insert(0,val)
                self.lastInsertIndex = 0
        else:
            left = 0
            right = size - 1
            while left <= right:
                mid = (left + (right - left) // 2)
                if val > self.sortList[mid]:
                    left = mid + 1
                elif val < mid:
                    right = mid - 1
                else:
                    right = mid - 1
            self.lastInsertIndex = left
            self.sortList.insert(left, val)

    def pop(self) -> None:
        removeVal = self.stackList[-1]
        self.stackList.pop(-1)
        self.sortList.remove(removeVal)

    def top(self) -> int:
        if self.getSize() == 0:
            return -1
        return self.stackList[-1]

    def getMin(self) -> int:
        if self.getSize() == 0:
            return -1
        return self.sortList[0]

    def getSize(self) -> int :
        return len(self.stackList)
'''

if __name__ == '__main__':
    obj = MinStack()
    obj.push(2)
    obj.push(0)
    obj.push(3)
    obj.push(0)
    min1 = obj.getMin()
    obj.pop()
    min2 = obj.getMin()
    obj.pop()
    min3 = obj.getMin()
    top = obj.top()
    min4 = obj.getMin()
    # print(f'min1: {min1},top: {top}, min2: {min2}')
    print(f'min1: {min1},top: {top}, min2: {min2}, min3: {min3}, min4: {min4}')