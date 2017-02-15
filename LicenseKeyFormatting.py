# encoding=utf-8

# 1. 除了第一组以外, 其他每个小组的个数必须等于K
# 2. 所有小写字母更换为大写
class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        # 进行倒序, 大写, 并替换-符号
        _S = list(S.replace('-', '').upper()[::-1])
        n = len(_S)
        if n <= K:
            return S.replace('-', '').upper()
        else:
            for i in range(0, n+n/K, K+1):
                _S.insert(i, '-')
            return ''.join(_S[1:])[::-1]


if __name__ == '__main__':
    s = Solution()
    S = 'a0001afds-'
    print(s.licenseKeyFormatting(S, 4))