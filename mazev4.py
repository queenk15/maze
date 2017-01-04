# Imports
import pygame
import intersects

# Initialize game engine
pygame.init()


# Window
WIDTH = 800
HEIGHT = 600
SIZE = (900, 700)
TITLE = "Follow the Instructions"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (21, 0, 255)
PURPLE = (138, 29, 125)


# Make a player
player =  [380, 310, 20, 20]
player_vx = 0
player_vy = 0
player_speed = 5

# Make player 2
pplayer =  [500, 310, 20, 20]
pplayer_vx = 0
pplayer_vy = 0
pplayer_speed = 5

#stages
START = 0
PLAYING = 1
END = 2


def setup():
    global stage, pcoins, ppcoins, win1, win2, win3, win4, win5, win6, ticks, time_remaining, player, pplayer
    
    # Make pcoins
    '''SECTION ONE'''
    pcoin1 = [25, 25, 10, 10]
    pcoin2 = [125, 25, 10, 10]
    pcoin3 = [25, 305, 10, 10]
    pcoin4 = [125, 185, 10, 10]
    pcoin5 = [125, 305, 10, 10]
    pcoin6 = [185, 325, 10, 10]
    pcoin7 = [185, 365, 10, 10]
    pcoin8 = [225, 25, 10, 10]
    pcoin9 = [225, 305, 10, 10]
    pcoin10 = [305, 45, 10, 10]
    pcoin11 = [325, 285, 10, 10]
    pcoin12 = [325, 385, 10, 10]
    pcoin13 = [335, 185, 10, 10]
    pcoin14 = [425, 45, 10, 10]
    pcoin15 = [425, 165, 10, 10]
    pcoin16 = [425, 265, 10, 10]
    '''SECTION TWO'''
    pcoin17 = [25, 405, 10, 10]
    pcoin18 = [25, 485, 10, 10]
    pcoin19 = [25, 545, 10, 10]
    pcoin20 = [25, 605, 10, 10]
    pcoin21 = [45, 385, 10, 10]
    pcoin22 = [45, 665, 10, 10]
    pcoin23 = [85, 485, 10, 10]
    pcoin24 = [105, 385, 10, 10]
    pcoin25 = [125, 425, 10, 10]
    pcoin26 = [145, 545, 10, 10]
    pcoin27 = [185, 465, 10, 10]
    pcoin28 = [285, 525, 10, 10]
    pcoin29 = [305, 465, 10, 10]
    pcoin30 = [305, 665, 10, 10]
    pcoin31 = [325, 445, 10, 10]
    pcoin32 = [325, 585, 10, 10]
    pcoin33 = [345, 465, 10, 10]
    pcoin34 = [385, 425, 10, 10]
    pcoin35 = [385, 660, 10, 10]
    pcoin36 = [425, 505, 10, 10]
    pcoin37 = [425, 605, 10, 10]

    pcoins = [pcoin1, pcoin2, pcoin3, pcoin4, pcoin5, pcoin6, pcoin7, pcoin8, pcoin9, pcoin10, pcoin11, pcoin12, pcoin13, pcoin14, pcoin15, pcoin16, pcoin17, pcoin18,
              pcoin19, pcoin20, pcoin21, pcoin22, pcoin23, pcoin24, pcoin25, pcoin26, pcoin27, pcoin28, pcoin29, pcoin30, pcoin31, pcoin32, pcoin33, pcoin34, pcoin35,
              pcoin36, pcoin37]
              
    #Make ppcoins
    '''SECTION three'''
    ppcoin1 = [465, 25, 10, 10]
    ppcoin2 = [465, 65, 10, 10]
    ppcoin3 = [465, 105, 10, 10]
    ppcoin4 = [465, 205, 10, 10]
    ppcoin5 = [525, 85, 10, 10]
    ppcoin6 = [525, 225, 10, 10]
    ppcoin7 = [585, 25, 10, 10]
    ppcoin8 = [665, 25, 10, 10]
    ppcoin9 = [665, 105, 10, 10]
    ppcoin10 = [665, 165, 10, 10]
    ppcoin11 = [665, 225, 10, 10]
    ppcoin12 = [665, 285, 10, 10]
    ppcoin13 = [745, 25, 10, 10]
    ppcoin14 = [805, 305, 10, 10]
    ppcoin15 = [865, 25, 10, 10]
    ppcoin16 = [865, 305, 10, 10]
    '''SECTION four'''
    ppcoin17 = [465, 505, 10, 10]
    ppcoin18 = [465, 605, 10, 10]
    ppcoin19 = [505, 465, 10, 10]
    ppcoin20 = [505, 545, 10, 10]
    ppcoin21 = [545, 505, 10, 10]
    ppcoin22 = [545, 545, 10, 10]
    ppcoin23 = [565, 425, 10, 10]
    ppcoin24 = [585, 545, 10, 10]
    ppcoin25 = [605, 365, 10, 10]
    ppcoin26 = [645, 405, 10, 10]
    ppcoin27 = [665, 445, 10, 10]
    ppcoin28 = [665, 625, 10, 10]
    ppcoin29 = [665, 665, 10, 10]
    ppcoin30 = [685, 505, 10, 10]
    ppcoin31 = [745, 345, 10, 10]
    ppcoin32 = [785, 525, 10, 10]
    ppcoin33 = [805, 385, 10, 10]
    ppcoin34 = [805, 665, 10, 10]
    ppcoin35 = [825, 485, 10, 10]
    ppcoin36 = [865, 445, 10, 10]
    ppcoin37 = [865, 585, 10, 10]

    ppcoins = [ppcoin1, ppcoin2, ppcoin3, ppcoin4, ppcoin5, ppcoin6, ppcoin7, ppcoin8, ppcoin9, ppcoin10, ppcoin11, ppcoin12, ppcoin13, ppcoin14, ppcoin15, ppcoin16,
               ppcoin17, ppcoin18,ppcoin19, ppcoin20, ppcoin21, ppcoin22, ppcoin23, ppcoin24, ppcoin25, ppcoin26, ppcoin27, ppcoin28, ppcoin29, ppcoin30, ppcoin31,
               ppcoin32, ppcoin33, ppcoin34, ppcoin35, ppcoin36, ppcoin37]

    # Make a player
    player =  [380, 310, 20, 20]
    player_vx = 0
    player_vy = 0
    player_speed = 5

    # Make player 2
    pplayer =  [500, 310, 20, 20]
    pplayer_vx = 0
    pplayer_vy = 0
    pplayer_speed = 5

    win1 = False
    win2 = False
    win3 = False
    win4 = False
    win5 = False
    win6 = False
    
    stage = START
    time_remaining = 36
    ticks = 0

