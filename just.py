import pygame
import datetime
# в этом коде можно приостановить время на часах и сделать так чтобы оно показывало нужное время 

pygame.init()
w,h = (838,837)
screen = pygame.display.set_mode((w,h))
pygame.display.set_caption("Mickey's clock")
run = True

image_clock = pygame.image.load("Labs_pp2/Tsis_7/for_clock/mainclock.png")
left_hand = pygame.image.load("Labs_pp2/Tsis_7/for_clock/leftarm.png")
right_hand = pygame.image.load("Labs_pp2/Tsis_7/for_clock/rightarm.png")
rect = image_clock.get_rect()


left_hand = pygame.transform.rotate(left_hand, -4)
right_hand = pygame.transform.rotate(right_hand, -55.5)

flag = True
i = 0
flag_1 = True

while run:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  run = False
            elif event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_SPACE:
                       flag = not flag
                  if event.key == pygame.K_UP and flag_1 == True:
                       flag_1 = False
                       i = 1
                  elif event.key == pygame.K_UP and flag_1 == False:
                       i = 0
                       flag_1 = True
                        
        
    if flag:
                  
      screen.blit(image_clock, rect)
      current_time = datetime.datetime.now()
      current_seconds = current_time.second
      current_minutes = current_time.minute
      input_minute = 20
      input_second = 5
      if i == 1:
           current_minutes = input_minute
           current_seconds = input_second
           flag = False

      angle_lh = current_seconds * 6
      rotated_left_hand = pygame.transform.rotate(left_hand, -angle_lh)
      rotated_rect_lh = rotated_left_hand.get_rect(center=rect.center)
      screen.blit(rotated_left_hand, rotated_rect_lh)

      angle_rh = (current_minutes * 60 + current_seconds) * 0.1
      rotated_right_hand = pygame.transform.rotate(right_hand, -angle_rh)
      rotated_right_rh = rotated_right_hand.get_rect(center = rect.center)
      screen.blit(rotated_right_hand, rotated_right_rh)

     
          
    pygame.display.flip()
    
    