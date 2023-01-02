import turtle
import time
import math
from AI import best_move
from Board import Board_Status

State = Board_Status(20)

def click(x,y):
    start_time = time.time()
    global colors
    x,y = getindexposition(x,y)
    game_res = State.is_win()
    if game_res in ["YOU LOST", "YOU WON", "DARW"]:
        return 
    if not 0 <= y < len(State.board) or not 0 <= x < len(State.board):
        return
    if State.board[y][x] == ' ':
        draw_XO(x,y,colors['x'])
        State.board[y][x]='x'
        State.add_his((y,x))
        State.update_possmove((y,x))
        game_res = State.is_win()
        if game_res in ["YOU LOST", "YOU WON", "DARW"]:
            draw_ending(game_res)
            return          
        ay,ax = best_move(State,'o')
        draw_XO(ax,ay,colors['o'])
        State.board[ay][ax]='o'    
        State.add_his((ay, ax))
        State.update_possmove((ay, ax))
        game_res = State.is_win()
        if game_res in ["YOU LOST", "YOU WON", "DARW"]:
            draw_ending(game_res)
            return
        end_time = time.time()
        print(end_time - start_time)

def initialize(size):
    global screen,colors
    screen = turtle.Screen()
    screen.onclick(click)
    screen.setup(screen.screensize()[1]*2,screen.screensize()[1]*2)
    screen.setworldcoordinates(-1,size+1,size+1,-1)
    screen.bgcolor('pink')
    screen.tracer(500)
    colors = {'o':turtle.Turtle(),'x':turtle.Turtle(), 'g':turtle.Turtle()}
    colors['o'].color('green')
    colors['x'].color('red')
    for key in colors:
        colors[key].ht()
        colors[key].penup()
        colors[key].speed(0)
    border = turtle.Turtle()
    border.speed(9)
    border.penup()
    side = (size)/2
    i=-1
    for start in range(size+1):
        border.goto(start,side + side *i)    
        border.pendown()
        i*=-1
        border.goto(start,side + side *i)     
        border.penup()
    i=1
    for start in range(size+1):
        border.goto(side + side *i, start)
        border.pendown()
        i *= -1
        border.goto(side + side *i, start)
        border.penup()
    border.ht()
    screen.listen()
    screen.mainloop()
    
def getindexposition(x,y):
    intx, inty = int(x), int(y)
    if x >= 0:
        x = intx
    else:
        x = intx - 1
    if y >= 0:
        y = inty
    else:
        y = inty - 1
    return x, y

def draw_XO(x,y,colturtle):
    if colturtle ==colors['x']:
        colturtle.goto(x+0.1, y+0.1)
        colturtle.pendown()
        colturtle.pensize(0.5)     
        colturtle.left(45)
        colturtle.forward(0.8*math.sqrt(2))
        colturtle.penup()
        colturtle.setx(x+0.1)
        colturtle.pendown()   
        colturtle.right(90)
        colturtle.forward(0.8*math.sqrt(2))
        colturtle.left(45)
        colturtle.penup()
    else:
        colturtle.goto(x+0.5, y+0.1)
        colturtle.pendown()
        colturtle.circle(0.4)
        colturtle.end_fill()
        colturtle.penup()

def draw_ending(g):
    x = turtle.Turtle()
    x.color('blue')
    x.goto(10, 10)
    style = ('Arial', 30)
    if g == 'YOU LOST':
        x.write(g, font=style, align='center')
        x.hideturtle()
    elif g == 'YOU WON':
        x.write(g, font=style, align='center')
        x.hideturtle()
    else:
        x.write(g, font=style, align='center')
        x.hideturtle()

if __name__ == '__main__':
    initialize(State.size)