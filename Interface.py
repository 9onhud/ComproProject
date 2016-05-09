import pygame, sys, Heroes, Monsters, Item, random
from pygame.locals import *
pygame.init()
Display = pygame.display.set_mode((800,600))
pygame.display.set_caption('Nimble Quest BETA Test!')
nimble = pygame.image.load('NimbleQuestBeta.jpg')
pickHero = pygame.image.load('CharSelectBackground.jpg')
pickWarrior = pygame.image.load('PickWarrior.jpg')
pickArcher = pygame.image.load('PickArcher.jpg')
pickMage = pygame.image.load('PickMage.jpg')
pickPriest = pygame.image.load('PickPriest.jpg')
wingame = pygame.image.load('Congrat.png')
lost = pygame.image.load('Lost.png')
winmap = pygame.image.load('Win.png')
endcredit = pygame.image.load('EndCredit.jpg')
FPS = 10
time = 0
FPSclock = pygame.time.Clock()
direction = "right"
gameplay = 'Begin'
mapgame,pick = 0,0
def moveParty(party):
    if len(party)!=0:
        for i in range(len(party)-1,0,-1):
            party[i].x = party[i-1].x
            party[i].y = party[i-1].y
            party[i].direction = party[i-1].direction
        party[0].move()
        
hero = Heroes.Hero(direction)
warrior = Heroes.Warrior(hero.direction)
arc = Heroes.Archer(hero.direction)
mage = Heroes.Mage(hero.direction)
pri = Heroes.Priest(hero.direction)
monster = Monsters.Monster()
potion = Item.Potion()
allItem = [potion]

