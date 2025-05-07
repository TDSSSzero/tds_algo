class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        next = self.build_next(needle)
        i = 0
        j = 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                j+=1
                i+=1
            elif j > 0:
                j = next[j - 1]
            else:
                i += 1
            if j == len(needle):
                return i - j
        return -1

    def build_next(self,pat):
        next = [0] * len(pat)
        j = 0  # 当前共同前后缀的长度
        i = 1
        while i < len(pat):  # 遍历字符
            if pat[j] == pat[i]:
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

if __name__ == '__main__':
    s = Solution()
    print(s.strStr("ababcabd","bc"))