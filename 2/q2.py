def is_sudoku(A):
    def col(A,n):
        return [x[n] for x in A]

    def grid(A, m, n):
        return [A[i][j] for i in range((m + 1) * 3) for j in range ((n + 1) * 3)]

    def validate(A):
        flag = [ 0 for i in range(9)]
        for i in range(9):
            for j in range(1,10):
                if A[i] == j:
                    flag[i] = [1]
                    break
        for i in range(9):
            if flag[i] == 0:
                return 0
    
    for i in range(9):
        if validate(A[i]) == 0 or validate(col(A, i)) == 0:
            return False
    for i in range(3):
        for j in range(3):
            if validate(grid(A, i, j)) == 0:
                return False
    return True