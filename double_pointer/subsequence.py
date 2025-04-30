
'''
判断s是否是t的子字符串
要求：s中的字符顺序和t中的保持一致
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        l = len(t)
        checkIndex = 0
        for c in t:
            if s[checkIndex] == c:
                checkIndex += 1
                if checkIndex == len(s):
                    return True
        return False

if __name__ == '__main__':
    solution = Solution()
    case1 = ['bce','aec','axe']
    case2 = ['abcde','abcde','a']
    res = []
    for i in range(len(case1)):
        r = solution.isSubsequence(case1[i],case2[i])
        print(f'sub: {case1[i]}, target: {case2[i]}, res: {r}')
        res.append(r)
    print(res)