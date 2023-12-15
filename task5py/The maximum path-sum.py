def maxPathSum(A, row, col, N, M):
    if row == N-1 and col == M-1:
        return A[row][col]
    
    if row >= N or col >= M:
        return float('-inf')
    
    down = maxPathSum(A, row+1, col, N, M) + A[row][col]
    right = maxPathSum(A, row, col+1, N, M) + A[row][col]
    
    return max(down, right)
 
N, M = map(int, input().split())
A = []
for _ in range(N):
    row = list(map(int, input().split()))
    A.append(row)
 
result = maxPathSum(A, 0, 0, N, M)
print(result)