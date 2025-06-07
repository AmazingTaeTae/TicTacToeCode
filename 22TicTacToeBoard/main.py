import pygame, sys
# from pygame.locals import *
scale = 2.5
def drawGameBoard():
    pygame.draw.line(windowSurface, BLACK, (100 * scale, 0), (100 * scale, 300 * scale), round(4 * scale))
    pygame.draw.line(windowSurface, BLACK, (200 * scale, 0), (200 * scale, 300 * scale), round(4 * scale))
    pygame.draw.line(windowSurface, BLACK, (0, 100 * scale), (300 * scale, 100 * scale), round(4 * scale))
    pygame.draw.line(windowSurface, BLACK, (0, 200 * scale), (300 * scale, 200 * scale), round(4 * scale))



pygame.init()
windowSurface = pygame.display.set_mode((300 * scale, 300 * scale), 0, 32)
pygame.display.set_caption('Tic Tac Toe')

# Set up the colors.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (111, 0, 225)
YELLOW = (242, 216, 48)

windowSurface.fill(WHITE)
drawGameBoard()
pygame.display.update()

# TODO code so that if the user clicks one of the squares, display O or X on the screen
#  AND put the player move information in one of the box variables

# TODO bring the game logic from ticTacToeCLI.py



box1 = " "
box2 = " "
box3 = " "
box4 = " "
box5 = " "
box6 = " "
box7 = " "
box8 = " "
box9 = " "

def player1Input():
    global box1, box2, box3, box4, box5, box6, box7, box8, box9
    global columnIndex, rowIndex
    if columnIndex == 0 and rowIndex == 0 and box1 == " ":
        box1 = "O"
        pygame.draw.circle(windowSurface, BLUE, (50 * scale, 50 * scale), 25 * scale, round(10 * scale))
        return True
    elif columnIndex == 1 and rowIndex == 0 and box2 == " ":
        box2 = "O"
        pygame.draw.circle(windowSurface, BLUE, (150 * scale, 50 * scale), 25 * scale, round(10 * scale))
        return True
    elif columnIndex == 2 and rowIndex == 0 and box3 == " ":
        box3 = "O"
        pygame.draw.circle(windowSurface, BLUE, (250 * scale, 50 * scale), 25 * scale, round(10 * scale))
        return True
    elif columnIndex == 0 and rowIndex == 1 and box4 == " ":
        box4 = "O"
        pygame.draw.circle(windowSurface, BLUE, (50 * scale, 150 * scale), 25 * scale, round(10 * scale))
        return True
    elif columnIndex == 1 and rowIndex == 1 and box5 == " ":
        box5 = "O"
        pygame.draw.circle(windowSurface, BLUE, (150 * scale, 150 * scale), 25 * scale, round(10 * scale))
        return True
    elif columnIndex == 2 and rowIndex == 1 and box6 == " ":
        box6 = "O"
        pygame.draw.circle(windowSurface, BLUE, (250 * scale, 150 * scale), 25 * scale, round(10 * scale))
        return True
    elif columnIndex == 0 and rowIndex == 2 and box7 == " ":
        box7 = "O"
        pygame.draw.circle(windowSurface, BLUE, (50 * scale, 250 * scale), 25 * scale, round(10 * scale))
        return True
    elif columnIndex == 1 and rowIndex == 2 and box8 == " ":
        box8 = "O"
        pygame.draw.circle(windowSurface, BLUE, (150 * scale, 250 * scale), 25 * scale, round(10 * scale))
        return True
    elif columnIndex == 2 and rowIndex == 2 and box9 == " ":
        box9 = "O"
        pygame.draw.circle(windowSurface, BLUE, (250 * scale, 250 * scale), 25 * scale, round(10 * scale))
        return True
    else:
        print("invalid move")
        return False

def checkPlayer1Won():
    if (box1 == "O" and box2 == "O" and box3 == "O"
            or box4 == "O" and box5 == "O" and box6 == "O"
            or box7 == "O" and box8 == "O" and box9 == "O"
            or box1 == "O" and box4 == "O" and box7 == "O"
            or box2 == "O" and box5 == "O" and box8 == "O"
            or box3 == "O" and box6 == "O" and box9 == "O"
            or box1 == "O" and box5 == "O" and box9 == "O"
            or box3 == "O" and box5 == "O" and box7 == "O"
    ):
        print("player1 has won")
        return True
    return False

