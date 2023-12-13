# Done

ra, ca = map(int, input().split())
matrixA = [list(map(int, input().split())) for _ in range(ra)]
rb, cb = map(int, input().split())
matrixB = [list(map(int, input().split())) for _ in range(rb)]
 
result = [[0] * cb for _ in range(ra)]
for i in range(ra):
    for j in range(cb):
        for k in range(ca):
            result[i][j] += matrixA[i][k] * matrixB[k][j]
 
for row in result:
    print(' '.join(map(str, row)))