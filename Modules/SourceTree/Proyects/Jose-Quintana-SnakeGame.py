import pygame
pygame.init() # inicia todos los médules de PuBame

yellow = (251, 230, 70) #Score
black = (0, 0, 0) #pantalla
red = (250, 76, 70) #game over
green = (107, 250, 158) #food
blue = (91, 57, 250) #snake

dis=pygame.display.set_mode((500,400))
pygame.display.update() #actualiza los cambios que ocurtan en la pantalla
pygame.display.set_caption("Snake game by JD") # ARaneserá el nombre del jusse
game_over=False

x1 = 250
y1 = 200

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type== pygame.QUIT: #cierra la pantalla al pinchar la (x))
            game_over=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -10
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 10
    x1 += x1_change
    y1 += y1_change
    dis.fill(black)
    pygame.draw.rect(dis, blue, [x1, y1, 10, 10]) #crea snake 
    pygame.display.update()


    clock.tick(30)

pygame.quit() #termina todo
quit()