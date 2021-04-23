from colorama import init
init(autoreset=True)
from colorama import Fore, Back, Style
print(Fore.RED + 'loading')
import sys, pygame
import datetime, time
#code prep
#define stuff
#inv defs
def inv2text(inv_dat, dat):
    return inv_dat[ dat ]
def text2inv(text_dat, key):
    return text_dat[key]
def disp_inv(inv, inv_data):
    length = len(inv) - 1
    i = 0
    while i <= length :
        if inv[i] != 0:
            print(inv2text(inv_data, i) + ' ' + str(inv[i]))
        i = i +1
    return '1'
def inv_stash(inv_, text_dat, cmd, stash):
    item = input('drop>>>')
    try:
        print('droping ' + str(inv_[text_dat[item]]) + ' ' +item)
        stash[text_dat[item]] =  inv_[text_dat[item]]
        inv_[text_dat[item]] = 0
    except KeyError:
        print(Fore.RED + 'error: ' + item + 'is not a reconised item\n please try again')
    
    return inv_, stash
#more def
DASH_dir =  'X'
inv_dat_txt = ['key', 'sword', 'shield','wood','rubie','staff']
txt_dat_inv = {'key': 0, 'sword': 1, 'shield': 2, 'wood':3,'rubie':4,'staff':5}
inv = [0,1,1,0,0,1]
stash = [0,0,0,0,0,0]
hp = 5
ded_ = False
#print(inv2text(inv_dat_txt, 2))
#print(text2inv(txt_dat_inv, 'key'))
#print(inv[0])
#print(inv)
#print(len(inv))
disp_inv(inv, inv_dat_txt)
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
fell = pygame.image.load("fell.png")

