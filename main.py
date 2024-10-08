import pygame
import random
import os
pygame.init()
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong Game with Rock-Paper-Scissors")
background_music = os.path.join('Music', 'Background.mp3')
pygame.mixer.music.load(background_music)
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100
BALL_SIZE = 20
PADDLE_SPEED = 10
BALL_SPEED_X = 10 
BALL_SPEED_Y = 10
score_left = 0
score_right = 0
WINNING_SCORE = 11
paddle_left = pygame.Rect(50, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle_right = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH//2 - BALL_SIZE//2, HEIGHT//2 - BALL_SIZE//2, BALL_SIZE, BALL_SIZE)
ball_dx = BALL_SPEED_X
ball_dy = BALL_SPEED_Y * random.choice((-1, 1))
ball_start_side = None  
button_font = pygame.font.Font(None, 36)
button_width = 150
button_height = 50
quit_button = pygame.Rect(WIDTH//2 - button_width//2, HEIGHT//2 + 100, button_width, button_height)
again_button = pygame.Rect(WIDTH//2 - button_width//2, HEIGHT//2 + 30, button_width, button_height)
last_winner = None
def reset_ball():
    global ball_dx, ball_dy
    if ball_start_side == "Left":
        ball.x = paddle_left.right
        ball_dx = BALL_SPEED_X  
    else:
        ball.x = paddle_right.left - BALL_SIZE
        ball_dx = -BALL_SPEED_X 
    ball.y = random.randint(0, HEIGHT - BALL_SIZE)  
    ball_dy = BALL_SPEED_Y * random.choice((-1, 1))
def draw_gradient_background():
    color_start = (173, 216, 230)  
    color_end = (255, 160, 122)  
    for i in range(HEIGHT):
        r = color_start[0] + (color_end[0] - color_start[0]) * i // HEIGHT
        g = color_start[1] + (color_end[1] - color_start[1]) * i // HEIGHT
        b = color_start[2] + (color_end[2] - color_start[2]) * i // HEIGHT
        pygame.draw.line(window, (r, g, b), (0, i), (WIDTH, i))
def draw_game():
    draw_gradient_background()  
    pygame.draw.rect(window, WHITE, paddle_left)
    pygame.draw.rect(window, WHITE, paddle_right)
    pygame.draw.ellipse(window, WHITE, ball)
    pygame.draw.aaline(window, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT))
    font = pygame.font.Font(None, 74)
    score_text = font.render(f"{score_left}  {score_right}", True, WHITE)
    window.blit(score_text, (WIDTH//2 - 50, 20))
    player_font = pygame.font.Font(None, 36)
    p1_label = player_font.render("P1", True, WHITE)
    p2_label = player_font.render("P2", True, WHITE)
    window.blit(p1_label, (paddle_left.x + PADDLE_WIDTH//2 - 10, paddle_left.y - 30))
    window.blit(p2_label, (paddle_right.x + PADDLE_WIDTH//2 - 10, paddle_right.y - 30))
    pygame.display.flip()
def draw_buttons():
    pygame.draw.rect(window, BLUE, quit_button)
    pygame.draw.rect(window, BLUE, again_button)
    quit_text = button_font.render("Quit", True, WHITE)
    again_text = button_font.render("Play Again", True, WHITE)
    window.blit(quit_text, (quit_button.x + 35, quit_button.y + 10))
    window.blit(again_text, (again_button.x + 15, again_button.y + 10))
    pygame.display.flip()
def rock_paper_scissors():
    rps_font = pygame.font.Font(None, 30)  
    instructions = rps_font.render("Left: Paper=1/Rock=2/Scissors=3, Right: Paper=J/Rock=K/Scissors=L", True, WHITE)
    window.fill(BLACK)
    window.blit(instructions, (50, HEIGHT//2 - 50))
    pygame.display.flip()
    choice_left = None
    choice_right = None
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if choice_left is None:
                    if event.key == pygame.K_1:
                        choice_left = 'rock'
                    elif event.key == pygame.K_2:
                        choice_left = 'paper'
                    elif event.key == pygame.K_3:
                        choice_left = 'scissors'
                if choice_right is None:
                    if event.key == pygame.K_j:
                        choice_right = 'rock'
                    elif event.key == pygame.K_k:
                        choice_right = 'paper'
                    elif event.key == pygame.K_l:
                        choice_right = 'scissors'
        window.fill(BLACK)
        window.blit(instructions, (50, HEIGHT//2 - 50))
        if choice_left:
            left_choice_text = rps_font.render(f"Left: {choice_left}", True, GREEN)
            window.blit(left_choice_text, (50, HEIGHT//2 + 50))
        if choice_right:
            right_choice_text = rps_font.render(f"Right: {choice_right}", True, GREEN)
            window.blit(right_choice_text, (WIDTH - 250, HEIGHT//2 + 50))
        pygame.display.flip()
        if choice_left is not None and choice_right is not None:
            if choice_left == choice_right:
                choice_left = None
                choice_right = None
                tie_text = rps_font.render("Tie! Choose again.", True, RED)
                window.blit(tie_text, (WIDTH//2 - 100, HEIGHT//2 + 150))
                pygame.display.flip()
                pygame.time.wait(2000)  
                continue
            elif (choice_left == 'rock' and choice_right == 'scissors') or \
                 (choice_left == 'scissors' and choice_right == 'paper') or \
                 (choice_left == 'paper' and choice_right == 'rock'):
                winner = "Left"
            else:
                winner = "Right"
            winner_text = rps_font.render(f"{winner} Player Wins RPS!", True, GREEN)
            window.fill(BLACK)
            window.blit(winner_text, (WIDTH//2 - 150, HEIGHT//2))
            pygame.display.flip()
            pygame.time.wait(5000)  
            return winner
def game_over_screen(winner):
    window.fill(BLACK)
    font = pygame.font.Font(None, 74)
    win_text = font.render(f"{winner} Player Wins!", True, GREEN)
    window.blit(win_text, (WIDTH//2 - 200, HEIGHT//2 - 100))  
    draw_buttons() 
    pygame.display.flip()
running = True
game_over = False
last_winner = rock_paper_scissors()
ball_start_side = last_winner
reset_ball()
while running:
    if game_over:
        game_over_screen(last_winner)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if quit_button.collidepoint(mouse_pos):
                    running = False
                elif again_button.collidepoint(mouse_pos):
                    score_left = 0
                    score_right = 0
                    game_over = False
                    last_winner = rock_paper_scissors()  
                    ball_start_side = last_winner
                    reset_ball()
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and paddle_left.top > 0:
            paddle_left.y -= PADDLE_SPEED
        if keys[pygame.K_s] and paddle_left.bottom < HEIGHT:
            paddle_left.y += PADDLE_SPEED
        if keys[pygame.K_UP] and paddle_right.top > 0:
            paddle_right.y -= PADDLE_SPEED
        if keys[pygame.K_DOWN] and paddle_right.bottom < HEIGHT:
            paddle_right.y += PADDLE_SPEED
        ball.x += ball_dx
        ball.y += ball_dy
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_dy = -ball_dy
        if ball.colliderect(paddle_left) and ball_dx < 0:
            ball_dx = -ball_dx
        if ball.colliderect(paddle_right) and ball_dx > 0:
            ball_dx = -ball_dx
        if ball.left <= 0:
            score_right += 1
            ball_start_side = "Left"
            reset_ball()
        if ball.right >= WIDTH:
            score_left += 1
            ball_start_side = "Right"
            reset_ball()
        if score_left >= WINNING_SCORE or score_right >= WINNING_SCORE:
            game_over = True
            last_winner = "Left" if score_left > score_right else "Right"
        draw_game()
    pygame.time.delay(15)
pygame.quit()