# encoding=utf-8

# 顺序查找
def sequential_search(a, k):
    length = len(a)
    if length == 0:
        return False
    else:
        for i in xrange(length):
            if a[i] == k:
                return i+1
        return False


if __name__ == '__main__':
    array = [89, 45, 68, 90, 29, 34, 17]
    key_1, key_2 = 29, 30
    print(sequential_search(array, key_1))
    print(sequential_search(array, key_2))