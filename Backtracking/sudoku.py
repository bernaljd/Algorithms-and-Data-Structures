from sys import stdin

def check():
    pass

def sudoku(r, c, curr_sol, sols):
    if r == 9:
        sols.append(curr_sol.copy())
    elif c == 9:
        sudoku(r + 1, 0, curr_sol)
    else:
        if curr_sol[r][c] != 0: 
            if check(r, c, curr_sol[r][c], curr_sol):
                sudoku(r, c + 1, curr_sol)
            else:
                for v in range(1, 10):
                    if check(r, c, v, curr_sol):
                        curr_sol[r][c] = v
                        sudoku(r, c + 1, curr_sol)