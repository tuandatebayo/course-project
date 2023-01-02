import copy
from Heuristic import heuristic
class Board_Status():
    def __init__(self,size):
        self.size = size
        self.board = [[" " for i in range(size)] for j in range(size)]
        self.move_history = []
        self.possible_moves = []

    def score_of_row(self,cordi,cordj,cordf,col):
        colscores = []
        y,x = cordi 
        dy, dx = cordj
        yf,xf = cordf
        row = []                                 
        while y != yf + dy or x != xf + dx:     
            row.append(self.board[y][x])
            y += dy
            x += dx
        for s in range(len(row)-4):
            lis = row[s:s+5]
            blank = lis.count(' ')     
            filled = lis.count(col)
            if blank + filled < 5:  
                score = -1            
            else:                   
                score = filled 
            colscores.append(score)    
        return colscores

    def score_of_col(self,col):
        scores = []
        n = len(self.board)
        for start in range(n):
            scores.extend(self.score_of_row((start, 0),  (0, 1), (start, n-1),     col))
            scores.extend(self.score_of_row((0, start),  (1, 0), (n-1, start),     col))
            scores.extend(self.score_of_row((start, 0),  (1, 1), (n-1, n-1-start), col))
            scores.extend(self.score_of_row((start, 0), (-1, 1), (0, start),       col))        
            if start + 1 < len(self.board):
                scores.extend(self.score_of_row((0, start + 1),      (1, 1), (n-2-start, n-1), col)) 
                scores.extend(self.score_of_row((n -1 , start + 1), (-1, 1), (start+1, n-1),   col))     
        dict = {}
        for i in range(-1,6):
            dict[i] = scores.count(i)
        return dict

    def limit(self,y,x,dy,dx,length):
        yf = y + length*dy                  
        xf = x + length*dx
        while not 0 <= yf < len(self.board) or not 0 <= xf < len(self.board):
            yf -= dy
            xf -= dx        
        return yf,xf

    def score_of_col_contain_cell(self,col,y,x): 
        scores = {(0,1):[],(-1,1):[],(1,0):[],(1,1):[]}
        scores[(0,1)].extend(self.score_of_row(self.limit(y,x,0,-1,4),  (0, 1),  self.limit(y,x,0,1,4), col))
        scores[(1,0)].extend(self.score_of_row(self.limit(y,x,-1,0,4),  (1, 0),  self.limit(y,x,1,0,4), col))
        scores[(1,1)].extend(self.score_of_row(self.limit(y,x,-1,-1,4), (1, 1), self.limit(y,x,1,1,4), col))
        scores[(-1,1)].extend(self.score_of_row(self.limit(y,x,-1,1,4), (1,-1), self.limit(y,x,1,-1,4), col))
        sumcol = {0: {},1: {},2: {},3: {},4: {},5: {},-1: {}} 
        for key in scores:
            for s in scores[key]:
                if key in sumcol[s]:
                    sumcol[s][key] += 1
                else:
                    sumcol[s][key] = 1         
        return sumcol
        
    def sum_direction_value(self,sumcol): 
        for key in sumcol:
            if key == 5:
                sumcol[5] = int(1 in sumcol[5].values())
            else:
                sumcol[key] = sum(sumcol[key].values())

    def is_win(self): 
        X = self.score_of_col('x')
        O = self.score_of_col('o')
        if 5 in X and X[5] == 1:
            return 'YOU WON'
        elif 5 in O and O[5] == 1:
            return 'YOU LOST'
        if (sum(X.values()) == X[-1] and sum(O.values()) == O[-1]) or len(self.move_history) == len(self.board)**2:
            return 'DRAW'        
        return 'Continue playing'

    def add_his(self,move):
        self.move_history.append(move)
        return

    def update_possmove(self,move):
        y,x = move
        if move in self.possible_moves:
            self.possible_moves.remove(move)
        directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(-1,1),(1,-1)]
        for direction in directions:
            dy,dx = direction
            for length in [1,2,3,4]:
                move = self.limit(y,x,dy,dx,length)
                if move not in self.move_history and move not in self.possible_moves:
                    self.possible_moves.append(move)

    def next(self,move,col):
        y,x = move
        next_move = Board_Status(size = self.size)
        next_move.board = copy.deepcopy(self.board)
        next_move.move_history = copy.deepcopy(self.move_history)
        next_move.possible_moves = copy.deepcopy(self.possible_moves)
        next_move.board[y][x] = col
        next_move.add_his(move)
        next_move.update_possmove(move)
        return next_move

    def topmove(self,col):
        S = []
        if col == 'o':
            anticol = 'x'
            for tmove in self.possible_moves:
                a = heuristic(self,col,anticol,tmove)
                S.append((tmove,a))
            S.sort(key = lambda x: x[1],reverse= True)
        else:
            anticol = 'o'
            for tmove in self.possible_moves:
                a = heuristic(self,col,anticol,tmove)
                S.append((tmove,a))
            S.sort(key = lambda x: x[1],reverse= False)
        A = []
        for i in S:
            A.append(i[0])
        return A
        
