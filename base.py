board = [
    [0,8,2,6,3,0,7,0,0],
    [1,0,0,0,0,0,8,0,0],
    [3,5,0,0,0,8,0,0,9],
    [0,0,0,0,6,9,3,0,0],
    [6,1,0,4,0,3,0,0,0],
    [4,0,3,0,0,0,6,0,5],
    [0,0,0,8,0,0,0,0,0],
    [8,7,9,3,4,5,0,0,0],
    [0,0,0,9,0,0,0,7,8]
    ]


def display(b):
    for i in range(0,9):
        if i!=0 and i%3==0:
            print("------------------------")

        for j in range(0,9):
            if j%3==0 and j!=0:
                print(" | ", end="")

            if j==8:
                print(b[i][j])
            else:
                print(str(b[i][j]) + " ", end="")
            
def valid(b, pos, num):
    # Checks Row Validity
    for i in range(len(b[0])):
        if b[pos[0]][i] == num and pos[1] != i:
            return False

    # Checks Column Validity
    for i in range(len(b)):
        if b[i][pos[1]] == num and pos[0] != i:
            return False

    # Checks Square Validity
    sq_x = pos[1] // 3
    sq_y = pos[0] // 3
    for i in range(sq_y*3, sq_y*3 + 3):
        for j in range(sq_x * 3, sq_x*3 + 3):
            if b[i][j] == num and (i,j) != pos:
                return False

    return True

def solve(b):
    find = isEmpty(b)
    if find:
        r, c = find
    else:
        return True

    for i in range(1,10):
        if valid(b, (r, c), i):
            b[r][c] = i

            if solve(b):
                return True

            b[r][c] = 0

    return False

def isEmpty(b):
    for i in range(0,9):
        for j in range(0,9):
            if b[i][j] == 0:
                return (i, j)  # row, col
            
