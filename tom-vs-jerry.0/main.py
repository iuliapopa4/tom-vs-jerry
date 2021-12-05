import pygame
import os
pygame.font.init()

WIDTH, HEIGHT=900,500
BLACK=(0,0,0)
RED=(255,0,0)
WIN=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")
FENCE=pygame.Rect(WIDTH//2-5, 0, 0, HEIGHT)
SKY=pygame.Rect(0,HEIGHT//2+26,WIDTH,0)

#HEALTH_FONT=pygame.font.SysFont('corbel',30)
WINNER_FONT=pygame.font.SysFont('corbel',100)

FPS=60
VEL=5
ATTACK_VEL=7
MAX_ATTACK=3

TOM_GOT_HIT=pygame.USEREVENT+1
JERRY_GOT_HIT=pygame.USEREVENT+2

TOM=pygame.image.load(os.path.join('resources','tom.png'))
JERRY=pygame.image.load(os.path.join('resources','jerry.png'))
SPACE=pygame.image.load(os.path.join('resources','background.jpg'))
HEALTH=pygame.image.load(os.path.join('resources','health.png'))
TOM_WINS=pygame.image.load(os.path.join('resources','tom_wins.png'))
JERRY_WINS=pygame.image.load(os.path.join('resources','jerry_wins.png'))

def draw_window(jerry,tom,jerry_attack,tom_attack,jerry_health,tom_health,health):
    WIN.blit(SPACE,(0,0))
    pygame.draw.rect(WIN, BLACK, FENCE)
    pygame.draw.rect(WIN, BLACK, SKY)

    #jerry_health_text=HEALTH_FONT.render(f"Health:{jerry_health}",1, (0,0,0))
    #tom_health_text=HEALTH_FONT.render(f"Health:{tom_health}",1, (0,0,0))
    # WIN.blit(jerry_health_text,(WIDTH-jerry_health_text.get_width()-10,10))
    # WIN.blit(tom_health_text,(10,10))
    
    for i in range(tom_health):
        WIN.blit(HEALTH,(i*health.x,0))
    for i in range(jerry_health):
        WIN.blit(HEALTH,(i*health.x+500,0))

    WIN.blit(TOM,(tom.x,tom.y))
    WIN.blit(JERRY,(jerry.x,jerry.y))

    for attack in jerry_attack:
            pygame.draw.rect(WIN,RED,attack)
    for attack in tom_attack:
            pygame.draw.rect(WIN,RED,attack)

    pygame.display.update()

def tom_move(keys_pressed,tom):
    if keys_pressed[pygame.K_a] and tom.x-VEL > 0: #LEFT
        tom.x-=VEL
    if keys_pressed[pygame.K_d] and tom.x+VEL+tom.width < FENCE.x: #RIGHT
        tom.x+=VEL
    if keys_pressed[pygame.K_s] and tom.y+VEL+tom.height < HEIGHT: #DOWN
        tom.y+=VEL
    if keys_pressed[pygame.K_w] and tom.y-VEL+tom.height-15 > SKY.y: #UP
        tom.y-=VEL

def jerry_move(keys_pressed,jerry):
    if keys_pressed[pygame.K_LEFT] and jerry.x-VEL > FENCE.x+FENCE.width: #LEFT
        jerry.x-=VEL
    if keys_pressed[pygame.K_RIGHT] and jerry.x+VEL+jerry.width < WIDTH: #RIGHT
        jerry.x+=VEL
    if keys_pressed[pygame.K_DOWN] and jerry.y+VEL+jerry.height < HEIGHT: #DOWN
        jerry.y+=VEL
    if keys_pressed[pygame.K_UP] and jerry.y-VEL+jerry.height-10 > SKY.y: #UP
        jerry.y-=VEL

def move_attack(tom_attack, jerry_attack, tom, jerry):
    for attack in tom_attack:
        attack.x+=ATTACK_VEL
        if jerry.colliderect(attack):
            pygame.event.post(pygame.event.Event(JERRY_GOT_HIT))
            tom_attack.remove(attack)
        elif attack.x>WIDTH:
            tom_attack.remove(attack)
    for attack in jerry_attack:
        attack.x-=ATTACK_VEL
        if tom.colliderect(attack):
            pygame.event.post(pygame.event.Event(TOM_GOT_HIT))
            jerry_attack.remove(attack)  
        elif attack.x<0:
            jerry_attack.remove(attack)

# def draw_winner(text):
#     draw_text=WINNER_FONT.render(text,1,(0,0,0))
#     WIN.blit(draw_text,(WIDTH//2-draw_text.get_width()/2,HEIGHT/2-draw_text.get_height()/2))
#     pygame.display.update()
#     pygame.time.delay(5000)

    

def main():
    jerry=pygame.Rect(700, 300, 66, 90)
    tom=pygame.Rect(100, 300, 99, 100)
    health=pygame.Rect(40,40,40,40)
    jerry_attack=[]
    tom_attack=[]

    tom_health=10
    jerry_health=10

    clock=pygame.time.Clock()
    run=True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                pygame.quit()

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LCTRL and len(tom_attack)<MAX_ATTACK:
                    attack=pygame.Rect(tom.x+tom.width,tom.y+tom.height//2-2,10,5)
                    tom_attack.append(attack)
                if event.key==pygame.K_RCTRL and len(jerry_attack)<MAX_ATTACK:
                    attack=pygame.Rect(jerry.x,jerry.y+jerry.height//2-2,10,5)
                    jerry_attack.append(attack)
            if event.type==JERRY_GOT_HIT:
                jerry_health-=1
            if event.type==TOM_GOT_HIT:
                tom_health-=1

        # winner_text=""        
        # if jerry_health<=0:
        #     winner_text="Tom wins!"
        # if tom_health<=0:
        #     winner_text="Jerry wins!"
        # if winner_text!="":
        #     draw_winner(winner_text)
        #     break

        if jerry_health<=0:
            WIN.blit(TOM_WINS,(130,40))
            pygame.display.update()
            pygame.time.delay(5000)
            break
        if tom_health<=0:
            WIN.blit(JERRY_WINS,(77,40))
            pygame.display.update()
            pygame.time.delay(5000)
            break

        keys_pressed=pygame.key.get_pressed()
        tom_move(keys_pressed,tom)
        jerry_move(keys_pressed,jerry)
        move_attack(tom_attack, jerry_attack, tom, jerry)

        draw_window(jerry,tom,jerry_attack,tom_attack,jerry_health,tom_health,health)


    main()

if __name__=="__main__":
    main()
