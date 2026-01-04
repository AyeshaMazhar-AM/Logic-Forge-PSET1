import heapq

def kth_Smallest(matrix, k):
    n = len(matrix)
    min_Heap = []

    for row in range(n):
        heapq.heappush(min_Heap, (matrix[row][0], row, 0))
    count = 0
    while min_Heap:
        value, row, col = heapq.heappop(min_Heap)
        count += 1
        if count == k:
            return value
        if col + 1 < n:
            heapq.heappush(min_Heap, (matrix[row][col + 1], row, col + 1))
matrix = [
    [1, 5, 9],
    [10, 11, 13],
    [12, 13, 15]
]
print(kth_Smallest(matrix, 8))
