

import pygame
import sys


# Initialize pygame
pygame.init()


# Constants
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 10
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 10
CROSS_WIDTH = 10
SPACE = 50


# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CIRCLE_COLOR = (0, 0, 255)
CROSS_COLOR = (255, 0, 0)
TEXT_COLOR = (0, 255, 0)


# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")


# Board representation
board = [[None] * BOARD_COLS for _ in range(BOARD_ROWS)]
player = "X"
game_over = False
winner = None


# Font for game messages
font = pygame.font.Font(None, 70)




# Draw grid lines
def draw_grid():
   screen.fill(WHITE)
   for i in range(1, BOARD_ROWS):
       pygame.draw.line(screen, BLACK, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)
       pygame.draw.line(screen, BLACK, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT), LINE_WIDTH)




# Draw marks (X and O)
def draw_marks():
   for row in range(BOARD_ROWS):
       for col in range(BOARD_COLS):
           if board[row][col] == "O":
               pygame.draw.circle(
                   screen,
                   CIRCLE_COLOR,
                   (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2),
                   CIRCLE_RADIUS,
                   CIRCLE_WIDTH,
               )
           elif board[row][col] == "X":
               pygame.draw.line(
                   screen,
                   CROSS_COLOR,
                   (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                   (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                   CROSS_WIDTH,
               )
               pygame.draw.line(
                   screen,
                   CROSS_COLOR,
                   (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE),
                   (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                   CROSS_WIDTH,
               )




# Check for a winner or tie
def check_winner():
   global game_over, winner


   # Check rows and columns
   for i in range(BOARD_ROWS):
       if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None:
           winner = board[i][0]
           game_over = True
           return
       if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not None:
           winner = board[0][i]
           game_over = True
           return


   # Check diagonals
   if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
       winner = board[0][0]
       game_over = True
       return
   if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
       winner = board[0][2]
       game_over = True
       return


   # Check tie (if board is full)
   if all(board[row][col] is not None for row in range(BOARD_ROWS) for col in range(BOARD_COLS)):
       winner = "Tie"
       game_over = True




# Display winner or tie message
def display_message():
   if winner == "Tie":
       text = font.render("It's a Tie!", True, TEXT_COLOR)
   else:
       text = font.render(f"Player {winner} Wins!", True, TEXT_COLOR)


   text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
   screen.blit(text, text_rect)
   pygame.display.update()
   pygame.time.delay(2000)  # Pause for 2 seconds before restarting
   restart_game()




# Restart game
def restart_game():
   global board, player, game_over, winner
   board = [[None] * BOARD_COLS for _ in range(BOARD_ROWS)]
   player = "X"
   game_over = False
   winner = None
   screen.fill(WHITE)
   draw_grid()




# Main game loop
draw_grid()
running = True


while running:
   draw_marks()
   pygame.display.update()


   if game_over:
       display_message()


   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False


       if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
           x, y = event.pos
           # row, col = y // SQUARE_SIZE, x // SQUARE_SIZE
           row = y // SQUARE_SIZE
           col = x // SQUARE_SIZE


           if board[row][col] is None:
               board[row][col] = player
               player = "O" if player == "X" else "X"


               check_winner()


pygame.quit()
sys.exit()


