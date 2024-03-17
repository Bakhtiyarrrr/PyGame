import pygame
w, h = 500,500
pygame.init()
screen = pygame.display.set_mode((w,h))
pygame.display.set_caption("Moving of square")
run = True
black = (0,0,0)
green = (0,255,0)
x,y = w//2,h//2
pos = (x,y,20,20)
font = pygame.font.Font(None,30)
i = 0

while run:
    for event in pygame.event.get():
        screen.fill(black)
        pygame.draw.rect(screen,green,pos)
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if x <= 10:
                    i = 1
                    continue
                x -=20
                i = 0
                pos = (x,y,20,20)
            elif event.key == pygame.K_RIGHT:
                if x >= w - 30:
                    i = 2
                    continue
                x += 20
                i = 0
                pos = (x,y,20,20)
            elif event.key == pygame.K_UP:
                if y <= 20:
                    i = 3
                    continue
                y -= 20
                i  = 0
                pos = (x,y,20,20)
            elif event.key == pygame.K_DOWN:
                if y >= h - 30:
                    i = 4
                    continue
                y += 20
                i = 0
                pos = (x, y, 20,20)
       
    if i == 1:         
      text = font.render("You achieved left bound!",True, green) 
      text_rect = text.get_rect(center = (w//2,h//2))
      screen.blit(text,text_rect)
    if i == 2:
      text = font.render("You achieved right bound!",True, green) 
      text_rect = text.get_rect(center = (w//2,h//2))
      screen.blit(text,text_rect)
    if i == 3:
      text = font.render("You achieved upper bound!",True, green) 
      text_rect = text.get_rect(center = (w//2,h//2))
      screen.blit(text,text_rect)
    if i == 4:
      text = font.render("You achieved lower bound!",True, green) 
      text_rect = text.get_rect(center = (w//2,h//2))
      screen.blit(text,text_rect)
      

    
    pygame.display.flip()
    
            