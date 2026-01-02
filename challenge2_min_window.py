def minWindowBrute(log, pattern):
    if not log or not pattern:
        return ""
    
    from collections import Counter
    pattern_count = Counter(pattern)
    min_len = float("inf")
    sub_string = ""

    n = len(log)
    for i in range(n):
        for j in range(i, n):
            substring = log[i:j+1]
            window_count = Counter(substring)
            if all(window_count[c] >= pattern_count[c] for c in pattern_count):
                if j - i + 1 < min_len:
                    min_len = j - i + 1
                    sub_string = substring

    return sub_string
print(minWindowBrute("ADOBECODEBANC", "ABC"))
print(minWindowBrute("a", "a"))
print(minWindowBrute("a", "aa"))