while True:
    events = pygame.event.get()
    if mapgame==0:
        if pick==0:
            Display.blit(nimble,(0,0))
            for e in events:
                if e.type==MOUSEBUTTONDOWN:
                    x,y = e.pos
                    if (x in range(672,762)) and (y in range(515,560)):
                        pick = 0.5
        elif pick==0.5:
            Display.blit(pickHero,(0,0))
            for e in events:
                if e.type==MOUSEBUTTONDOWN:
                    x,y = e.pos
                    if (x in range(50,80)) and (y in range(40,100)):
                        pick = 1
                    elif (x in range(35,65)) and (y in range(140,210)):
                        pick = 2
                    elif (x in range(70,100)) and (y in range(282,352)):
                        pick = 3
                    elif (x in range(10,40)) and (y in range(460,535)):
                        pick = 4
        elif pick==1:
            Display.blit(pickWarrior,(0,0))
            for e in events:
                if e.type==MOUSEBUTTONDOWN:
                    x,y = e.pos
                    if (x in range(35,65)) and (y in range(140,210)):
                        pick = 2
                    elif (x in range(70,100)) and (y in range(282,352)):
                        pick = 3
                    elif (x in range(10,40)) and (y in range(460,535)):
                        pick = 4                    
                    elif (x in range(610,676)) and (y in range(460,495)):
                        mapgame = 1
                        beginHero = Heroes.Warrior(hero.direction)
                        allHero = [arc,mage,pri]
        elif pick==2:
            Display.blit(pickArcher,(0,0))
            for e in events:
                if e.type==MOUSEBUTTONDOWN:
                    x,y = e.pos
                    if (x in range(50,80)) and (y in range(40,100)):
                        pick = 1
                    elif (x in range(70,100)) and (y in range(282,352)):
                        pick = 3
                    elif (x in range(10,40)) and (y in range(460,535)):
                        pick = 4                    
                    elif (x in range(610,676)) and (y in range(460,495)):
                        mapgame = 1
                        beginHero = Heroes.Archer(hero.direction)
                        allHero = [warrior,mage,pri]
        elif pick==3:
            Display.blit(pickMage,(0,0))
            for e in events:
                if e.type==MOUSEBUTTONDOWN:
                    x,y = e.pos
                    if (x in range(50,80)) and (y in range(40,100)):
                        pick = 1
                    elif (x in range(35,65)) and (y in range(140,210)):
                        pick = 2
                    elif (x in range(10,40)) and (y in range(460,535)):
                        pick = 4                    
                    elif (x in range(610,676)) and (y in range(460,495)):
                        mapgame = 1
                        beginHero = Heroes.Mage(hero.direction)
                        allHero = [warrior,arc,pri]
        elif pick==4:
            Display.blit(pickPriest,(0,0))
            for e in events:
                if e.type==MOUSEBUTTONDOWN:
                    x,y = e.pos
                    if (x in range(50,80)) and (y in range(40,100)):
                        pick = 1
                    elif (x in range(35,65)) and (y in range(140,210)):
                        pick = 2
                    elif (x in range(70,100)) and (y in range(282,352)):
                        pick = 3                    
                    elif (x in range(610,676)) and (y in range(460,495)):
                        mapgame = 1
                        beginHero = Heroes.Priest(hero.direction)
                        allHero = [warrior,arc,mage]
        roundMon = 1
    if mapgame==1:
        maxRound = 2
        if gameplay=='Begin':
            mapPic = pygame.image.load('Map1.jpg')
            if roundMon==1:
                partyHero = []
                partyHero.append(beginHero)
                allDropHero = []    
                allDropItem = []                
                bat = Monsters.Bat(random.randrange(352,700,32),random.randrange(128,500,32))
                bat1 = Monsters.Bat(random.randrange(352,700,32),random.randrange(128,500,32))
                bat2 = Monsters.Bat(bat1.x-32,bat1.y)
                bat3 = Monsters.Bat(bat1.x-64,bat1.y)
                partyMonster = [[bat1,bat2,bat3]]
                oneMonster = [[bat]]
                allMonster = [bat,bat1,bat2,bat3]
            if roundMon==2:
                bat1 = Monsters.Bat(random.randrange(352,700,32),random.randrange(128,500,32))
                bat2 = Monsters.Bat(bat1.x-32,bat1.y)
                bat3 = Monsters.Bat(bat1.x-64,bat1.y)   
                partyMonster = [[bat1,bat2,bat3]]
                goz = Monsters.Godzilla(random.randrange(352,700,32),random.randrange(128,500,32))
                oneMonster = [[goz]]
                allMonster = [bat1,bat2,bat3,goz]
            gameplay = 'Play'
            time = 0
    elif mapgame==2:
        maxRound = 3
        if gameplay=='Begin':
            mapPic = pygame.image.load('Map2.jpg')
            if roundMon==1:
                allHero.extend(allDropHero)
                allDropHero = []
                allDropItem = []
                bat = Monsters.Bat(random.randrange(352,700,32),random.randrange(128,500,32))
                bat1 = Monsters.Bat(random.randrange(352,700,32),random.randrange(128,500,32))
                bat2 = Monsters.Bat(bat1.x-32,bat1.y)
                bat3 = Monsters.Bat(bat1.x-64,bat1.y)
                bat4 = Monsters.Bat(random.randrange(352,700,32),random.randrange(128,500,32))
                goz1 = Monsters.Godzilla(bat4.x-32,bat4.y)
                goz2 = Monsters.Godzilla(bat4.x-64,bat4.y)                
                partyMonster = [[bat1,bat2,bat3],[bat4,goz1,goz2]]
                oneMonster = [[bat]]
                allMonster = [bat,bat1,bat2,bat3,bat4,goz1,goz2]
            elif roundMon==2:
                bat1 = Monsters.Bat(random.randrange(352,700,32),random.randrange(128,500,32))
                bat2 = Monsters.Bat(bat1.x-32,bat1.y)
                bat3 = Monsters.Bat(bat1.x-64,bat1.y)
                bat4 = Monsters.Bat(random.randrange(352,700,32),random.randrange(128,500,32))
                goz1 = Monsters.Godzilla(bat4.x-32,bat4.y)
                goz2 = Monsters.Godzilla(bat4.x-64,bat4.y)                 
                partyMonster = [[bat1,bat2,bat3],[bat4,goz1,goz2]]                
                goz = Monsters.Godzilla(random.randrange(352,700,32),random.randrange(128,500,32))
                oneMonster = [[goz]]
                allMonster = [bat1,bat2,bat3,bat4,goz1,goz2,goz]         
            elif roundMon==3:
                bat1 = Monsters.Bat(random.randrange(352,700,32),random.randrange(128,500,32))
                bat2 = Monsters.Bat(bat1.x-32,bat1.y)
                bat3 = Monsters.Bat(bat1.x-64,bat1.y)
                goz1 = Monsters.Godzilla(random.randrange(352,700,32),random.randrange(128,500,32))
                goz2 = Monsters.Godzilla(goz1.x-32,goz1.y)
                goz3 = Monsters.Godzilla(goz1.x-32,goz1.y)
                partyMonster = [[bat1,bat2,bat3],[goz1,goz2,goz3]]  
                imp = Monsters.Imp(random.randrange(352,700,32),random.randrange(128,500,32))
                oneMonster = [[imp]]
                allMonster = [bat1,bat2,bat3,goz1,goz2,goz3,imp]
                gob = Monsters.Goblin(random.randrange(352,700,32),random.randrange(128,500,32))
            gameplay = 'Play'
            time = 0
    elif mapgame==3:
        maxRound = 3
        if gameplay=='Begin':
            mapPic = pygame.image.load('Map3.jpg')
            if roundMon==1:
                allHero.extend(allDropHero)
                allDropHero = []
                allDropItem = []                
                bat1 = Monsters.Bat(random.randrange(352,700,32),random.randrange(128,500,32))
                bat2 = Monsters.Bat(bat1.x-32,bat1.y)
                bat3 = Monsters.Bat(bat1.x-64,bat1.y)
                imp1 = Monsters.Imp(random.randrange(352,700,32),random.randrange(128,500,32))
                goz1 = Monsters.Godzilla(imp1.x-32,imp1.y)
                goz2 = Monsters.Godzilla(imp1.x-32,imp1.y)
                partyMonster = [[bat1,bat2,bat3],[imp1,goz1,goz2]]  
                imp = Monsters.Imp(random.randrange(352,700,32),random.randrange(128,500,32))
                goz = Monsters.Godzilla(random.randrange(352,700,32),random.randrange(128,500,32))
                oneMonster = [[imp],[goz]]
                allMonster = [bat1,bat2,bat3,imp1,goz1,goz2,imp,goz]
            elif roundMon==2:
                goz1 = Monsters.Godzilla(random.randrange(352,700,32),random.randrange(128,500,32))
                imp1 = Monsters.Imp(goz1.x-32,goz1.y)
                imp2 = Monsters.Imp(goz1.x-32,goz1.y)                
                imp3 = Monsters.Imp(random.randrange(352,700,32),random.randrange(128,500,32))
                bat1 = Monsters.Bat(imp3.x-32,imp3.y)
                gob1 = Monsters.Goblin(imp3.x-32,imp3.y)
                partyMonster = [[goz1,imp1,imp2],[imp3,bat1,gob1]]  
                imp = Monsters.Imp(random.randrange(352,700,32),random.randrange(128,500,32))
                goz = Monsters.Godzilla(random.randrange(352,700,32),random.randrange(128,500,32))
                gob = Monsters.Goblin(random.randrange(352,700,32),random.randrange(128,500,32))
                oneMonster = [[imp],[goz],[gob]]
                allMonster = [goz1,imp1,imp2,imp3,bat1,gob1,imp,goz,gob]
            elif roundMon==3:
                goz1 = Monsters.Godzilla(random.randrange(352,700,32),random.randrange(128,500,32))
                goz2 = Monsters.Godzilla(goz1.x-32,goz1.y)
                imp1 = Monsters.Imp(goz1.x-32,goz1.y)                 
                imp2 = Monsters.Imp(random.randrange(352,700,32),random.randrange(128,500,32))
                imp3 = Monsters.Imp(imp2.x-32,imp2.y)
                goz3 = Monsters.Godzilla(imp2.x-32,imp2.y)     
                gob1 = Monsters.Goblin(random.randrange(352,700,32),random.randrange(128,500,32)) 
                gob2 = Monsters.Goblin(gob1.x-32,gob1.y)
                imp4 = Monsters.Imp(gob1.x-32,gob1.y) 
                partyMonster = [[goz1,goz2,imp1],[imp2,imp3,goz3],[gob1,gob2,imp4]] 
                bat = Monsters.Bat(random.randrange(352,700,32),random.randrange(128,500,32))
                imp = Monsters.Imp(random.randrange(352,700,32),random.randrange(128,500,32))
                gob = Monsters.Goblin(random.randrange(352,700,32),random.randrange(128,500,32))
                oneMonster = [[bat],[imp],[gob]]
                allMonster = [goz1,goz2,imp1,imp2,imp3,goz3,gob1,gob2,imp4,bat,imp,gob]
            gameplay = 'Play'
            time = 0            
    if mapgame>=1:
        if beginHero not in partyHero:
            gameplay = 'Lost'
        if beginHero.x<192 or beginHero.x>736 or beginHero.y<0 or beginHero.y>512:
            gameplay = 'Lost'
        if len(allMonster)==0 and gameplay!='End':
            gameplay = 'Wait'
        if time>25:
            for monster in allMonster:
                if beginHero.x==monster.x and beginHero.y==monster.y:
                    gameplay = 'Lost'
        if gameplay=='Lost':
            Display.blit(lost,(0,0))
            for e in events:
                if e.type==KEYDOWN:
                    if e.key == K_SPACE:
                        mapgame = 0
                        pick = 0.5
                        gameplay = 'Begin'
        elif gameplay=='Wait':
            print('roundMon1:%d'%roundMon)
            print('mapgame1:%d'%mapgame)
            if roundMon==maxRound:
                if mapgame==3:
                    Display.blit(wingame,(0,0)) #END
                    for e in events:
                        if e.type==KEYDOWN:
                            if e.key == K_SPACE:      
                                gameplay = 'End'
                else:
                    Display.blit(winmap,(0,0))
                    for e in events:
                        if e.type==KEYDOWN:
                            if e.key == K_SPACE:
                                mapgame+=1
                                for h in partyHero:
                                    h.hp = h.maxhp
                                gameplay = 'Begin'
                                roundMon = 1
            else:
                roundMon+=1
                gameplay = 'Begin'
            print('roundMon2:%d'%roundMon)
            print('mapgame2:%d'%mapgame)    
            print()
        elif gameplay=='Play':
            Display.blit(mapPic,(0,0))
            direction = beginHero.checkControlKey(events)
            if len(allDropHero)!=0:
                for d in allDropHero:
                    Display.blit(d.D1,(d.x,d.y))
            if len(allDropItem)!=0:
                for d in allDropItem:
                    Display.blit(d.item_img,(d.x,d.y))
            if time%2==0:
                moveParty(partyHero)
            hero.drawParty(Display,partyHero,'playparty',time)
            hero.drawParty(Display,allDropHero,'dropparty',time)
            hero.drawParty(Display,allDropItem,'dropitem',time)
            if time%3==0:
                for m in oneMonster:
                    moveParty(m)
                for m in partyMonster:
                    moveParty(m)
            monster.drawParty(Display,allMonster,time)
            hero.attack(partyHero,allMonster,allHero,allDropHero,allItem,allDropItem)
            monster.attack(partyHero,allMonster,allHero,time)
            monster.drawAtk(Display,allMonster)
            hero.drawAtk(Display,partyHero)
            for h in allDropHero:
                if h.x==beginHero.x and h.y==beginHero.y:
                    partyHero.append(h)
                    allDropHero.remove(h)
            for i in allDropItem:
                if i.x==beginHero.x and i.y==beginHero.y:
                    i.active(partyHero,allMonster,allDropItem)
                    allDropItem.remove(i)
            if potion.timeHeal>0 and potion.timeHeal<=3:
                potion.drawHeal(Display,partyHero)
            time+=1
        elif gameplay=='End':
            Display.blit(endcredit,(0,0))
    for e in events:
        if e.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    FPSclock.tick(FPS)