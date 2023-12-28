import pygame
import sys
import copy

# Initialize pygame
pygame.init()

# Constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
YELLOW = (255, 255, 0)
RED = (255, 0 , 0)
WIDTH, HEIGHT = 400, 400
CELL_SIZE = WIDTH // 8

# Initialize screen and clock
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Reversi (Othello)')
clock = pygame.time.Clock()
last_move = None

def draw_board(board, last_move):
    for y in range(8):
        for x in range(8):
            color = GREEN if (x, y) != last_move else YELLOW
            pygame.draw.rect(screen, color, (x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, BLACK, (x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE), width=1, border_radius=1)
            
            if board[y][x] == 'W':
                pygame.draw.circle(screen, WHITE, (int((x+0.5)*CELL_SIZE), int((y+0.5)*CELL_SIZE)), CELL_SIZE//3)
            elif board[y][x] == 'B':
                pygame.draw.circle(screen, BLACK, (int((x+0.5)*CELL_SIZE), int((y+0.5)*CELL_SIZE)), CELL_SIZE//3)



def valid_move(board, x, y, player):
    if board[y][x] != '.':
        return False
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < 8 and 0 <= ny < 8 and board[ny][nx] == opponent(player):
                while 0 <= nx < 8 and 0 <= ny < 8:
                    if board[ny][nx] == player:
                        return True
                    if board[ny][nx] == '.':
                        break
                    nx += dx
                    ny += dy
    return False

def make_move(board, x, y, player):
    board[y][x] = player
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < 8 and 0 <= ny < 8 and board[ny][nx] == opponent(player):
                nx += dx
                ny += dy
                while 0 <= nx < 8 and 0 <= ny < 8:
                    if board[ny][nx] == player:
                        while True:
                            nx -= dx
                            ny -= dy
                            if nx == x and ny == y:
                                break
                            board[ny][nx] = player
                        break
                    if board[ny][nx] == '.':
                        break
                    nx += dx
                    ny += dy

def opponent(player):
    return 'B' if player == 'W' else 'W'

def score(board):
    w, b = 0, 0
    for y in range(8):
        for x in range(8):
            if board[y][x] == 'W':
                w += 1
            elif board[y][x] == 'B':
                b += 1
    return w, b

def alpha_beta(board, depth, alpha, beta, player):
    if depth == 0:
        w, b = score(board)
        return w - b if player == 'W' else b - w

    moves = [(x, y) for x in range(8) for y in range(8) if valid_move(board, x, y, player)]
    if not moves:
        return alpha_beta(board, depth-1, alpha, beta, opponent(player))

    if player == 'W':
        max_val = -float('inf')
        for x, y in moves:
            new_board = copy.deepcopy(board)
            make_move(new_board, x, y, player)
            val = alpha_beta(new_board, depth-1, alpha, beta, opponent(player))
            max_val = max(max_val, val)
            alpha = max(alpha, val)
            if beta <= alpha:
                break
        return max_val
    else:
        min_val = float('inf')
        for x, y in moves:
            new_board = copy.deepcopy(board)
            make_move(new_board, x, y, player)
            val = alpha_beta(new_board, depth-1, alpha, beta, opponent(player))
            min_val = min(min_val, val)
            beta = min(beta, val)
            if beta <= alpha:
                break
        return min_val

def best_move(board, depth, player):
    moves = [(x, y) for x in range(8) for y in range(8) if valid_move(board, x, y, player)]
    if not moves:
        return None

    best = None
    if player == 'W':
        max_val = -float('inf')
        for x, y in moves:
            new_board = copy.deepcopy(board)
            make_move(new_board, x, y, player)
            val = alpha_beta(new_board, depth-1, -float('inf'), float('inf'), opponent(player))
            if val > max_val:
                max_val = val
                best = (x, y)
    else:
        min_val = float('inf')
        for x, y in moves:
            new_board = copy.deepcopy(board)
            make_move(new_board, x, y, player)
            val = alpha_beta(new_board, depth-1, -float('inf'), float('inf'), opponent(player))
            if val < min_val:
                min_val = val
                best = (x, y)
    return best


def game_over(board):
    # Modified to check for no possible moves for both players
    moves_white = any(valid_move(board, x, y, 'W') for x in range(8) for y in range(8))
    moves_black = any(valid_move(board, x, y, 'B') for x in range(8) for y in range(8))
    if not moves_white and not moves_black:
        w, b = score(board)
        if w > b:
            winner = 'W'
        elif b > w:
            winner = 'B'
        else:
            winner = 'Draw'
        return True, winner
    return False, None

def draw_menu(screen):
    screen.fill(GREEN)
    font = pygame.font.Font(None, 36)
    two_player_text = font.render('Two Player Mode', True, BLACK)
    ai_mode_text = font.render('Play Against Computer', True, BLACK)
    two_player_rect = two_player_text.get_rect(center=(WIDTH // 2, HEIGHT // 4))
    ai_mode_rect = ai_mode_text.get_rect(center=(WIDTH // 2, 3 * HEIGHT // 4))
    screen.blit(two_player_text, two_player_rect)
    screen.blit(ai_mode_text, ai_mode_rect)
    return two_player_rect, ai_mode_rect

def display_winner(screen, winner):
    screen.fill(GREEN)
    font = pygame.font.Font(None, 74)
    if winner != 'Draw':
        winner_text = f"Winner: {winner}"
    else:
        winner_text = "Draw"
    text = font.render(winner_text, True, RED)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()


def main():
    global last_move

    # Game Mode Selection
    mode = None
    two_player_rect, ai_mode_rect = draw_menu(screen)
    pygame.display.flip()

    while mode is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if two_player_rect.collidepoint(event.pos):
                    mode = '1'
                elif ai_mode_rect.collidepoint(event.pos):
                    mode = '2'

    # Initialize the board
    board = [['.' for _ in range(8)] for _ in range(8)]
    board[3][3], board[3][4], board[4][3], board[4][4] = 'W', 'B', 'B', 'W'
    current_player = 'W'
    game_over_flag = False
    winner = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if not game_over_flag and event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                x //= CELL_SIZE
                y //= CELL_SIZE
                if valid_move(board, x, y, current_player):
                    make_move(board, x, y, current_player)
                    last_move = (x, y)
                    current_player = opponent(current_player)

        # Check for valid moves and skip turn if none
        if not any(valid_move(board, x, y, current_player) for x in range(8) for y in range(8)):
            current_player = opponent(current_player)

        # For computer move in single-player mode
        if mode == '2' and current_player == 'B' and not game_over_flag:
            move = best_move(board, 3, current_player)
            if move:
                x, y = move
                make_move(board, x, y, current_player)
                last_move = (x, y)
            current_player = opponent(current_player)

        game_over_flag, winner = game_over(board)
        if game_over_flag:
            display_winner(screen, winner)
            pygame.time.wait(10000)  # Wait for 10 seconds before closing
            break

        screen.fill(BLACK)
        draw_board(board, last_move)
        pygame.display.flip()
        clock.tick(100)

if __name__ == "__main__":
    main()
