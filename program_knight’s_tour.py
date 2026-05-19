N = 5

board = [[-1 for _ in range(N)] for _ in range(N)]

move_x = [2, 1, -1, -2, -2, -1, 1, 2]
move_y = [1, 2, 2, 1, -1, -2, -2, -1]


def aman(x, y):
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1


def solve(x, y, langkah):
    if langkah == N * N:
        return True

    for i in range(8):
        next_x = x + move_x[i]
        next_y = y + move_y[i]

        if aman(next_x, next_y):
            board[next_x][next_y] = langkah

            if solve(next_x, next_y, langkah + 1):
                return True

            board[next_x][next_y] = -1

    return False


x = int(input("Posisi awal X: "))
y = int(input("Posisi awal Y: "))

board[x][y] = 0

if solve(x, y, 1):
    print("\nSolusi Tur Kuda:\n")

    for row in board:
        print(row)
else:
    print("Tidak ada solusi")
