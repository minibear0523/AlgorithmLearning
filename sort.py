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
        return self.arr

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

    # 选择排序: 每次选取最小值插入到相应位置
    # 时间复杂度: O(n^2), 性能方面: 插入排序 > 选择排序 > 冒泡排序
    def selectionSort(self):
        """每次都选取最小值, 插入到数据的指定位置进行排序"""
        length = len(self.arr)
        if length <= 1:
            return self.arr
        for i in range(0, length):
            min_index = i
            for j in range(i+1, length):
                if self.arr[min_index] > self.arr[j]:
                    min_index = j
            self.arr[min_index], self.arr[i] = self.arr[i], self.arr[min_index]
        return self.arr

    # 归并排序: 递归分解数据, 然后再合并数组
    # 时间复杂度: O(nlogn), 最有时间复杂度: O(n)
    # 空间复杂度: O(n)
    def mergeSort(self, arr):
        """将数据递归分解, 最后进行merge, 将数组分为left和right直至最小个数, 进行比较归并即可."""
        length = len(arr)
        if length <= 1:
            return arr
        num = length / 2
        left = self.mergeSort(arr[:num])
        right = self.mergeSort(arr[num:])
        return self._merge(left, right)

    def _merge(self, left, right):
        """将数组left和right进行合并"""
        l_index, r_index = 0, 0
        result = []
        while l_index < len(left) and r_index < len(right):
            if left[l_index] < right[r_index]:
                result.append(left[l_index])
                l_index += 1
            else:
                result.append(right[r_index])
                r_index += 1
        result += left[l_index:]
        result += right[r_index:]
        return result

    # 希尔排序: 递减增量排序, 每次的步幅增加, 不稳定排序
    # 时间复杂度: O(nlog^2n)
    def shellSort(self):
        length = len(self.arr)
        if length <= 1:
            return self.arr
        gap = length/2
        while gap > 0:
            for i in range(gap, length):
                tmp = self.arr[i]
                j = i
                while (j >= gap and self.arr[j-gap] > tmp):
                    self.arr[j] = self.arr[j-gap]
                    j = j - gap
                self.arr[j] = tmp
            gap = gap/2
        return self.arr

    # 快速排序: 划分区域排序
    # 时间复杂度: O(n^2), 最优时间复杂度O(nlogn)
    def quickSort(self):
        if len(self.arr) <= 1:
            return self.arr
        return self._qSort(0, len(self.arr)-1)
        
    def _qSort(self, left, right):
        """left是左边界, right是右边界"""
        if left >= right:
            return self.arr
        else:
            key = self.arr[left]
            l_index = left
            r_index = right
            while l_index < r_index:
                while self.arr[r_index] >= key and l_index < r_index:
                    r_index -= 1
                while self.arr[l_index] <= key and l_index < r_index:
                    l_index += 1
                self.arr[l_index], self.arr[r_index] = self.arr[r_index], self.arr[l_index]
            self.arr[left], self.arr[l_index] = self.arr[l_index], self.arr[left]
            self._qSort(left, l_index-1)
            self._qSort(r_index+1, right)
            return self.arr


if __name__ == '__main__':
    solution = SortSolution()
    test_case = solution._testCaseGenerator(20)
    #t1 = timeit.Timer('solution.selectionSort()', 'from __main__ import solution')
    #print(t1.timeit(number=1000))
    print(test_case)
    print(solution.quickSort())