papers = pygame.image.load("researchnotes.png")
door = pygame.image.load("door.png")
player = pygame.image.load("warior.png")
tree = pygame.image.load("tree.png")
ded = pygame.image.load("ded.png")
treestump = pygame.image.load("treestump.png")
check = pygame.image.load("check.png")
lava = pygame.image.load("lava.png")
lava2 = pygame.image.load("lava.png")
lava3 = pygame.image.load("lava.png")
ico = pygame.image.load("ico.png")
back = pygame.image.load("background.png")
#set up rects
fellrect = fell.get_rect()
doorrect = door.get_rect()
papersrect = papers.get_rect()
backrect = back.get_rect()
playerrect = player.get_rect()
treerect = tree.get_rect()
dedrect = ded.get_rect()
treestumprect = tree.get_rect()
checkrect = check.get_rect()
lavarect =lava.get_rect()
lava2rect =lava2.get_rect()
lava3rect =lava3.get_rect()
#move 
playerrect = playerrect.move(500, 500)
treerect.topleft = (100, 400)
dedrect.topleft = (-900, -900)
fellrect.topleft = (-900, -900)
treestumprect.topleft = (-100, -400)
lavarect = lavarect.move(0, 200)
lava2rect = lava2rect.move(400, 200)
lava3rect = lava3rect.move(690, 200)
doorrect = doorrect.move(200, 200)
papersrect = papersrect.move(300, 400)
#visuals
pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_WAITARROW)
pygame.display.set_icon(ico)
ver = "0.1.1"
pygame.display.set_caption("game " +  'ver ' + ver)
time.sleep(1)
print(Fore.GREEN + 'DONE!')
pygame.mixer.music.load("audio.mp3")
#pygame.mixer.music.play()
while 1:
    # DO NOT USE pygame.display.toggle_fullscreen()
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)
    #pygame.overlay.display((yuv.y, yuv.u, yuv.v))
    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        #keys
        if event.type == pygame.KEYDOWN:
            if ded_ != True:
                if event.key == pygame.K_LEFT:
                    playerrect = playerrect.move(-10, 0)
                    DASH_dir =  '<'
                    ########
                    if  pygame.Rect.colliderect(lavarect, playerrect) == True:
                        print(Fore.YELLOW + 'burn burn')
                        playerrect = playerrect.move(20, 0)
                        hp = hp - 1
                    if  pygame.Rect.colliderect(lava2rect, playerrect) == True:
                        print(Fore.YELLOW + 'burn burn')
                        playerrect = playerrect.move(20, 0)
                        hp = hp - 1
                    if  pygame.Rect.colliderect(lava3rect, playerrect) == True:
                        print(Fore.YELLOW + 'burn burn')
                        playerrect = playerrect.move(20, 0)
                        hp = hp - 1
                        ########
                if event.key == pygame.K_RIGHT:
                    playerrect = playerrect.move(10, 0)
                    DASH_dir =  '>'
                    ########
                    if  pygame.Rect.colliderect(lavarect, playerrect) == True:
                        print(Fore.YELLOW + 'burn burn')
                        playerrect = playerrect.move(-20, 0)
                        hp = hp - 1
                    if  pygame.Rect.colliderect(lava2rect, playerrect) == True:
                        print(Fore.YELLOW + 'burn burn')
                        playerrect = playerrect.move(-20, 0)
                        hp = hp - 1
                    if  pygame.Rect.colliderect(lava3rect, playerrect) == True:
                        print(Fore.YELLOW + 'burn burn')
                        playerrect = playerrect.move(-20, 0)
                        hp = hp - 1
                ##########
                if event.key == pygame.K_UP:
                    playerrect = playerrect.move(0, -10)
                    DASH_dir =  '^'
                ######
                    if  pygame.Rect.colliderect(lavarect, playerrect) == True:
                        print(Fore.YELLOW + 'burn burn')
                        playerrect = playerrect.move(0, 20)
                        hp = hp - 1
                    if  pygame.Rect.colliderect(lava2rect, playerrect) == True:
                        print(Fore.YELLOW + 'burn burn')
                        playerrect = playerrect.move(0, 20)
                        hp = hp - 1
                    if  pygame.Rect.colliderect(lava3rect, playerrect) == True:
                        print(Fore.YELLOW + 'burn burn')
                        playerrect = playerrect.move(0, 20)
                        hp = hp - 1
                ########
                if event.key == pygame.K_DOWN:
                    playerrect = playerrect.move(0, 10)
                    DASH_dir =  'v'
                #####
                    if  pygame.Rect.colliderect(lavarect, playerrect) == True:
                        print(Fore.YELLOW + 'burn burn')
                        playerrect = playerrect.move(0, -20)
                        hp = hp - 1
                    if  pygame.Rect.colliderect(lava2rect, playerrect) == True:
                        print(Fore.YELLOW + 'burn burn')
                        playerrect = playerrect.move(0, -20)
                        hp = hp - 1
                    if  pygame.Rect.colliderect(lava3rect, playerrect) == True:
                        print(Fore.YELLOW + 'burn burn')
                        playerrect = playerrect.move(0, -20)
                        hp = hp - 1
                if event.key == pygame.K_SPACE:
                    if  pygame.Rect.colliderect(checkrect, playerrect) == True:
                        print('E')
                        print(Fore.GREEN + 'DONE!')
                        exit()
                    elif pygame.Rect.colliderect(treerect, playerrect) == True:
                        print('+1 wood')
                        inv[3] = inv[3] + 1
                        treerect.topleft = (-100, -400)
                        treestumprect.topleft = (100, 400)
                    elif pygame.Rect.colliderect(papersrect, playerrect) == True:
                        print('this door deeds a key\nfor now here you go')
                        inv[0] = 1
                        print('+1 key')
                if event.key == pygame.K_e:
                    print('===============inventory===============')
                    disp_inv(inv, inv_dat_txt)
                    print('to stash an item type stash')
                    cmd = input('>>>')
                    if cmd == 'stash':
                        dat = inv_stash(inv, txt_dat_inv, cmd, stash)
                        inv = dat[0]
                        stash = dat[1]
            else:
                print('you died')
                ded_ = False
                hp = 5
                time.sleep(3)
                dedrect.topleft = (-900, -900)
                fellrect.topleft = (-900, -900)
                playerrect.topleft = (500, 500)
                
        if event.type == pygame.MOUSEBUTTONUP:
        #if you only care about the left button
            if event.button == 1:
                if playerrect.collidepoint(event.pos):
                    #button clicked, do button stuff
                    print('hi there my class is ' + class_ + '\nhp: ' + str(hp))
                    print('ready to dash:' + DASH_dir)
                    disp_inv(inv, inv_dat_txt)

    if pygame.Rect.colliderect(doorrect, playerrect) == True:
        if inv[0] != 1:
             playerrect.topleft = (300, 400)
    if hp == 0:
        dedrect.topleft = (0, 0)
        ded_ = True
    screen.fill(black)

    if  pygame.Rect.colliderect(backrect, playerrect) == False:
        ded_ = True
        fellrect.topleft = (0, 0)
    screen.blit(back, backrect)  
    screen.blit(tree, treerect)
    screen.blit(treestump, treestumprect)
    screen.blit(check, checkrect)  
    screen.blit(lava, lavarect)
    screen.blit(lava2, lava2rect)
    screen.blit(lava3, lava3rect)
    screen.blit(papers, papersrect)
    screen.blit(door, doorrect)
    screen.blit(player, playerrect)
    screen.blit(ded, dedrect)
    screen.blit(fell, fellrect)  
    pygame.display.flip()



input()

print(Fore.GREEN + 'DONE!')



