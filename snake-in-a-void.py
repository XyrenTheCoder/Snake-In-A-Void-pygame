import pygame, random, os.path, pyautogui, time
from datetime import datetime

pyautogui.alert("Welcome to Snake In A Void!\n\n- CONTROLS -\n\nArrow keys: change directions of the snake.\nHold lshift or rshift: sprint\nRelease lshift or rshift: stop sprinting.\nEscape: quit game.\nR key: restart game.\nX key: pause game.\nZ key: show this guide.\n\n- OBJECTS & OBJECTIVES -\n\nYou're a snake who has been trapped inside a void. Your goal is to survive and get as much score as you can.\n\nCyan (ultimate fruit): +10 points\nWhite (fruit): +5 points\nRed (bomb): -20 points\nGrey & window borders (wall): kills you when touched\n\nThanks for playing the game!")
#open(".highscore.txt", "x")
with open(".highscore.txt", "r") as file:
    if os.name == 'nt': os.system("attrib +h .highscore.txt")
    else: pass
    file.close()

window_x = 720
window_y = 540

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
init = datetime.now()

bgm = pygame.mixer.Sound("bgm.ogg")
ult_sound = pygame.mixer.Sound("bonus.ogg")
fruit_sound = pygame.mixer.Sound("fruit.ogg")
bomb_sound = pygame.mixer.Sound("bomb.ogg")
death_sound = pygame.mixer.Sound("death.ogg")
click_sound = pygame.mixer.Sound("click.ogg")
restart_sound = pygame.mixer.Sound("restart.ogg")
quit_sound = pygame.mixer.Sound("exit.ogg")

pygame.mixer.music.load('bgm.ogg')
pygame.mixer.music.load('bonus.ogg')
pygame.mixer.music.load('fruit.ogg')
pygame.mixer.music.load('bomb.ogg')
pygame.mixer.music.load('death.ogg')
pygame.mixer.music.load('click.ogg')
pygame.mixer.music.load('restart.ogg')
pygame.mixer.music.load('exit.ogg')

pygame.mixer.Sound.play(bgm, -1)

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

direction = 'RIGHT'
change_to = direction
score = 0

def show_score(color, font, size):
    iscore = pygame.font.SysFont(font, size)
    score_surface = iscore.render(f'Score : {str(score)}', True, color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)

def game_over():
    pygame.mixer.Sound.play(death_sound)
    pygame.mixer.music.stop()
    bgm.stop()
    end = datetime.now()
    elapsed = end - init
    f = open(".highscore.txt", 'a')
    f.write(f"{score}\n")
    f.close()
    font = pygame.font.SysFont('segoe ui', 35)
    game_over_surface = font.render(f'Final score: {str(score)} | Elapsed time: {str(elapsed)}', True, white)
    f = open(".highscore.txt").read().splitlines()
    q = list()
    for i in f: q.append(int(i))
    highscore = max(q)
    font2 = pygame.font.SysFont('courier', 30)
    game_over_sub = font2.render(f'Highest score record: {str(highscore)}', True, green)
    font3 = pygame.font.SysFont('segoe ui', 20)
    game_over_restart = font3.render('R: restart | ESC: quit | Z: how to play guide', True, blue)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect2 = game_over_surface.get_rect()
    game_over_rect3 = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x/2, window_y/4)
    game_over_rect2.midbottom = (window_x/2, window_y/2+100)
    game_over_rect3.bottomleft = (window_x/2-350, window_y/2+250)

    game_window.blit(game_over_surface, game_over_rect)
    game_window.blit(game_over_sub, game_over_rect2)
    game_window.blit(game_over_restart, game_over_rect3)
    pygame.display.flip()

    while True:
        for restart in pygame.event.get():
            if restart.type == pygame.KEYDOWN:
                if restart.key == pygame.K_r:
                    pygame.mixer.Sound.play(restart_sound)
                    pygame.mixer.music.stop()
                    time.sleep(1)
                    pygame.quit()
                    os.system(f"python {os.path.basename(__file__)}")
                elif restart.key == pygame.K_z:
                    pygame.mixer.Sound.play(click_sound)
                    pygame.mixer.music.stop()
                    pyautogui.alert("Welcome to Snake In A Void!\n\n- CONTROLS -\n\nArrow keys: change directions of the snake.\nHold lshift or rshift: sprint\nRelease lshift or rshift: stop sprinting.\nEscape: quit game.\nR key: restart game.\nX key: pause game.\nZ key: show this guide.\n\n- OBJECTS & OBJECTIVES -\n\nYou're a snake who has been trapped inside a void. Your goal is to survive and get as much score as you can.\n\nCyan (ultimate fruit): +10 points\nWhite (fruit): +5 points\nRed (bomb): -20 points\nGrey & window borders (wall): kills you when touched\n\nThanks for playing the game!")
                elif restart.key == pygame.K_ESCAPE:
                    pygame.mixer.Sound.play(quit_sound)
                    pygame.mixer.music.stop()
                    time.sleep(1)
                    raise KeyboardInterrupt
                else: pass
            else: pass

