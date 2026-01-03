def minWindow(log, pattern):
    if not log or not pattern:
        return ""

    req = {}
    for c in pattern:
        req[c] = req.get(c, 0) + 1

    window = {}
    found = 0
    left = 0
    sub_string = ""
    min_len = float("inf")

    for right, char in enumerate(log):
        window[char] = window.get(char, 0) + 1
        if char in req and window[char] == req[char]:
            found += 1
        while found == len(req):
            if right - left + 1 < min_len:
                min_len = right - left + 1
                sub_string = log[left:right+1]

            window[log[left]] -= 1

            if log[left] in req and window[log[left]] < req[log[left]]:
                found -= 1
            left += 1

    return sub_string

print(minWindow("ADOBECODEBANC", "ABC"))
print(minWindow("a", "a"))
print(minWindow("a", "aa"))