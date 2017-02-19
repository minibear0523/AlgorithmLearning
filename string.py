# encoding=utf-8


class Solution(object):
    def bruteForceStringMatch(self, string, pattern):
        for i in range(0, len(string) - len(pattern)):
            j = 0
            while j < len(pattern) and pattern[j] == string[j+i]:
                j += 1
                if j == len(pattern):
                    return i
        return -1


if __name__ == '__main__':
    s = Solution()
    string = 'NOBODY NOTICED HIM'
    pattern = 'NOT'
    print(s.bruteForceStringMatch(string, pattern))