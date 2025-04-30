
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            s = f'{s[1:]}{s[:1]}'
            if s == goal:
                return True
        return False
'''
abcde -> bcdea
bcdea -> cdeab

'''
if __name__ == '__main__':
    solution = Solution()
    case1 = [
        ("abcde","cdeab"),
        ("abcde","abced"),
        ("a","a"),
        ("aca","caa"),
    ]
    case2 = [
        True,
        False,
        True,
        True,
    ]
    res = []
    for i in range(len(case1)):
        r = solution.rotateString(case1[i][0], case1[i][1])
        print(f'expect: {case2[i]}, res: {r}')
        res.append(r)
    print(res)

'''
给定两个字符串, s 和 goal。如果在若干次旋转操作之后，s 能变成 goal ，那么返回 true 。

s 的 旋转操作 就是将 s 最左边的字符移动到最右边。 

例如, 若 s = 'abcde'，在旋转一次之后结果就是'bcdea' 。
 

示例 1:

输入: s = "abcde", goal = "cdeab"
输出: true
示例 2:

输入: s = "abcde", goal = "abced"
输出: false
 

提示:

1 <= s.length, goal.length <= 100
s 和 goal 由小写英文字母组成
'''