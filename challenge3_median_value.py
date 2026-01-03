def find_median(scoresA, scoresB):
    m, n = len(scoresA), len(scoresB)
    total = m + n

    mid1 = (total - 1) // 2
    mid2 = total // 2

    i = j = 0
    count = 0
    prev = median_value = 0

    while count <= mid2:
        prev = median_value
        if i < m and (j >= n or scoresA[i] <= scoresB[j]):
            median_value = scoresA[i]
            i += 1
        else:
            median_value = scoresB[j]
            j += 1
        count += 1

    if total % 2 == 0:
        return (prev + median_value) / 2
    else:
        return median_value
scoresA = [1, 2]
scoresB = [3, 4]
print(find_median(scoresA, scoresB))