import pygame, random, os, os.path

with open(".highscore.txt", "+r") as file:
    if os.name == 'nt': os.system("attrib +h .highscore.txt")
    else: pass
    file.close()

window_x = 720
window_y = 480

black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
grey = pygame.Color(50,50,50)
red = pygame.Color(255,0,0)
green = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)
cyan = pygame.Color(0,255,255)

pygame.init()
pygame.display.set_caption('Now playing: Snake In A Void')
game_window = pygame.display.set_mode((window_x, window_y))
fps = pygame.time.Clock()

snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

fruit_pos0 = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]
fruit_pos1 = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]
fruit_pos2 = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]
ult_pos = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]
bomb_pos = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]
wall_pos0 = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]
wall_pos1 = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]
wall_pos2 = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]
wall_pos3 = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]

fruit_spawn = True
ult_spawn = True
bomb_spawn = True
wall_spawn = True

snake_speed = 15
direction = 'RIGHT'
change_to = direction
score = 0

def show_score(color, font, size):
    iscore = pygame.font.SysFont(font, size)
    score_surface = iscore.render(f'Score : {str(score)}', True, color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)

def game_over():
    f = open(".highscore.txt", 'a')
    f.write(f"{score}\n")
    f.close()
    font = pygame.font.SysFont('segoe ui', 50)
    game_over_surface = font.render(f'Your score is : {str(score)}', True, white)
    f = open(".highscore.txt").read().splitlines()
    q = list()
    for i in f: q.append(int(i))
    highscore = max(q)
    font2 = pygame.font.SysFont('courier', 30)
    game_over_sub = font2.render(f'Highest score record: {str(highscore)}', True, green)
    font3 = pygame.font.SysFont('segoe ui', 20)
    game_over_restart = font3.render('-Press R to restart, Press ESC to quit game-', True, blue)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect2 = game_over_surface.get_rect()
    game_over_rect3 = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x/2, window_y/4)
    game_over_rect2.midbottom = (window_x/2-58, window_y/2+100)
    game_over_rect3.bottomleft = (window_x/2-350, window_y/2+250)

    game_window.blit(game_over_surface, game_over_rect)
    game_window.blit(game_over_sub, game_over_rect2)
    game_window.blit(game_over_restart, game_over_rect3)
    pygame.display.flip()

    for restart in pygame.event.get():
        if restart.type == pygame.KEYDOWN:
            if restart.key == pygame.K_r:
                pygame.quit()
                os.system(f"python {os.path.basename(__file__)}")
            elif restart.key == pygame.K_ESCAPE: raise KeyboardInterrupt
            else: pass
        else: pass

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: change_to = 'UP'
            if event.key == pygame.K_DOWN: change_to = 'DOWN'
            if event.key == pygame.K_LEFT: change_to = 'LEFT'
            if event.key == pygame.K_RIGHT: change_to = 'RIGHT'
            if event.key == pygame.K_ESCAPE: raise KeyboardInterrupt
            if event.key == pygame.K_r:
                pygame.quit()
                os.system(f"python {os.path.basename(__file__)}")

    if change_to == 'UP' and direction != 'DOWN': direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP': direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT': direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT': direction = 'RIGHT'
    if direction == 'UP': snake_position[1] -= 10
    if direction == 'DOWN': snake_position[1] += 10
    if direction == 'LEFT': snake_position[0] -= 10
    if direction == 'RIGHT': snake_position[0] += 10

    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_pos0[0] and snake_position[1] == fruit_pos0[1] or snake_position[0] == fruit_pos1[0] and snake_position[1] == fruit_pos1[1] or snake_position[0] == fruit_pos2[0] and snake_position[1] == fruit_pos2[1]:
        score += 5
        fruit_spawn = False
    elif snake_position[0] == ult_pos[0] and snake_position[1] == ult_pos[1]:
        score += 10
        ult_spawn = False
    elif snake_position[0] == bomb_pos[0] and snake_position[1] == bomb_pos[1]:
        score -= 20
        bomb_spawn = False
    elif snake_position[0] == wall_pos0[0] and snake_position[1] == wall_pos0[1] or snake_position[0] == wall_pos1[0] and snake_position[1] == wall_pos1[1] or snake_position[0] == wall_pos2[0] and snake_position[1] == wall_pos2[1] or snake_position[0] == wall_pos3[0] and snake_position[1] == wall_pos3[1]: game_over()
    else: snake_body.pop()

    if not fruit_spawn:
        fruit_pos0 = [random.randrange(1, (window_x // 10)) * 10, random.randrange(1, (window_y // 10)) * 10]
        fruit_pos1 = [random.randrange(1, (window_x // 10)) * 10, random.randrange(1, (window_y // 10)) * 10]
        fruit_pos2 = [random.randrange(1, (window_x // 10)) * 10, random.randrange(1, (window_y // 10)) * 10]
    if not ult_spawn: ult_pos = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]
    if not bomb_spawn: bomb_pos = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]
    if not wall_spawn:
            wall_pos0 = [random.randrange(1, (window_x // 10)) * 10, random.randrange(1, (window_y // 10)) * 10]
            wall_pos1 = [random.randrange(1, (window_x // 10)) * 10, random.randrange(1, (window_y // 10)) * 10]
            wall_pos2 = [random.randrange(1, (window_x // 10)) * 10, random.randrange(1, (window_y // 10)) * 10]
            wall_pos3 = [random.randrange(1, (window_x // 10)) * 10, random.randrange(1, (window_y // 10)) * 10]

    fruit_spawn = True
    ult_spawn = True
    bomb_spawn = True
    game_window.fill(black)

    for pos in snake_body:
        pygame.draw.rect(game_window, blue, pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(game_window, white, pygame.Rect(fruit_pos0[0], fruit_pos0[1], 10, 10))
        pygame.draw.rect(game_window, white, pygame.Rect(fruit_pos1[0], fruit_pos1[1], 10, 10))
        pygame.draw.rect(game_window, white, pygame.Rect(fruit_pos2[0], fruit_pos2[1], 10, 10))
        pygame.draw.rect(game_window, cyan, pygame.Rect(ult_pos[0], ult_pos[1], 10, 10))
        pygame.draw.rect(game_window, red, pygame.Rect(bomb_pos[0], bomb_pos[1], 10, 10))
        pygame.draw.rect(game_window, grey, pygame.Rect(wall_pos0[0], wall_pos0[1], 10, 10))
        pygame.draw.rect(game_window, grey, pygame.Rect(wall_pos1[0], wall_pos1[1], 10, 10))
        pygame.draw.rect(game_window, grey, pygame.Rect(wall_pos2[0], wall_pos2[1], 10, 10))
        pygame.draw.rect(game_window, grey, pygame.Rect(wall_pos3[0], wall_pos3[1], 10, 10))

    if snake_position[0] < 0 or snake_position[0] > window_x-10: game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10: game_over()

    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]: game_over()

    show_score(white, 'segoe ui', 20)
    pygame.display.update()
    fps.tick(snake_speed)
