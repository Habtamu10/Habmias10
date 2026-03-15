# Matrix Operations
def matrix_add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def matrix_multiply(A, B):
    rows_A, cols_A = len(A), len(A[0])
    cols_B = len(B[0])
    result = [[0] * cols_B for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    return result

def print_matrix(M):
    for row in M:
        print(row)

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print("A + B:")
print_matrix(matrix_add(A, B))
print("A * B:")
print_matrix(matrix_multiply(A, B))