# make walls
'''boarder walls'''
wall1 =  [10, 20, 10, 660]
wall2 =  [880, 20, 10, 660]
wall3 =  [10, 10, 880, 10]
wall4 =  [10, 680, 880, 10]
'''left upper corner'''
wall5 =  [40, 40, 180, 10]
wall6 =  [40, 70, 60, 10]
wall7 =  [160, 70, 60, 10]
wall8 =  [120, 70, 20, 100]
wall9 =  [40, 100, 60, 20]
wall10 =  [40, 120, 20, 20]
wall11 =  [40, 140, 60, 20]
wall12 =  [80, 120, 20, 20]
wall13 =  [160, 100, 60, 20]
wall14 =  [160, 120, 20, 20]
wall15 =  [160, 140, 60, 20]
wall16 =  [200, 120, 20, 20]
wall17 =  [40, 180, 20, 10]
wall18 =  [80, 180, 20, 20]
wall19 =  [160, 180, 20, 20]
wall20 =  [200, 180, 20, 10]
wall21 =  [40, 210, 20, 10]
wall22 =  [70, 220, 120, 20]
wall23 =  [200, 210, 20, 10]
wall24 =  [40, 240, 20, 20]
wall25 =  [80, 260, 100, 10]
wall26 =  [200, 240, 20, 20]
wall27 =  [40, 280, 20, 20]
wall28 =  [80, 290, 100, 10]
wall29 =  [200, 280, 20, 20]
wall30 =  [20, 320, 120, 20]
wall31 =  [160, 320, 20, 60]
wall32 =  [200, 330, 120, 10]
wall33 =  [20, 360, 120, 20]
wall34 =  [200, 360, 120, 10]
wall35 =  [240, 40, 40, 20]
wall36 =  [240, 60, 60, 20]
wall37 =  [240, 100, 80, 10]
wall38 =  [240, 130, 80, 10]
wall39 =  [240, 160, 60, 40]
wall40 =  [240, 230, 180, 30]
wall41 =  [240, 280, 80, 30]
wall42 =  [300, 20, 140, 20]
wall43 =  [320, 60, 10, 130]
wall44 =  [350, 60, 10, 130]
wall45 =  [300, 205, 120, 10]
wall46 =  [440, 20, 20, 140]
wall47 =  [380, 60, 40, 100]
wall48 =  [380, 180, 140, 5]
wall49 =  [440, 185, 20, 70]
'''MIDDLE BOX'''
wall50 =  [340, 280, 220, 20]
wall51 =  [340, 280, 20, 60]
wall52 =  [340, 360, 20, 60]
wall53 =  [340, 400, 220, 20]
wall54 =  [540, 280, 20, 60]
wall184 =  [540, 360, 20, 60]
wall185 =  [440, 300, 20, 100]
'''LEFT LOWER CORNER'''
wall55 =  [200, 350, 120, 10]
wall56 =  [20, 380, 20, 20]
wall57 =  [20, 440, 20, 40]
wall58 =  [20, 500, 20, 20]
wall59 =  [20, 560, 20, 20]
wall60 =  [20, 620, 20, 60]
wall61 =  [40, 400, 20, 20]
wall62 =  [40, 460, 20, 20]
wall63 =  [40, 540, 20, 20]
wall64 =  [40, 600, 20, 20]
wall65 =  [60, 420, 20, 20]
wall66 =  [60, 480, 20, 40]
wall67 =  [60, 560, 20, 20]
wall68 =  [60, 620, 20, 20]
wall69 =  [80, 380, 20, 20]
wall70 =  [80, 500, 20, 40]
wall71 =  [80, 580, 20, 20]
wall72 =  [80, 640, 20, 20]
wall73 =  [100, 400, 20, 40]
wall74 =  [100, 460, 20, 20]
wall75 =  [100, 520, 20, 40]
wall76 =  [120, 400, 20, 20]
wall77 =  [120, 480, 20, 20]
wall78 =  [120, 540, 20, 40]
wall79 =  [120, 620, 20, 20]
wall80 =  [140, 420, 20, 20]
wall81 =  [140, 500, 20, 20]
wall82 =  [140, 560, 20, 40]
wall83 =  [140, 640, 20, 20]
wall84 =  [160, 380, 20, 20]
wall85 =  [160, 440, 20, 40]
wall86 =  [160, 520, 20, 20]
wall87 =  [160, 580, 20, 40]
wall88 =  [180, 400, 20, 20]
wall89 =  [180, 480, 20, 20]
wall90 =  [180, 540, 20, 20]
wall91 =  [180, 600, 20, 20]
wall92 =  [180, 640, 20, 40]
wall93 =  [200, 420, 20, 20]
wall94 =  [200, 500, 20, 20]
wall95 =  [200, 560, 20, 20]
wall96 =  [220, 380, 20, 20]
wall97 =  [220, 540, 20, 20]
wall98 =  [220, 580, 20, 20]
wall99 =  [220, 620, 20, 40]
wall100 =  [240, 400, 20, 20]
wall101 =  [240, 440, 20, 80]
wall102 =  [240, 600, 20, 40]
wall103 =  [260, 500, 20, 40]
wall104 =  [260, 560, 20, 20]
wall105 =  [260, 620, 20, 20]
wall106 =  [260, 660, 40, 20]
wall107 =  [280, 400, 20, 80]
wall108 =  [280, 500, 140, 20]
wall109 =  [280, 600, 140, 20]
wall110 =  [280, 620, 40, 20]
wall111 =  [300, 440, 20, 20]
wall112 =  [300, 560, 20, 40]
wall113 =  [300, 620, 20, 20]
wall114 =  [320, 400, 20, 20]
wall115 =  [320, 460, 20, 20]
wall116 =  [320, 540, 20, 20]
wall117 =  [340, 440, 20, 20]
wall118 =  [340, 640, 20, 40]
wall119 =  [360, 420, 20, 60]
wall120 =  [360, 560, 20, 20]
wall121 =  [360, 660, 20, 20]
wall122 =  [380, 620, 20, 20]
wall123 =  [400, 440, 20, 40]
wall124 =  [400, 540, 20, 40]
wall125 =  [400, 620, 20, 40]
wall126 =  [440, 420, 20, 80]
wall127 =  [440, 520, 20, 80]
wall128 =  [440, 620, 20, 60]
'''UPPER LEFT CORNER '''
wall129 =  [760, 320, 120, 20]
wall130 =  [760, 360, 120, 20]
wall131 =  [460, 40, 20, 20]
wall132 =  [460, 80, 20, 20]
wall133 =  [460, 120, 20, 20]
wall134 =  [480, 160, 40, 20]
wall135 =  [480, 220, 20, 40]
wall136 =  [500, 20, 20, 60]
wall137 =  [500, 100, 20, 40]
wall138 =  [520, 40, 20, 40]
wall139 =  [520, 100, 20, 40]
wall140 =  [520, 180, 20, 40]
wall141 =  [520, 240, 20, 20]
wall142 =  [560, 40, 20, 120]
wall143 =  [560, 180, 20, 140]
wall144 =  [600, 20, 20, 260]
wall145 =  [600, 300, 20, 20]
wall146 =  [640, 20, 20, 20]
wall147 =  [640, 60, 20, 260]
wall148 =  [660, 300, 40, 20]
wall149 =  [680, 40, 20, 240]
wall150 =  [720, 20, 20, 100]
wall151 =  [720, 140, 20, 180]
wall152 =  [760, 40, 20, 160]
wall153 =  [760, 220, 20, 100]
wall154 =  [800, 20, 20, 80]
wall155 =  [800, 120, 20, 180]
wall156 =  [840, 40, 20, 180]
wall157 =  [840, 240, 20, 80]
'''LOWER RIGHT CORNER'''
wall158 =  [480, 440, 20, 100]
wall159 =  [480, 560, 20, 100]
wall160 =  [500, 440, 100, 20]
wall161 =  [500, 640, 160, 20]
wall162 =  [680, 640, 180, 20]
wall163 =  [580, 340, 20, 120]
wall164 =  [580, 340, 160, 20]
wall165 =  [720, 360, 20, 60]
wall166 =  [740, 400, 100, 20]
wall167 =  [840, 400, 20, 260]
wall168 =  [640, 380, 40, 20]
wall169 =  [620, 380, 20, 120]
wall170 =  [520, 480, 100, 20]
wall171 =  [520, 480, 20, 60]
wall172 =  [520, 560, 20, 60]
wall173 =  [520, 600, 140, 20]
wall174 =  [680, 600, 140, 20]
wall175 =  [800, 440, 20, 180]
wall176 =  [680, 440, 100, 20]
wall177 =  [680, 380, 20, 80]
wall178 =  [560, 520, 120, 20]
wall179 =  [560, 560, 220, 20]
wall180 =  [660, 480, 20, 40]
wall181 =  [660, 480, 120, 20]
wall182 =  [760, 480, 20, 100]
wall183 =  [780, 440, 20, 20]
'''middle barrier'''
wall186 =  [440, 160, 20, 20]
wall187 =  [440, 250, 20, 40]
wall188 =  [440, 500, 20, 20]
wall189 =  [440, 600, 20, 20]

walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10, wall11, wall12, wall13, wall14, wall15, wall16, wall17, wall18, wall19, wall20,
         wall21, wall22, wall23, wall24, wall25, wall26, wall27, wall28, wall29, wall30, wall31, wall32, wall33, wall34, wall35, wall36, wall37, wall38, wall39,
         wall40, wall41, wall42, wall43, wall44, wall45, wall46, wall47, wall48, wall49, wall50, wall51, wall52, wall53, wall54, wall55, wall56, wall57, wall58,
         wall59, wall60, wall61, wall62, wall63, wall64, wall65, wall66, wall67, wall68, wall69, wall70, wall71, wall72, wall73, wall74, wall75, wall76, wall77,
         wall78, wall79, wall80, wall81, wall82, wall83, wall84, wall85, wall86, wall87, wall88, wall89, wall90, wall91, wall92,  wall93, wall94, wall95, wall96,
         wall97, wall98, wall99, wall100, wall101, wall102, wall103, wall104, wall105, wall106, wall107, wall108, wall109, wall110, wall111, wall112, wall113,
         wall114, wall115, wall116, wall117, wall118, wall119, wall120, wall121, wall122, wall123, wall124, wall125, wall126, wall127, wall128, wall129, wall130,
         wall131, wall132, wall133, wall134, wall135, wall136, wall137, wall138, wall139, wall140, wall141, wall142, wall143, wall144, wall145, wall146, wall147,
         wall148, wall149, wall150, wall151, wall152, wall153, wall154, wall155, wall156, wall157, wall158, wall159, wall160, wall161, wall162, wall163, wall164,
         wall165, wall166, wall167, wall168, wall169, wall170, wall171, wall172, wall173, wall174, wall175, wall176, wall177, wall178, wall179, wall180, wall181,
         wall182, wall183, wall184, wall185, wall186, wall187, wall188, wall189]


