def is_sudoku(A):
    def grid(A):
        return [[A[i][j] for i in range((m + 1) * 3) for j in range((n + 1) * 3)] for m in range(3) for n in range(3)]

    def validate(A):  # 0 = pass, 1 = fail
        l = {i for i in range(1, 10)}
        for i in range(len(A)):
            if not l.issubset(set(A[i])):
                return 1
        return 0

    return False if any(validate(A), validate([[x] for x in zip(*A)]), validate(grid(A))) else True


if __name__ == '__main__':
    A = [[4, 3, 5, 2, 6, 9, 7, 8, 1],
         [6, 8, 2, 5, 7, 1, 4, 9, 3],
         [1, 9, 7, 8, 3, 4, 5, 6, 2],
         [8, 2, 6, 1, 9, 5, 3, 4, 7],
         [3, 7, 4, 6, 8, 2, 9, 1, 5],
         [9, 5, 1, 7, 4, 3, 6, 2, 8],
         [5, 1, 9, 3, 2, 6, 8, 7, 4],
         [2, 4, 8, 9, 5, 7, 1, 3, 6],
         [7, 6, 3, 4, 1, 8, 2, 5, 9]]
    print([[x] for x in zip(*A)])
