# encoding=utf-8

import timeit
import random

class SortSolution():
    def __init__(self):
        self.arr = []
        
    # 测试数据生成器
    def _testCaseGenerator(self, n):
        """n表示数组的长度"""
        for i in range(n):
            self.arr.append(random.randint(0, 1000))

    # 冒泡排序: 比较相邻元素大小, 逆序则交换, 这样最大或最小的元素则会在一次遍历之后归位.
    # 时间复杂度: 最好的情况是O(n), 最差的情况是O(n^2)
    # 空间复杂度: O(1)
    # 改进思路1: 设置标志位, 如果一次遍历后,flag == false, 说明已经完成排序
    # 改进思路2: 记录遍历一次后标记的最后位置, 下次从头部遍历到这个位置
    def bubbleSort(self):
        """比较相邻两个元素的大小, 如果逆序则交换"""
        length = len(self.arr)
        if length <= 1:
            return self.arr
        k = length
        for i in range(length):
            # 设置标记, 便于判断是否已经完成排序
            flag = False
            for j in range(1, k):
                if self.arr[j-1] > self.arr[j]:
                    self.arr[j-1], self.arr[j] = self.arr[j], self.arr[j-1]
                    k = j
                    flag = True
            if flag == False:
                break
        return self.arr

    # 直接插入排序: 将元素直接插入到有序数组的对应位置即可
    # 时间复杂度: O(n^2), 虽然时间复杂度与冒泡排序相同, 但是操作次数降低了很多, 所以时间要更快
    def insertionSort(self):
        """将元素插入到已经有序的数据中对应位置"""
        length = len(self.arr)
        if length <= 1:
            return self.arr
        
        for i in range(1, length):
            if self.arr[i] < self.arr[i-1]:
                val = self.arr[i]
                index = i
                for j in range(i-1, -1, -1):
                    if self.arr[j] > val:
                        self.arr[j+1] = self.arr[j]
                        index = j
                    else:
                        break
                self.arr[index] = val
        return self.arr


if __name__ == '__main__':
    solution = SortSolution()
    test_case = solution._testCaseGenerator(2000)
    t1 = timeit.Timer('solution.insertionSort()', 'from __main__ import solution')
    print(t1.timeit(number=1000))