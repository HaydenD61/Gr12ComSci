import pygame

def main_menu():
    pygame.display.set_caption("Main Menu")
    screen.fill((0, 0, 0))  # Fill the screen with black

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = pygame.font.Font(None, 50).render("Main Menu", True, (0, 255, 0))
        MENU_RECT = MENU_TEXT.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

        PLAY_BUTTON = pygame.font.Font(None, 50).render("Play", True, (0, 255, 0))
        PLAY_RECT = PLAY_BUTTON.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))

        QUIT_BUTTON = pygame.font.Font(None, 50).render("Quit", True, (0, 255, 0))
        QUIT_RECT = QUIT_BUTTON.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))
        if PLAY_RECT.collidepoint(MENU_MOUSE_POS):
            if pygame.mouse.get_pressed()[0]:
                return
        if QUIT_RECT.collidepoint(MENU_MOUSE_POS):
            if pygame.mouse.get_pressed()[0]:
                pygame.quit()
                exit()
        

        screen.blit(MENU_TEXT, MENU_RECT)
        screen.blit(PLAY_BUTTON, PLAY_RECT)
        screen.blit(QUIT_BUTTON, QUIT_RECT)

        pygame.display.update()

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = pygame.Rect(100, 100, 50, 50)

pygame.display.set_caption("Block")

# Main loop
screen.fill((0, 0, 0))  # Fill the screen with black
main_menu()

run = True
while run:
    screen.fill((12, 32, 100))  # Fill the screen with a different color
    pygame.draw.rect(screen, (0, 0, 0), player)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 5
    elif keys[pygame.K_RIGHT]:
        player.x += 5
    elif keys[pygame.K_UP]:
        player.y -= 5
    elif keys[pygame.K_DOWN]:
        player.y += 5
    if player.x < 0:
        player.x = 0
    elif player.x > SCREEN_WIDTH - player.width:
        player.x = SCREEN_WIDTH - player.width
    if player.y < 0:
        player.y = 0
    elif player.y > SCREEN_HEIGHT - player.height:
        player.y = SCREEN_HEIGHT - player.height
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    pygame.display.update()

pygame.quit()