goal1 = [360, 300, 80, 100]
goal2 = [460, 300, 80, 100]
    
# Game loop
setup()

win1 = False 
win2 = False
win3 = False
win4 = False
win5 = False
win6 = False
done = False
lose = True

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
        elif event.type == pygame.KEYDOWN:
            
            if stage == START:
                if event.key == pygame.K_SPACE:
                    stage = PLAYING
                  
            elif stage == END:
                if event.key == pygame.K_SPACE:
                    setup()


    if stage == PLAYING:
        pressed = pygame.key.get_pressed()
        
        up = pressed[pygame.K_UP]
        down = pressed[pygame.K_DOWN]
        left = pressed[pygame.K_LEFT]
        right = pressed[pygame.K_RIGHT]

        if up:
            player_vy = -player_speed
        elif down:
            player_vy = player_speed
        else:
            player_vy = 0
            
        if left:
            player_vx = -player_speed
        elif right:
            player_vx = player_speed
        else:
            player_vx = 0

        a = pressed[pygame.K_a]
        w = pressed[pygame.K_w]
        s = pressed[pygame.K_s]
        d = pressed[pygame.K_d]    

        if w:
            pplayer_vy = -pplayer_speed
        elif s:
            pplayer_vy = pplayer_speed
        else:
            pplayer_vy = 0
            
        if a:
            pplayer_vx = -pplayer_speed
        elif d:
            pplayer_vx = pplayer_speed
        else:
            pplayer_vx = 0



            
    # Game logic (Check for collisions, update points, etc.)
    if stage == PLAYING:
        ''' move the player in horizontal direction '''
        player[0] += player_vx

        ''' resolve collisions horizontally '''
        for w in walls:
            if intersects.rect_rect(player, w):        
                if player_vx > 0:
                    player[0] = w[0] - player[2]
                elif player_vx < 0:
                    player[0] = w[0] + w[2]

        ''' move the player in vertical direction '''
        player[1] += player_vy
        
        ''' resolve collisions vertically '''
        for w in walls:
            if intersects.rect_rect(player, w):                    
                if player_vy > 0:
                    player[1] = w[1] - player[3]
                if player_vy < 0:
                    player[1] = w[1] + w[3]

        '''llllllllll'''
        ''' move the player in horizontal direction '''
        pplayer[0] += pplayer_vx

        ''' resolve collisions horizontally '''
        for w in walls:
            if intersects.rect_rect(pplayer, w):        
                if pplayer_vx > 0:
                    pplayer[0] = w[0] - pplayer[2]
                elif pplayer_vx < 0:
                    pplayer[0] = w[0] + w[2]

        ''' move the player in vertical direction '''
        pplayer[1] += pplayer_vy
        
        ''' resolve collisions vertically '''
        for w in walls:
            if intersects.rect_rect(pplayer, w):                    
                if pplayer_vy > 0:
                    pplayer[1] = w[1] - pplayer[3]
                if pplayer_vy < 0:
                    pplayer[1] = w[1] + w[3]

        ''' timer stuff '''
        if stage == PLAYING:
            ticks += 1

            if ticks % refresh_rate == 0:
                time_remaining -= 1

            if time_remaining == 0:
                stage = END

        ''' here is where you should resolve player collisions with screen edges '''
        




        ''' get the coins '''
        pcoins = [c for c in pcoins if not intersects.rect_rect(player, c)]

        if len(pcoins) == 0 and intersects.rect_rect(player, goal1):
            win1 = True
            

        ppcoins = [c for c in ppcoins if not intersects.rect_rect(pplayer, c)]

        if len(ppcoins) == 0 and intersects.rect_rect(pplayer, goal2):
            win2 = True

        if len(ppcoins) < len(pcoins) and intersects.rect_rect(pplayer, goal2) and time_remaining == 0:
            win4 = True

        if len(pcoins) < len(ppcoins) and intersects.rect_rect(player, goal1) and time_remaining == 0:
            win3 = True

        if len(pcoins) < len(ppcoins) and not intersects.rect_rect(player, goal1) and time_remaining == 0:
                             win5 = True
                             
        if len(ppcoins) < len(pcoins) and not intersects.rect_rect(pplayer, goal2) and time_remaining == 0:
                             win6 = True


        if win1 == True:
            stage = END
        if win2 == True:
            stage = END
        if win3 == True:
            stage = END
        if win4 == True:
            stage = END
        if win5 == True:
            stage == END
        if win6 == True:
            stage == END
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)


    ''' game play '''
    pygame.draw.rect(screen, YELLOW, player)
    pygame.draw.rect(screen, BLUE, pplayer)
    
    ''' timer text '''
    font = pygame.font.Font(None, 48)
    timer_text = font.render(str(time_remaining), True, RED)
    screen.blit(timer_text, (380, 370))

    for w in walls:
        pygame.draw.rect(screen, PURPLE, w)

    for c in pcoins:
        pygame.draw.rect(screen, WHITE, c)
    for c in ppcoins:
        pygame.draw.rect(screen, WHITE, c)
        
    if win1:
        font = pygame.font.Font(None, 48)
        text = font.render("You Win YELLOW you collected all of your coins and", 1, WHITE)
        text1 = font.render("went back to your box!", 1, WHITE)
        screen.blit(text, [50, 350])
        screen.blit(text1, [250, 400])
    if win2:
        font = pygame.font.Font(None, 48)
        text = font.render("You Win BLUE you collected all of your coins and", 1, WHITE)
        text1 = font.render("went back to your box!", 1, WHITE)
        screen.blit(text, [50, 350])
        screen.blit(text1, [250, 400])
    if win3:
        font = pygame.font.Font(None, 48)
        text = font.render("You Win YELLOW you collected more coins than Blue and", 1, WHITE)
        text1 = font.render("went back to your box!", 1, WHITE)
        screen.blit(text, [50, 350])
        screen.blit(text1, [250, 400])
    if win4:
        font = pygame.font.Font(None, 48)
        text = font.render("You Win BLUE you collected more coins than Yellow", 1, WHITE)
        text1 = font.render("and went back to your box!", 1, WHITE)
        screen.blit(text, [50, 350])
        screen.blit(text1, [250, 400])
    if win5:
        font = pygame.font.Font(None, 48)
        text = font.render("You Win Blue you collected more of coins than Yellow", 1, WHITE)
        text1 = font.render("and went back to your box!", 1, WHITE)
        screen.blit(text, [50, 350])
        screen.blit(text1, [250, 400])
    if win6:
        font = pygame.font.Font(None, 48)
        text = font.render("You Win Yellow you collected more coins than Blue", 1, WHITE)
        text1 = font.render("and went back to your box!", 1, WHITE)
        screen.blit(text, [50, 350])
        screen.blit(text1, [250, 400])

    pygame.draw.rect(screen, PURPLE, [560, 540, 20, 20])
    pygame.draw.rect(screen, PURPLE, [520, 540, 20, 20])
    pygame.draw.rect(screen, PURPLE, [480, 540, 20, 20])
    pygame.draw.rect(screen, PURPLE, [560, 540, 20, 20])
    pygame.draw.rect(screen, PURPLE, [660, 640, 20, 20])
    pygame.draw.rect(screen, PURPLE, [660, 600, 20, 20])    
    pygame.draw.rect(screen, PURPLE, [500, 80, 20, 20])
    pygame.draw.rect(screen, PURPLE, [560, 160, 20, 20])
    pygame.draw.rect(screen, PURPLE, [600, 280, 20, 20])
    pygame.draw.rect(screen, PURPLE, [680, 280, 20, 20])
    pygame.draw.rect(screen, PURPLE, [640, 40, 20, 20])
    pygame.draw.rect(screen, PURPLE, [720, 120, 20, 20])
    pygame.draw.rect(screen, PURPLE, [760, 200, 20, 20])
    pygame.draw.rect(screen, PURPLE, [800, 100, 20, 20])
    pygame.draw.rect(screen, PURPLE, [840, 220, 20, 20])

    ''' begin/end game text '''
    if stage == START:
        screen.fill(BLACK)
        font = pygame.font.Font(None, 48)
        text1 = font.render("WIN", True, RED)
        text3 = font.render("Try to collect all the coins and get back to your box", True, RED)
        text4 = font.render("before time is up!!!", True, RED)
        text2 = font.render("(Press SPACE to play.)", True, RED)
        screen.blit(text1, [350, 150])
        screen.blit(text2, [225, 200])
        screen.blit(text3, [50, 300])
        screen.blit(text4, [275,350])
    elif stage == END:
        font = pygame.font.Font(None, 48)
        text1 = font.render("Game Over", True, WHITE)
        text2 = font.render("(Press SPACE to restart.)", True, WHITE)
        screen.blit(text1, [310, 150])
        screen.blit(text2, [210, 200])

    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()
    clock.tick(refresh_rate)   

    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)

# Close window and quit
pygame.quit()
