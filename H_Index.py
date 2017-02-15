# encoding=utf-8
# H Index定义是: N篇文章中的h篇有h个引述, 并且其他的N-h篇文章的引述不超过h个.

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        n = len(citations)
        for i in xrange(n):
            if citations[i] >= (n-i):
                return n-i
        return 0


if __name__ == '__main__':
    citations = [3, 0, 6, 1, 5]
    s = Solution()
    print(s.hIndex(citations))