def aman(board, row, col, n):
    # cek kolom
    for i in range(row):
        if board[i] == col:
            return False

    # cek diagonal kiri
    for i in range(row):
        if abs(board[i] - col) == abs(i - row):
            return False

    return True


def solve(board, row, n):
    if row == n:
        return True

    for col in range(n):
        if aman(board, row, col, n):
            board[row] = col

            if solve(board, row + 1, n):
                return True

    return False


def print_board(board, n):
    for i in range(n):
        for j in range(n):
            if board[i] == j:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


n = int(input("Masukkan ukuran papan: "))

board = [-1] * n

if solve(board, 0, n):
    print("\nSolusi ditemukan:\n")
    print_board(board, n)
else:
    print("Tidak ada solusi")