while True:
    snake_speed = 10
    if score >= 40: snake_speed = 15
    elif score >= 80: snake_speed = 20
    elif score >= 100: snake_speed = 25
    elif score >= 140: snake_speed = 30
    elif score >= 180: snake_speed = 35
    elif score >= 200: snake_speed = 40

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                pyautogui.alert("Game paused.\nClose this textbox to unpause.")
            if event.key == pygame.K_z:
                pygame.mixer.Sound.play(click_sound)
                pygame.mixer.music.stop()
                pyautogui.alert("Welcome to Snake In A Void!\n\n- CONTROLS -\n\nArrow keys: change directions of the snake.\nHold lshift or rshift: sprint\nRelease lshift or rshift: stop sprinting.\nEscape: quit game.\nR key: restart game.\nX key: pause game.\nZ key: show this guide.\n\n- OBJECTS & OBJECTIVES -\n\nYou're a snake who has been trapped inside a void. Your goal is to survive and get as much score as you can.\n\nCyan (ultimate fruit): +10 points\nWhite (fruit): +5 points\nRed (bomb): -20 points\nGrey & window borders (wall): kills you when touched\n\nThanks for playing the game!")
            if event.key == pygame.K_UP:
                change_to = 'UP'
                pygame.mixer.Sound.play(click_sound)
                pygame.mixer.music.stop()
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
                pygame.mixer.Sound.play(click_sound)
                pygame.mixer.music.stop()
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
                pygame.mixer.Sound.play(click_sound)
                pygame.mixer.music.stop()
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
                pygame.mixer.Sound.play(click_sound)
                pygame.mixer.music.stop()
            if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                snake_speed += 10
                pygame.mixer.Sound.play(click_sound)
                pygame.mixer.music.stop()
            if event.key == pygame.K_ESCAPE:
                pygame.mixer.Sound.play(quit_sound)
                pygame.mixer.music.stop()
                time.sleep(1)
                raise KeyboardInterrupt
            if event.key == pygame.K_r:
                pygame.mixer.Sound.play(restart_sound)
                pygame.mixer.music.stop()
                time.sleep(1)
                pygame.quit()
                os.system(f"python {os.path.basename(__file__)}")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT: snake_speed -= 10

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
        pygame.mixer.Sound.play(fruit_sound)
        pygame.mixer.music.stop()
        fruit_spawn = False
    elif snake_position[0] == ult_pos[0] and snake_position[1] == ult_pos[1]:
        score += 10
        pygame.mixer.Sound.play(ult_sound)
        pygame.mixer.music.stop()
        ult_spawn = False
    elif snake_position[0] == bomb_pos[0] and snake_position[1] == bomb_pos[1]:
        score -= 20
        pygame.mixer.Sound.play(bomb_sound)
        pygame.mixer.music.stop()
        bomb_spawn = False
    elif snake_position[0] == wall_pos0[0] and snake_position[1] == wall_pos0[1] or snake_position[0] == wall_pos1[0] and snake_position[1] == wall_pos1[1] or snake_position[0] == wall_pos2[0] and snake_position[1] == wall_pos2[1] or snake_position[0] == wall_pos3[0] and snake_position[1] == wall_pos3[1]:
        game_over()
        break
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
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
            break

    show_score(white, 'segoe ui', 20)
    pygame.display.update()
    fps.tick(snake_speed)
