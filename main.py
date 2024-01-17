import pygame
import math
pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True
pygame.display.set_caption('Dijkstra')
s = set()
ss = tuple()
sd = tuple()
so = set()
path = set()
dist = lambda x,x1,y,y1:math.sqrt((x-x1)**2+(y-y1)**2)


while running:
    mousex,mousey = pygame.mouse.get_pos()
    screen.fill('black')
    for i in range(0,1280,32):
        for j in range(0,720,32):
            if ((i,j) != ss and (i,j) != sd and (i,j) not in path):
                pygame.draw.rect(screen,'green',pygame.Rect(i,j,30,30))
                s.add((i,j))
            elif (i,j) == ss:
                
                pygame.draw.rect(screen,'green',pygame.Rect(ss[0],ss[1],30,30))
                    

                pygame.draw.rect(screen,'yellow',pygame.Rect(i,j,30,30))
                ss = (i,j)
            elif (i,j) == sd:
                pygame.draw.rect(screen,'green',pygame.Rect(sd[0],sd[1],30,30))
                    

                pygame.draw.rect(screen,'blue',pygame.Rect(i,j,30,30))
                sd = (i,j)
            if (i,j) in so:
                pygame.draw.rect(screen,'aqua',pygame.Rect(i,j,30,30))
            
            if (i,j) in path and (i,j) != sd and (i,j) != ss:
                pygame.draw.rect(screen,'white',pygame.Rect(i,j,30,30))
   
    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
        path = set()
        sd = 0
        ss = 0
        so = set()
        



    d = dist(0,mousex,0,mousey)
    c = (0,0)
    for t in s:
        if (dist(t[0],mousex,t[1],mousey)<d):
            d = dist(t[0],mousex,t[1],mousey)
            c = t
    
    rect = pygame.Rect(c[0],c[1],30,30)
    if (c != ss and c != sd):
        pygame.draw.rect(screen, 'red', rect)
        print(c)

    
    
    if pygame.mouse.get_pressed()[1] == 1:
        
        d = dist(0,mousex,0,mousey)
        c = (0,0)
        for t in s:
            if (dist(t[0],mousex,t[1],mousey)<d):
                d = dist(t[0],mousex,t[1],mousey)
                c = t
        rect = pygame.Rect(c[0],c[1],30,30)
        pygame.draw.rect(screen, 'aqua', rect)
        so.add(c)
        s.remove(c)
        
    


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pygame.draw.rect(screen, 'yellow', rect)
            ss = c
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            pygame.draw.rect(screen, 'blue', rect)
            sd = c
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                mp = dict()
                mf = dict()
                for itr in s:
                    mp[itr] = 1280*720
                mp[ss] = 0
                cs = ss
                sdis = set()
                t = [ss]
                
                while (len(t) != 0):
                    
                    if (cs != ss and (cs not in so) and cs != sd):
                        rect = pygame.Rect(cs[0],cs[1],30,30)
                        pygame.draw.rect(screen, 'white', rect)
                        pygame.display.flip()

                    if ((cs[0],cs[1]+32) not in sdis and tuple(cs[0],cs[1]+32) not in so and (cs[0],cs[1]+32) in mp and (cs[0],cs[1]+32) not in t and mp[(cs[0],cs[1]+32)]>mp[cs]+1):
                        mp[(cs[0],cs[1]+32)] = mp[cs]+1
                        mf[(cs[0],cs[1]+32)] = cs
                        t.append((cs[0],cs[1]+32))

                    if ((cs[0]+32,cs[1])not in sdis and tuple(cs[0]+32,cs[1]) not in so and(cs[0]+32,cs[1]) in mp and (cs[0]+32,cs[1]) not in t and mp[(cs[0]+32,cs[1])]>mp[cs]+1):
                        mp[(cs[0]+32,cs[1])] = mp[cs]+1
                        mf[(cs[0]+32,cs[1])] = cs
                        t.append((cs[0]+32,cs[1]))

                    if ((cs[0],cs[1]-32) not in sdis and tuple(cs[0],cs[1]-32) not in so and (cs[0],cs[1]-32) in mp and (cs[0],cs[1]-32) not in t and mp[(cs[0],cs[1]-32)]>mp[cs]+1):
                        mp[(cs[0],cs[1]-32)] = mp[cs]+1
                        mf[(cs[0],cs[1]-32)] = cs
                        t.append((cs[0],cs[1]-32))

                    
                    if ((cs[0]-32,cs[1]) not in sdis and tuple(cs[0]-32,cs[1]) not in so and (cs[0]-32,cs[1]) in mp and (cs[0]-32,cs[1]) not in t and mp[(cs[0]-32,cs[1])]>mp[cs]+1):
                        mp[(cs[0]-32,cs[1])] = mp[cs]+1
                        mf[(cs[0]-32,cs[1])] = cs
                        t.append((cs[0]-32,cs[1]))

                    sdis.add(cs)
                    rect = pygame.Rect(cs[0],cs[1],30,30)
                    print(so)
                    if (cs != ss and (cs not in so) and cs != sd):
                        pygame.draw.rect(screen, 'gray', rect)
                        pygame.display.flip()
                    elif (cs == sd):
                        break
                    if (t):
                        cs = t.pop(0)
                sk = sd
                search = sk
                while search != ss:
                    if (mf.get(sk)):
                        search = mf[sk]
                    else:
                        break
                    
                    if (search != ss and search != sd):
                        path.add(search)
                        rect = pygame.Rect(search[0],search[1],30,30)
                        pygame.draw.rect(screen, 'gray', rect)
                    sk = search

    


    pygame.display.flip()
    clock.tick(60)

pygame.quit()