def swap_rows(matrix, x, y):
    matrix[x - 1], matrix[y - 1] = matrix[y - 1], matrix[x - 1]
    print (matrix)

def swap_columns(matrix, x, y):
    for i in range(len(matrix)):
        matrix[i][x - 1], matrix[i][y - 1] = matrix[i][y - 1], matrix[i][x - 1]

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

n, x, y = map(int, input().split())

matrix = [list(map(int, input().split())) for i in range(n)]

swap_rows(matrix, x, y)
swap_columns(matrix, x, y)

print_matrix(matrix)
