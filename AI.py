from Heuristic import heuristic
def best_move(board,col):
    depth = 2
    bestmove = (-1,-1)
    best_value = 0
    anticol = 'x'
    for move in board.topmove(col)[:5]:
        value = minimax(board.next(move,col),move,-100000,100000,depth -1, anticol)
        if  value > best_value:
            best_value = value
            bestmove = move
    if bestmove == (-1,-1):
        return board.topmove(col)[0]
    return bestmove
def minimax(board,move,alpha, beta,depth,col):
    if col == 'o':
        anticol = 'x'
    else:
        anticol = 'o'
    val = heuristic(board,anticol,col,move)
    if depth == 0 or board.is_win() in ["YOU LOST", "YOU WON", "DARW"]:
        return val
    if col =='o':
        value = -9999
        for nmove in board.topmove(col):
            value= max(value,minimax(board.next(nmove,col),nmove,alpha,beta,depth - 1,anticol)+ val)
            alpha = max(value,alpha)
            if alpha >= beta:
                break
        return value         
    else:
        value = 9999
        for nmove in board.topmove(col): 
            value= min(value,val - minimax(board.next(nmove,col),nmove,alpha,beta,depth - 1,anticol))
            beta = min(value,beta)
            if alpha >= beta:
                break
        return value