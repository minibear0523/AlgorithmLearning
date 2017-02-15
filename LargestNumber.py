# encoding=utf-8

# 一个非负数组, 将数字组合为最大整数
# 自定义排序: 首先不考虑位数, 只比较第一位数字的大小, 当第一位数组最大的时候, 为第一个数字; 然后当第一位相同时, 比较第二位的大小, 需要考虑两种情况: 位数相同, 例如34和30比较, 34应该在前; 位数不同, 例如30和3比较, 因为0<3, 所以30在后.
# 分治法进行处理, 需要统计第一个数字的大小进行排列. 345 34 342 32
class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        for i in range(0, len(nums)):
            max_index = i
            for j in range(i+1, len(nums)):
                if self._parseNumberBit(nums[max_index], 0) < self._parseNumberBit(nums[j], 0):
                    # 直接判断第一位数字大小
                    max_index = j
                elif self._parseNumberBit(nums[max_index], 0) == self._parseNumberBit(nums[j], 0):
                    # 如果第一位数字相等, 那么首先判断位数
                    length_max = len(str(nums[max_index]))
                    length_cur = len(str(nums[j]))
                    if length_cur == length_max:
                        m, n = 0, 0
                        while self._parseNumberBit(nums[max_index], m) == self._parseNumberBit(nums[j], n):
                            m += 1
                            n += 1
                        if self._parseNumberBit(nums[max_index], m+1) < self._parseNumberBit(nums[j], n+1):
                            max_index = j
                    else:
                        m, n = 0, 0
                        while self._parseNumberBit(nums[max_index], m) == self._parseNumberBit(nums[j], n) and m < length_max and n < length_cur:
                            m += 1
                            n += 1




    def _parseNumberBit(self, num, index):
        """将数字的第一位进行比较"""
        return int(str(num)[index])