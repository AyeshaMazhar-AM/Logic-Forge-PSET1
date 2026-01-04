def rem_Invalid_Paren(expr):
    result = set()
    left = 0
    right = 0
    for ch in expr:
        if ch == '(':
            left += 1
        elif ch == ')':
            if left > 0:
                left -= 1
            else:
                right += 1
    def valid_string(index, left_count, right_count, left_rem, right_rem, path):
        if index == len(expr):
            if left_rem == 0 and right_rem == 0:
                result.add(path)
            return
        ch = expr[index]
        if ch == '(' and left_rem > 0:
            valid_string(index + 1, left_count, right_count, left_rem - 1, right_rem, path)
        if ch == ')' and right_rem > 0:
            valid_string(index + 1, left_count, right_count, left_rem, right_rem - 1, path)
        if ch not in '()':
            valid_string(index + 1, left_count, right_count, left_rem, right_rem, path + ch)
        elif ch == '(':
            valid_string(index + 1, left_count + 1, right_count, left_rem, right_rem, path + ch)
        elif ch == ')' and right_count < left_count:
            valid_string(index + 1, left_count, right_count + 1, left_rem, right_rem, path + ch)

    valid_string(0, 0, 0, left, right, "")
    return list(result)

print(rem_Invalid_Paren("()())()"))
print(rem_Invalid_Paren("(a)())()"))
print(rem_Invalid_Paren(")("))
print(rem_Invalid_Paren("abc"))
print(rem_Invalid_Paren("((("))