import pygame
from sys import exit
from random import randint, choice



pygame.init()
width =  800
height = 400
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Pongus')
light_grey = (200,200,200)
clock = pygame.time.Clock()
## left paddle
left_paddle_surf= pygame.image.load('original.jpg').convert_alpha()
left_paddle_y_pos = 150
left_paddle_rect = left_paddle_surf.get_rect(topleft = (30, left_paddle_y_pos))
## right paddle
right_paddle_surf = pygame.image.load('original.jpg').convert_alpha()
right_paddle_y_pos = 150
right_paddle_rect = right_paddle_surf.get_rect(topleft = (770, right_paddle_y_pos))
## background
background_surface = pygame.image.load('amogus.jpg').convert_alpha()
## bogus
bogus_surf = pygame.image.load('bogus.jpg').convert_alpha()
bogus_rect= bogus_surf.get_rect(center = (width/2,height/2))
x_bogus = 400
y_bogus = 200
velocidade_x_de_bogus = 2
velocidade_y_de_bogus = 2
subindo = 2
descendo = 2
esquerda = 2
direita =2 
## score do pongus
score_left = 0
score_right = 0
fonte = pygame.font.Font('freesansbold.ttf',32)
while True : 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
    x_bogus -= velocidade_x_de_bogus
    y_bogus -= velocidade_y_de_bogus


    ## movimentos dos paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        left_paddle_y_pos -= 3
    if keys[pygame.K_s]:
        left_paddle_y_pos += 3
    if keys[pygame.K_UP]:
        right_paddle_y_pos -= 3
    if keys[pygame.K_DOWN]:
        right_paddle_y_pos += 3
    if left_paddle_y_pos <=0 :
        left_paddle_y_pos = 0
    elif left_paddle_y_pos >= 320: 
        left_paddle_y_pos = 320
    if right_paddle_y_pos <= 0: 
        right_paddle_y_pos = 0
    if right_paddle_y_pos >= 320:
        right_paddle_y_pos = 320
    ## quicadas com as paredes
    if y_bogus <= 0 or y_bogus >= height-20:
        velocidade_y_de_bogus *= -1
    
    
    ## quicadas com os paddles
    if right_paddle_rect.collidepoint((x_bogus,y_bogus)):
        velocidade_x_de_bogus *= -1
        print('bingus')
    if left_paddle_rect.collidepoint((x_bogus,y_bogus)):
        velocidade_x_de_bogus *= -1
        print('bogus')
    ## reset da bola
    if x_bogus <= 0 or x_bogus >= width-20:
        x_bogus = 400
        y_bogus = 200
        

    ## bogus
    right_paddle_rect = right_paddle_surf.get_rect(topleft = (770, right_paddle_y_pos))
    left_paddle_rect = left_paddle_surf.get_rect(topleft = (30, left_paddle_y_pos))
    ## score do pongus
    left_text = fonte.render(f"{score_left}",False, light_grey)
    rigth_text =fonte.render(f"{score_right}",False, light_grey)
    if x_bogus >= 778:
        score_left  += 1
    if x_bogus <= 3 :
        score_right += 1
    

    
    


    


    screen.blit(background_surface,(0,0))
    screen.blit(left_paddle_surf,(30,left_paddle_y_pos))
    screen.blit(right_paddle_surf,(770,right_paddle_y_pos))
    screen.blit(bogus_surf,(x_bogus, y_bogus))
    screen.blit(left_text,(380,200))
    screen.blit(rigth_text,(420,200))
    keys = pygame.key.get_pressed()

    pygame.display.flip()
    clock.tick(120)