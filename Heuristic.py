def winning_situation(sumcol):     
    check = False
    for key4 in sumcol[4]:
        if sumcol[4][key4] >=1:
            for key3 in sumcol[3]:
                if key3 != key4 and sumcol[3][key3] >=2:
                        check = True    
    if 1 in sumcol[5].values():
        return 5
    elif len(sumcol[4])>=1 and sum(sumcol[4].values())>=2:
        return 4
    elif check:
        return 4
    else:
        score3 = sorted(sumcol[3].values(),reverse = True)
        if len(score3) >= 2 and score3[0] >= score3[1] >= 2:
            return 3
    return 0
def heuristic(board,col,anticol,move):
    y,x = move
    M = 1000
    adv, dis = 0, 0
    board.board[y][x] = col
    sumcol = board.score_of_col_contain_cell(col,y,x)       
    a = winning_situation(sumcol)
    adv += a * M
    board.sum_direction_value(sumcol)
    adv += sumcol[-1] + 2*sumcol[1] + 6*sumcol[2] + 900*sumcol[3] + 4000*sumcol[4]
    board.board[y][x] = anticol
    sumanticol = board.score_of_col_contain_cell(anticol,y,x)  
    d = winning_situation(sumanticol)
    dis += d * (M-100)
    board.sum_direction_value(sumanticol)
    dis += sumanticol[-1] + 2*sumanticol[1] + 5*sumanticol[2] + 200*sumanticol[3] + 1500*sumanticol[4]
    res = adv + dis
    board.board[y][x]=' '
    return res