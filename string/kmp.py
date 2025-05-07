from typing import List


class KMP:
    def __init__(self,pat:str):
        self.pat = pat
        self.next = self.build_next(pat)

    def build_next(self,patt):
        next = [0] * len(patt)  # next 数组（初值元素一个 0）
        j = 0  # 当前共同前后缀的长度
        i = 1
        while i < len(patt):  # 遍历字符
            if patt[j] == patt[i]:
                # 下一个字符依然相同，长度加 1
                j += 1
                next[i] = j
                i += 1
            else:
                # 下一个字符不同
                if j == 0:
                    # 查表后发现不存在更短的前后缀
                    next[i] = j
                    i += 1
                else:
                    # 查表看看其中存不存在更短的前后缀
                    j = next[j - 1]
        return next

    def search(self,txt) -> int:
        i = 0
        j = 0
        while i < len(txt):
            if txt[i] == self.pat[j]:
                j += 1
                i += 1
            elif j > 0:
                j = self.next[j - 1]
            else:
                i += 1
            if j == len(self.pat):
                return i-j
        return -1

'''
len(M),pat -> "abacabab"
len(N),txt -> ""
'''
class KMP2:

    def __init__(self,pat:str):
        self.pat = pat
        self.M = len(self.pat)
        #初始化一个全部为0的二维数组
        self.dp = [[0 for _ in range(256)] for _ in range(self.M)]
        self.build_next()

    def build_next(self):
        #只有遇到pat[0]第一个字母时，才转为状态1
        self.dp[0][ord(self.pat[0])] = 1
        X = 0
        for j in range(1,self.M):
            for c in range(256):
                self.dp[j][c] = self.dp[X][c]
            self.dp[j][ord(self.pat[j])] = j + 1
            X = self.dp[X][ord(self.pat[j])]

    def search(self,txt:str):
        N = len(txt)
        j = 0
        for i in range(N):
            j = self.dp[j][ord(txt[i])]
            if j == self.M:
                return i - self.M + 1
        return -1



if __name__ == '__main__':
    kmp = KMP("abacabab")
    print(kmp.next)
    kmp2 = KMP2("abacabab")
    # print(kmp2.dp)

    print(kmp.search("abcaabacabab"))
    print(kmp2.search("abcaabacabab"))
