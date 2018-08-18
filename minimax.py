import sys

#O is minimizing player, X is maximizing player
#evaluates one board state in isolation, not considering future states
def evaluate(board):
    #check rows 
    for r in range(0,3):
        if board[r][0]:
            if(board[r][0]==board[r][1] and board[r][0]==board[r][2]):
                if(board[r][0]=='O'):
                    return -10
                return 10

    #check cols
    for c in range(0,3):
        if board[0][c]:
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

#returns a list of row,col tuples
def openMoves(board):
    openMoves = []

    for r in range(0,3):
        for c in range(0,3):
            if(board[r][c] == None):
                openMoves.append((r,c))
    return openMoves

# minimax function, returns value after considering all possibilities 
# just returns the value of a board at that state, not the move itself
def minimax(board, depth, maximizingPlayer):

    value = evaluate(board)
   
    #return if terminal state, with depth factored in (faster wins)
    if value == 10:
        return value - depth 
    elif value == -10:
        return value + depth

    if isOver(board):
        return 0

    availableMoves = openMoves(board)


    if maximizingPlayer:
        bestValue = -100000
        
        #iterate through possible moves/nodes
        for m in availableMoves:
            if not board[m[0]][m[1]]: 
                #add new move to board
                board[m[0]][m[1]] = 'X'

                #find best value by making recursive call
                bestValue = max(bestValue, minimax(board, depth + 1, not maximizingPlayer))
            
                board[m[0]][m[1]] = None 
        return bestValue
            
    #if minimizing player
    else:
        bestValue = 100000
        for m in availableMoves:
            if not board[m[0]][m[1]]: 
                board[m[0]][m[1]] = 'O'

                bestValue =  min(bestValue, minimax(board, depth + 1, not maximizingPlayer))

                board[m[0]][m[1]] = None 
        return bestValue 

def findBestMove(board):
    bestMove = (None, None)
    bestVal = -10000
    for m in openMoves(board):
        
        # maximizing player makes potential move
        board[m[0]][m[1]] = "X"

        # evaluate board after maximizing player makes move (false since minimizing player goes next)
        value = minimax(board, 0, False)

        # undo move
        board[m[0]][m[1]] = None 
       
        # want highest value since maximizing player (minimizing player wants lowest value)
        if value > bestVal:
            bestVal = value
            bestMove = m

    return bestMove 

#returns new board after playing a move
def playMove(board, spot, piece):
    board[int(spot[0])][int(spot[1])] = str(piece)
    return board            

def prompt():
    tinput = raw_input()
    if str(tinput) == "quit":
        sys.exit(0)
    indexes = tinput.split(' ')
    row = int(indexes[1])
    col = int(indexes[0])
    spot = (row, col)
    return spot
   
def isOver(board):
    for r in range(0,3):
        for c in range(0,3):
            if not board[r][c]:
                return False 
    return True 

def printBoard(board):
    boardString = ""
    for r in range(2, -1, -1):
        for c in range(0, 3):
            if board[r][c]:
                boardString +=  board[r][c] 
            else:
                boardString += " "
            if c < 2: 
                boardString += "|"
        if r > 0:
            boardString += "\n-----\n"
    print(boardString + "\n")

#method that runs the game 
def main():
    print("Board layout is indexed 0-2, enter your move in format 'X-coord Y-coord'")  
    
    aiTurn = True 
    goingFirst = raw_input("Do you want to go first? Y for yes, anything else for no \n")

    if goingFirst == "Y":
        aiTurn = False
    else:
        aiTurn = True

    board = [[None for r in range(3)] for c in range(3)]
    while(evaluate(board) == 0 and not isOver(board)): 
        if(aiTurn):
            print("AI turn")
            board = playMove(board, findBestMove(board), "X")
            printBoard(board)
            aiTurn = not aiTurn
        else:
            print("Your turn")
            humanSpot = prompt()
            board = playMove(board, (humanSpot[0], humanSpot[1]), "O")
            printBoard(board) 
            aiTurn = not aiTurn
    if evaluate(board) == 10:
        print("AI wins")
        printBoard(board)
    elif evaluate(board) == -10:
        print("You win")
        printBoard(board)
    else:
        print("tie")
        printBoard(board)

main()
