from colorama import init
init(autoreset=True)
from colorama import Fore, Back, Style
import loader
print(Fore.RED + 'loading')
import sys, pygame
import datetime, time
#code prep
#define stuff
DASH_dir =  'X'
inv_dat_txt = ['key', 'sword', 'shield']
txt_dat_inv = {'key': 0, 'sword': 1, 'shield': 2}
inv = [0,1,1]
stash = [0,0,0]
inv[0] = 0
#print(loader.inv2text(inv_dat_txt, 2))
#print(loader.text2inv(txt_dat_inv, 'key'))
#print(inv[0])
#print(inv)
#print(len(inv))
loader.disp_inv(inv, inv_dat_txt)
#starting
    


#print(Fore.GREEN + str('selected class:' + class_))
class_ = input("class warior mage or archer >>>")
EDIT_CLASS = 'restart game'
if class_.lower() == 'mage':
    print(Fore.GREEN + str('selected class:' + class_))
elif class_.lower() == 'archer':
    print(Fore.GREEN + str('selected class:' + class_))
elif class_.lower() == 'warior':
    print(Fore.GREEN + str('selected class:' + class_))
else:
    print(Fore.RED + 'error \n seting class to warior\n to edit:\n' + EDIT_CLASS)
    class_ = 'warior'
pygame.init()

size = width, height = 920, 840
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

#set up imgs
ball = pygame.image.load("placeholder.png")
check = pygame.image.load("check.png")
lava = pygame.image.load("lava.png")
lava2 = pygame.image.load("lava.png")
lava3 = pygame.image.load("lava.png")
ico = pygame.image.load("ico.png")
#set up rects
ballrect = ball.get_rect()
checkrect = check.get_rect()
lavarect =lava.get_rect()
lava2rect =lava2.get_rect()
lava3rect =lava3.get_rect()
#move 
ballrect = ballrect.move(500, 500)
lavarect = lavarect.move(0, 200)
lava2rect = lava2rect.move(400, 200)
lava3rect = lava3rect.move(650, 200)
#visuals
pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_WAITARROW)
pygame.display.set_icon(ico)
ver = "0.0.1"
pygame.display.set_caption("game " +  'ver ' + ver)
time.sleep(1)
print(Fore.GREEN + 'DONE!')
while 1:
    # DO NOT USE pygame.display.toggle_fullscreen()
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)
    #pygame.overlay.display((yuv.y, yuv.u, yuv.v))
    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        #keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ballrect = ballrect.move(-10, 0)
                DASH_dir =  '<'
                ########
                if  pygame.Rect.colliderect(lavarect, ballrect) == True:
                    print(Fore.YELLOW + 'burn burn')
                    ballrect = ballrect.move(20, 0)
                if  pygame.Rect.colliderect(lava2rect, ballrect) == True:
                    print(Fore.YELLOW + 'burn burn')
                    ballrect = ballrect.move(20, 0)
                if  pygame.Rect.colliderect(lava3rect, ballrect) == True:
                    print(Fore.YELLOW + 'burn burn')
                    ballrect = ballrect.move(20, 0)
                ########
            if event.key == pygame.K_RIGHT:
                ballrect = ballrect.move(10, 0)
                DASH_dir =  '>'
                ########
                if  pygame.Rect.colliderect(lavarect, ballrect) == True:
                    print(Fore.YELLOW + 'burn burn')
                    ballrect = ballrect.move(-20, 0)
                if  pygame.Rect.colliderect(lava2rect, ballrect) == True:
                    print(Fore.YELLOW + 'burn burn')
                    ballrect = ballrect.move(-20, 0)
                if  pygame.Rect.colliderect(lava3rect, ballrect) == True:
                    print(Fore.YELLOW + 'burn burn')
                    ballrect = ballrect.move(-20, 0)
                ##########
            if event.key == pygame.K_UP:
                ballrect = ballrect.move(0, -10)
                DASH_dir =  '^'
                ######
                if  pygame.Rect.colliderect(lavarect, ballrect) == True:
                    print(Fore.YELLOW + 'burn burn')
                    ballrect = ballrect.move(0, 20)
                if  pygame.Rect.colliderect(lava2rect, ballrect) == True:
                    print(Fore.YELLOW + 'burn burn')
                    ballrect = ballrect.move(0, 20)
                if  pygame.Rect.colliderect(lava3rect, ballrect) == True:
                    print(Fore.YELLOW + 'burn burn')
                    ballrect = ballrect.move(0, 20)
            ########
            if event.key == pygame.K_DOWN:
                ballrect = ballrect.move(0, 10)
                DASH_dir =  'v'
                #####
                if  pygame.Rect.colliderect(lavarect, ballrect) == True:
                    print(Fore.YELLOW + 'burn burn')
                    ballrect = ballrect.move(0, -20)
                if  pygame.Rect.colliderect(lava2rect, ballrect) == True:
                    print(Fore.YELLOW + 'burn burn')
                    ballrect = ballrect.move(0, -20)
                if  pygame.Rect.colliderect(lava3rect, ballrect) == True:
                    print(Fore.YELLOW + 'burn burn')
                    ballrect = ballrect.move(0, -20)
            if event.key == pygame.K_SPACE:
                if  pygame.Rect.colliderect(checkrect, ballrect) == True:
                    print('E')
                    print(Fore.GREEN + 'DONE!')
                    exit()
            if event.key == pygame.K_e:
                print('===============inventory===============')
                loader.disp_inv(inv, inv_dat_txt)
                print('to stash an item type stash')
                cmd = input('>>>')
                if cmd == 'stash':
                    dat = loader.inv_stash(inv, txt_dat_inv, cmd, stash)
                    inv = dat[0]
                    stash = dat[1]
        if event.type == pygame.MOUSEBUTTONUP:
        #if you only care about the left button
            if event.button == 1:
                if ballrect.collidepoint(event.pos):
                    #button clicked, do button stuff
                    print('hi there my class is ' + class_)
                    print('ready to dash:' + DASH_dir)
                    loader.disp_inv(inv, inv_dat_txt)


    

    screen.fill(black)
    screen.blit(ball, ballrect)
    screen.blit(check, checkrect)
    screen.blit(lava, lavarect)
    screen.blit(lava2, lava2rect)
    screen.blit(lava3, lava3rect) 
    pygame.display.flip()



input()

print(Fore.GREEN + 'DONE!')



