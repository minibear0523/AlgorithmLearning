# encoding=utf-8


# 字符串匹配--暴力法
def brute_force_string_match(string, pattern):
    len_str = len(string)
    len_pat = len(pattern)
    if len_str < len_pat:
        return False
    elif string == pattern:
        return 0
    else:
        for i in range(0, len_str - len_pat):
            for j in range(0, len_pat):
                if string[i+j] != pattern[j]:
                    break
            