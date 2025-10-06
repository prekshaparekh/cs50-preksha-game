import pygame
from sys import exit
from random import randint


def display_score():
    current_time = int((pygame.time.get_ticks()) / 1000 - start_time)

    score_suf = test_font.render(f'Score: {current_time}', False, (64, 64, 64))
    score_rect = score_suf.get_rect(center=(400, 60))
    screen.blit(score_suf, score_rect)
    return current_time


def spawn_obstacle():
    if randint(0, 2):
        obstacle_rect_list.append(snail.get_rect(bottomright=(randint(900, 1100), 250)))
    else:
        obstacle_rect_list.append(fly.get_rect(bottomright=(randint(900, 1100), 200)))


def player_animation():
    global player_surface, player_index, framerate, index_time
    if player_rect.bottom < 250:
        player_surface = player_jump
    else:
        current_time = pygame.time.get_ticks()

        if current_time - index_time > framerate:
            player_index += 1
            if player_index >= len(player_walk): player_index = 0
            index_time = current_time
            player_surface = player_walk[player_index]


def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 250: screen.blit(snail, obstacle_rect)
            else: screen.blit(fly, obstacle_rect)

        obstacle_list = [obs for obs in obstacle_list if obs.x > 0]
        return obstacle_list
    else:
        return []


def collisons(player_rect, obs):
    if obs:
        for obstacle_rect in obs:
            if player_rect.colliderect(obstacle_rect):
                return False
        return True
    return True


def main():
    global screen, test_font, index_time, framerate, clock, score_suf, score_rect, sky, ground
    global snail1, snail2, snail_index, snail_surface, snail, snail_rect
    global fly_1, fly_2, fly_index, fly_surface, fly, fly_rect
    global obstacle_rect_list, player_walk1, player_walk2, player_index, player_walk
    global player_jump, player_surface, player_rect, player_gravity, score, game_active
    global obsacle_timer, start_time, snail_timer, fly_timer, player_stand, player_stand_rect
    global game_over_suf, game_over_rect, try_again_suf, try_again_rect

    pygame.init()
    screen = pygame.display.set_mode((800, 400))
    pygame.display.set_caption("game ;)")
    test_font = pygame.font.Font('Pixeltype.ttf', 50)
    index_time = 0
    framerate = 200

    clock = pygame.time.Clock()

    score_suf = test_font.render('runner', False, 'black')
    score_rect = score_suf.get_rect(center=(400, 50))

    sky = pygame.image.load('graphics/Sky.png').convert()
    ground = pygame.image.load('graphics/ground.png').convert()

    # obstacle list
    snail1 = pygame.image.load('graphics/snail1.png').convert_alpha()
    snail2 = pygame.image.load('graphics/snail2.png').convert_alpha()
    snail_index = 0
    snail_surface = [snail1, snail2]
    snail = snail_surface[snail_index]
    snail_rect = snail.get_rect(bottomright=(500, 250))

    fly_1 = pygame.image.load('graphics/fly1.png').convert_alpha()
    fly_2 = pygame.image.load('graphics/fly2.png').convert_alpha()
    fly_index = 0
    fly_surface = [fly_1, fly_2]
    fly = fly_surface[fly_index]
    fly_rect = fly.get_rect(bottomright=(600, 200))

    obstacle_rect_list = []

    # player
    player_walk1 = pygame.image.load('graphics/player_walk_1.png').convert_alpha()
    player_walk2 = pygame.image.load('graphics/player_walk_2.png').convert_alpha()
    player_index = 0
    player_walk = [player_walk1, player_walk2]
    player_jump = pygame.image.load('graphics/jump.png').convert_alpha()
    player_surface = player_walk[player_index]
    player_rect = player_surface.get_rect(midbottom=(145, 250))
    player_gravity = 0

    score = 0
    game_active = True
    obsacle_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(obsacle_timer, 1700)
    start_time = int((pygame.time.get_ticks()) / 1000)

    snail_timer = pygame.USEREVENT + 2
    pygame.time.set_timer(snail_timer, 450)

    fly_timer = pygame.USEREVENT + 2
    pygame.time.set_timer(fly_timer, 200)

    player_stand = pygame.image.load('graphics/player_stand.png').convert_alpha()
    player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
    player_stand_rect = player_stand.get_rect(center=(400, 170))
    game_over_suf = test_font.render('Pixel Runner', False, 'black')
    game_over_rect = game_over_suf.get_rect(center=(400, 50))

    try_again_suf = test_font.render('press space to try again!!', False, 'black')
    try_again_rect = try_again_suf.get_rect(center=(400, 345))

    pygame.mouse.set_cursor(pygame.cursors.tri_left)

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if game_active:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if player_rect.bottom >= 250:
                            player_gravity = -23
                    elif event.key == pygame.K_d:
                        player_rect.right += 20
                    elif event.key == pygame.K_a:
                        player_rect.right -= 20

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if player_rect.collidepoint(event.pos):
                        player_gravity = -20
            if game_active:
                if event.type == obsacle_timer:
                    spawn_obstacle()

                if event.type == snail_timer:
                    if snail_index == 0: snail_index = 1
                    else: snail_index = 0
                    snail = snail_surface[snail_index]

                if event.type == fly_timer:
                    if fly_index == 0: fly_index = 1
                    else: fly_index = 0
                    fly = fly_surface[fly_index]

            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    game_active = True
                    obstacle_rect_list.clear()
                    player_rect.midbottom = (145, 250)
                    player_gravity = 0
                    snail_rect.bottomright = (500, 250)
                    start_time = int((pygame.time.get_ticks()) / 1000)

        if game_active:
            screen.blit(sky, (0, 0))
            screen.blit(ground, (0, 250))

            score = display_score()

            player_gravity += 1
            player_rect.y += player_gravity

            if player_rect.bottom > 250: player_rect.bottom = 250

            obstacle_movement(obstacle_rect_list)

            player_animation()
            screen.blit(player_surface, player_rect)
            game_active = collisons(player_rect, obstacle_rect_list)

        else:
            screen.fill((94, 129, 162))
            screen.blit(player_stand, player_stand_rect)
            score_message = test_font.render(f"your score: {score}", False, (0, 204, 102))
            score_rect = score_message.get_rect(center=(400, 300))
            if score == 0:
                screen.blit(game_over_suf, game_over_rect)
                screen.blit(try_again_suf, try_again_rect)
            else:
                screen.blit(score_message, score_rect)
                screen.blit(game_over_suf, game_over_rect)
                screen.blit(try_again_suf, try_again_rect)

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
