#O is minimizing player
def evaluate(board):
    #check rows 
    for r in range(0,3):
        if(board[r][0]==board[r][1] and board[r][0]==board[r][2] and board[r][0] != None):
            if(board[r][0]=='O'):
                return -10
            return 10

    for c in range(0,3):
        if(board[0][c]==board[1][c] and board[0][c]==board[2][c]):
            if(board[0][c]=='O'):
                return -10
            return 10

    if(board[0][0]==board[1][1] and board[0][0]==board[2][2] and board[1][1] != None):
        if(board[1][1] == 'O'):
            return -10
        return 10

    if(board[0][2]==board[1][1] and board[0][2]==board[2][0] and board[1][1] != None):
        if(board[1][1] == 'O'):
            return -10
        return 10
