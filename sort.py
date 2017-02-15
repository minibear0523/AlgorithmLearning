# encoding=utf-8


# 选择排序: 
# 每次都寻找最小元素与当前元素互换
def selection_sort(a):
    length = len(a)
    if length == 0 or length == 1:
        return a
    else:
        min_ele = None
        for i in range(0, length):
            min_ele = a[i]
            min_index = i
            for j in range(i+1, length):
                if a[j] < min_ele:
                    min_ele = a[j]
                    min_index = j
            if min_index != i:
                a[i], a[min_index] = a[min_index], a[i]
            print(a)
        return a


# 冒泡排序
# 比较相邻两个元素的大小, 交换位置.
def bubble_sort(a):
    length = len(a)
    if length <= 1:
        return a
    else:
        for i in range(0, length-1):
            for j in range(0, length-1-i):
                if a[j] > a[j+1]:
                    a[j], a[j+1] = a[j+1], a[j]
        return a


if __name__ == '__main__':
    array = [89, 45, 68, 90, 29, 34, 17]
    print(bubble_sort(array))