def player2Input():
    global box1, box2, box3, box4, box5, box6, box7, box8, box9
    global columnIndex, rowIndex

    if columnIndex == 0 and rowIndex == 0 and box1 == " ":
        box1 = "X"
        basicFont = pygame.font.SysFont(None, round(96 * scale))
        text = basicFont.render("X", True, RED)
        windowSurface.blit(text, (25 * scale, 25 * scale))
        return True
    elif columnIndex == 1 and rowIndex == 0 and box2 == " ":
        box2 = "X"
        basicFont = pygame.font.SysFont(None, round(96 * scale))
        text = basicFont.render("X", True, RED)
        windowSurface.blit(text, (125 * scale, 25 * scale))
        return True
    elif columnIndex == 2 and rowIndex == 0 and box3 == " ":
        box3 = "X"
        basicFont = pygame.font.SysFont(None, round(96 * scale))
        text = basicFont.render("X", True, RED)
        windowSurface.blit(text, (225 * scale, 25 * scale))
        return True
    elif columnIndex == 0 and rowIndex == 1 and box4 == " ":
        box4 = "X"
        basicFont = pygame.font.SysFont(None, round(96 * scale))
        text = basicFont.render("X", True, RED)
        windowSurface.blit(text, (25 * scale, 125 * scale))
        return True
    elif columnIndex == 1 and rowIndex == 1 and box5 == " ":
        box5 = "X"
        basicFont = pygame.font.SysFont(None, round(96 * scale))
        text = basicFont.render("X", True, RED)
        windowSurface.blit(text, (125 * scale, 125 * scale))
        return True
    elif columnIndex == 2 and rowIndex == 1 and box6 == " ":
        box6 = "X"
        basicFont = pygame.font.SysFont(None, round(96 * scale))
        text = basicFont.render("X", True, RED)
        windowSurface.blit(text, (225 * scale, 125 * scale))
        return True
    elif columnIndex == 0 and rowIndex == 2 and box7 == " ":
        box7 = "X"
        basicFont = pygame.font.SysFont(None, round(96 * scale))
        text = basicFont.render("X", True, RED)
        windowSurface.blit(text, (25 * scale, 225 * scale))
        return True
    elif columnIndex == 1 and rowIndex == 2 and box8 == " ":
        box8 = "X"
        basicFont = pygame.font.SysFont(None, round(96 * scale))
        text = basicFont.render("X", True, RED)
        windowSurface.blit(text, (125 * scale, 225 * scale))
        return True
    elif columnIndex == 2 and rowIndex == 2 and box9 == " ":
        box9 = "X"
        basicFont = pygame.font.SysFont(None, round(96 * scale))
        text = basicFont.render("X", True, RED)
        windowSurface.blit(text, (225 * scale, 225 * scale))
        return True
    else:
        print("invalid move")
        return False

def checkPlayer2Won():
    if (box1 == "X" and box2 == "X" and box3 == "X"
            or box4 == "X" and box5 == "X" and box6 == "X"
            or box7 == "X" and box8 == "X" and box9 == "X"
            or box1 == "X" and box4 == "X" and box7 == "X"
            or box2 == "X" and box5 == "X" and box8 == "X"
            or box3 == "X" and box6 == "X" and box9 == "X"
            or box1 == "X" and box5 == "X" and box9 == "X"
            or box3 == "X" and box5 == "X" and box7 == "X"
    ):
        print("player2 has won")
        return True
    return False

def checkGameTie():
    if (box1 != " " and box2 != " " and box3 != " "
        and box4 != " " and box5 != " " and box6 != " "
        and box7 != " " and box8 != " " and box9 != " "):

        print("this match has ended in a tie")
        return True
    return False



whoseTurn = "player1"
isMouseClickEnabled = True



while True:
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and isMouseClickEnabled:
            x = event.pos[0]
            y = event.pos[1]
            columnIndex = x // (100 * scale)
            rowIndex = y // (100 * scale)

            if whoseTurn == "player1":
                validMove = player1Input()
                didPlayer1Win = None
                if validMove == True:
                    didPlayer1Win = checkPlayer1Won()
                    didGameTie = checkGameTie()

                if didPlayer1Win == True:
                    basicFont = pygame.font.SysFont(None, round(50 * scale))
                    text = basicFont.render("Player1 won", True, GREEN)
                    windowSurface.blit(text, (50 * scale, 85 * scale))
                    isMouseClickEnabled = False
                elif didGameTie == True:
                    basicFont = pygame.font.SysFont(None, round(50 * scale))
                    text = basicFont.render("Game tied", True, GREEN)
                    windowSurface.blit(text, (50 * scale, 85 * scale))
                else:
                    whoseTurn = "player2"

            elif whoseTurn == "player2":
                validMove = player2Input()
                if validMove == True:
                    didPlayer2Win = checkPlayer2Won()
                if didPlayer2Win == True:
                    basicFont = pygame.font.SysFont(None, round(50 * scale))
                    text = basicFont.render("Player2 won", True, GREEN)
                    windowSurface.blit(text, (50 * scale, 85 * scale))
                    # display the win text
                    isMouseClickEnabled = False

                else:
                    whoseTurn = "player1"