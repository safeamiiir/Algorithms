import numpy as np
print('Hey, we want to make N*N Square (N should make this way => N = 2^k; k is member of \'Natural Numbers\')')
[n, i, j] = input('import \"N\", (\"i\",\"j\") \n').split()
n = int(n)
i = int(i) - 1 # handle 0 at array
j = int(j) - 1 # handle 0 at array
print('n =', n)
print('(i,j) =', i+1, j+1)
board = np.full([n, n], '00')
board[i][j] = 'xx'
print('initialized board:\n', board)

def set_tile(n, i, j, my_board):
    n_half = int(n/2)
    if('00' in board and n_half > 0):
        print('\n')        
        print(board)
        if(i < n_half and j < n_half): #1
# #             print('in #1')
            my_board[n_half][n_half] = '**'
            my_board[n_half-1][n_half] = '**'
            my_board[n_half][n_half-1] = '**'
            set_tile(n_half, i, j, my_board[:n_half, :n_half])
            set_tile(n_half, n_half-1, 0, my_board[:n_half, n_half:])
            set_tile(n_half, 0, n_half-1, my_board[n_half:, :n_half])
            set_tile(n_half, 0, 0, my_board[n_half:, n_half:])
            
        elif(i < n_half and j >= n_half): #2
#             print('in #2')
            my_board[n_half-1][n_half-1] = '**'
            my_board[n_half][n_half-1] = '**'
            my_board[n_half][n_half] = '**'
            set_tile(n_half, n_half-1, n_half-1, my_board[:n_half, :n_half])
            set_tile(n_half, i, j-n_half, my_board[:n_half, n_half:])
            set_tile(n_half, 0, n_half-1, my_board[n_half:, :n_half])
            set_tile(n_half, 0, 0, my_board[n_half:, n_half:])
            
        elif(i >= n_half and j < n_half): #3
#             print('in #3')            
            my_board[n_half-1][n_half-1] = '**'
            my_board[n_half-1][n_half] = '**'
            my_board[n_half][n_half] = '**'
            set_tile(n_half, n_half-1, n_half-1, my_board[:n_half, :n_half])
            set_tile(n_half, n_half-1, 0, my_board[:n_half, n_half:])
            set_tile(n_half, i-n_half, j, my_board[n_half:, :n_half])
            set_tile(n_half, 0, 0, my_board[n_half:, n_half:])       
            
        elif(i >= n_half and j >= n_half): #4
#             print('in #4')            
            my_board[n_half-1][n_half-1] = '**'
            my_board[n_half-1][n_half] = '**'
            my_board[n_half][n_half-1] = '**'
            set_tile(n_half, n_half-1, n_half-1, my_board[:n_half, :n_half])
            set_tile(n_half, n_half-1, 0, my_board[:n_half, n_half:])
            set_tile(n_half, 0, n_half-1, my_board[n_half:, :n_half])
            set_tile(n_half, i-n_half, j-n_half, my_board[n_half:, n_half:]) 

set_tile(n, i, j, board)
print('Final Board:\n', board)