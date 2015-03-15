'''
Created on 21/06/201

@author: Kippel @ ihaveseenthings.com
'''

def solve(board):
    m = len(board)
    n = len(board[0])
    not_surrounded = []
    
    #first pass finding not surrounded Os
    for col in xrange(0, n):
        if board[0][col] == "O" and not (0, col) in not_surrounded:
            not_surrounded.append((0, col))  
    
    for col in xrange(0, n):
        if board[m-1][col] == "O" and not (m-1, col) in not_surrounded:
            not_surrounded.append((m-1, col))
            
    for row in xrange(0, m):
        if board[row][0] == "O" and not (row, 0) in not_surrounded:
            not_surrounded.append((row, 0))
    
    for row in xrange(0, m):
        if board[row][n-1] == "O" and not (0, n-1) in not_surrounded:
            not_surrounded.append((0, n-1))
    
    #flip of internal Os
    for i in xrange(1, m):
        for j in xrange(1, n):
            if board[i][j] == "O":
                board[i][j] = "X"
    
    print board

board = [["X", "X", "X", "X"],
         ["X", "O", "O", "X"],
         ["X", "X", "O", "X"],
         ["X", "O", "X", "X"]]

solve(board)