
import random

g0 = [0, 0, 0, 0]
g1 = [0, 0, 0, 0]
g2 = [0, 0, 0, 0]
g3 = [0, 0, 0, 0]

grid = [g0, g1, g2, g3]

def render():
    print(g0)
    print(g1)
    print(g2)
    print(g3)
    print('------------')

def isLost():
    empty = 0
    i = 0
    while i < len(grid):
        j = 0
        while j < len(grid[i]):
            if grid[i][j] == 0:
                empty = empty + 1
            j = j + 1
        i = i + 1

    if empty == 0:
        print('Game Lost!')
        exit()

def left():
    for k in range(4):
        for i in range(4):
            for j in range(3, 0, -1):
                if grid[i][j - 1] == 0 and grid[i][j] != 0:
                    grid[i][j - 1] = grid[i][j]
                    grid[i][j] = 0

    for i in range(4):
        for j in range(3):
            if grid[i][j] == grid[i][j + 1]:
                grid[i][j] = grid[i][j] * 2
                grid[i][j + 1] = 0

    for k in range(4):
        for i in range(4):
            for j in range(3, 0, -1):
                if grid[i][j - 1] == 0 and grid[i][j] != 0:
                    grid[i][j - 1] = grid[i][j]
                    grid[i][j] = 0


def right():
    for k in range(4):
        for i in range(4):
            for j in range(1, 4, 1):
                if grid[i][j - 1] != 0 and grid[i][j] == 0:
                    grid[i][j] = grid[i][j - 1]
                    grid[i][j - 1] = 0

    for i in range(4):
        for j in range(3):
            if grid[i][j] == grid[i][j + 1]:
                grid[i][j] = grid[i][j] * 2
                grid[i][j + 1] = 0

    for k in range(4):
        for i in range(4):
            for j in range(1, 4, 1):
                if grid[i][j - 1] != 0 and grid[i][j] == 0:
                    grid[i][j] = grid[i][j - 1]
                    grid[i][j - 1] = 0

def down():
    for k in range(4):
        for i in range(4):
            for j in range(1, 4, 1):
                if grid[j - 1][i] != 0 and grid[j][i] == 0:
                    grid[j][i] = grid[j - 1][i]
                    grid[j - 1][i] = 0

    for i in range(4):
        for j in range(3):
            if grid[j][i] == grid[j + 1][i]:
                grid[j][i] = grid[j][i] * 2
                grid[j + 1][i] = 0

    for k in range(4):
        for i in range(4):
            for j in range(1, 4, 1):
                if grid[j - 1][i] != 0 and grid[j][i] == 0:
                    grid[j][i] = grid[j - 1][i]
                    grid[j - 1][i] = 0


def up():
    for k in range(4):
        for i in range(4):
            for j in range(3, 0, -1):
                if grid[j - 1][i] == 0 and grid[j][i] != 0:
                    grid[j - 1][i] = grid[j][i]
                    grid[j][i] = 0

    for i in range(4):
        for j in range(3):
            if grid[j][i] == grid[j + 1][i]:
                grid[j][i] = grid[j][i] * 2
                grid[j + 1][i] = 0

    for k in range(4):
        for i in range(4):
            for j in range(3, 0, -1):
                if grid[j - 1][i] == 0 and grid[j][i] != 0:
                    grid[j - 1][i] = grid[j][i]
                    grid[j][i] = 0


def init():
    x = random.randint(0, 3)
    y = random.randint(0, 3)
    a = random.randint(0, 3)
    b = random.randint(0, 3)

    grid[x][y] = 2
    grid[a][b] = 2

def random2():


    validSpot = False

    while validSpot == False:
        x = random.randint(0, 3)
        y = random.randint(0, 3)

        if grid[x][y] == 0:
            validSpot = True
            grid[x][y] = 2



def move():
    validMove = False
    while validMove == False:
        direction = input('{u} for up, {d} for down, {r} for right, {l} for left: ')
        if direction == 'u':
            up()
            validMove = True
        elif direction == 'd':
            down()
            validMove = True
        elif direction == 'r':
            right()
            validMove = True
        elif direction == 'l':
            left()
            validMove = True
        else:
            print('Enter a valid move!')

    random2()
    render()
    isLost()

init()
render()

while True:
    move()

#left()

#right()

#down()

#up()
