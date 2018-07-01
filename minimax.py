#O is minimizing player, X is maximizing player
def evaluate(board):
    #check rows 
    for r in range(0,3):
        if(board[r][0]==board[r][1] and board[r][0]==board[r][2] and board[r][0] != None):
            if(board[r][0]=='O'):
                return -10
            return 10

    #check cols
    for c in range(0,3):
        if(board[0][c]==board[1][c] and board[0][c]==board[2][c]):
            if(board[0][c]=='O'):
                return -10
            return 10

    #check diagonals
    if(board[0][0]==board[1][1] and board[0][0]==board[2][2] and board[1][1] != None):
        if(board[1][1] == 'O'):
            return -10
        return 10

    if(board[0][2]==board[1][1] and board[0][2]==board[2][0] and board[1][1] != None):
        if(board[1][1] == 'O'):
            return -10
        return 10
    
    #no win condition
    return 0 


def openMoves(board):
    openMoves = []

    for r in range(0,3):
        for c in range(0,3):
            if(board[r][c] == None):
                openMoves.add((r,c))
    return openMoves

#minimax function, returns value after considering all possibilities 
#just returns the value of a board at that state, not the move itself
def minimax(board, maximizingPlayer):

    value = evaluate(board)
   
    #if terminal state
    if value != 0:
        return value

    openMoves = openMoves(board)

    if maximizingPlayer:
        bestValue = -100000
        
        #iterate through possible moves/nodes
        for m in openMoves:
            
            #add new move to board
            board[m[0]][m[1]] == 'X'

            #find best value by making recursive call
            return max(bestValue, minimax(board, !maximizingPlayer)
            
            board[m[0]][m[1]] == None 
            
    #if minimizing player
    else:
        bestValue = 100000
        for m in openMoves:
            board[m[0]][m[1]] == 'O'

            return min(bestValue, minimax(board, !maximizingPlayer)

            board[m[0]][m[1]] == None 



