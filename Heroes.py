import pygame,sys,random,math
from pygame.locals import *
class Hero():
    def __init__(self,direction):
        self.direction = direction
        self.x = 400
        self.y = 300
        self.cdatk = 0
        self.drawatk = 0
        self.countRangeAtk = 10
    def checkControlKey(self,events):
        for e in events:
            if e.type==KEYDOWN:
                if self.direction != 'right' and (e.key == K_a or e.key == K_LEFT) :
                    self.direction = 'left'
                elif self.direction != 'left' and (e.key == K_d or e.key == K_RIGHT) :
                    self.direction = 'right'
                elif self.direction != 'down' and (e.key == K_w or e.key == K_UP) :
                    self.direction = 'up'
                elif self.direction != 'up' and (e.key == K_s or e.key == K_DOWN) :
                    self.direction = 'down'
        return self.direction
    def move(self):
        if self.direction == 'left' :
            self.x -= 32
        elif self.direction == 'right' :
            self.x += 32
        elif self.direction == 'up' :
            self.y -= 32
        elif self.direction == 'down' :
            self.y += 32
        return (self.x,self.y)
    def drawParty(self,Display,party,typeLs,time):
        if typeLs=='playparty':
            lshero = []
            if party[0].direction=='down':
                for i in range(len(party)-1,-1,-1):
                    lshero.append(party[i])
            else:
                lshero = party
            for member in lshero:
                if time%8 in [0,1,4,5]:
                    if member.direction == 'down':
                        Display.blit(member.D1, (member.x,member.y))
                    if member.direction == 'up':
                        Display.blit(member.U1, (member.x,member.y)) 
                    if member.direction == 'left':
                        Display.blit(member.L1, (member.x,member.y))                        
                    if member.direction == 'right':
                        Display.blit(member.R1, (member.x,member.y))
                elif time%8 in [2,3]:
                    if member.direction == 'down':
                        Display.blit(member.D2, (member.x,member.y))
                    if member.direction == 'up':
                        Display.blit(member.U2, (member.x,member.y)) 
                    if member.direction == 'left':
                        Display.blit(member.L2, (member.x,member.y))                        
                    if member.direction == 'right':
                        Display.blit(member.R2, (member.x,member.y))
                else:
                    if member.direction == 'down':
                        Display.blit(member.D3, (member.x,member.y))
                    if member.direction == 'up':
                        Display.blit(member.U3, (member.x,member.y)) 
                    if member.direction == 'left':
                        Display.blit(member.L3, (member.x,member.y))                        
                    if member.direction == 'right':
                        Display.blit(member.R3, (member.x,member.y))
            self.drawHP(party,Display)
        elif typeLs=='dropparty':
            for d in party:
                Display.blit(d.D1,(d.x,d.y))
        elif typeLs=='dropitem':
            for d in party:
                Display.blit(d.item_img,(d.x,d.y))
    def drawHP(self,party,Display):
        for i in range(len(party)):
            pygame.draw.rect(Display,(0,255,0),(72,30+100*(i+1),((100*party[i].hp)/party[i].maxhp)/100*77,15))
            Display.blit(party[i].hpGauge, (10,100*(i+1)))
    def drawAtk(self,Display,partyHero):
        for h in partyHero:
            if h.drawatk>0:
                if h.typeAtk=='melee':
                    if h.drawatk==4:
                        Display.blit(h.A1,(h.x-16,h.y-16))
                    elif h.drawatk==3:
                        Display.blit(h.A2,(h.x-16,h.y-16))
                    elif h.drawatk==2:
                        Display.blit(h.A3,(h.x-16,h.y-16))
                    else:
                        Display.blit(h.A4,(h.x-16,h.y-16))
                elif h.typeAtk=='AOE':
                    if h.drawatk==6:
                        h.pic = pygame.transform.rotate(h.A1,h.degree)
                        Display.blit(h.pic,(h.x+(h.targetX-h.x)*(1/3),h.y+(h.targetY-h.y)*(1/3)))
                    elif h.drawatk==5:
                        h.pic = pygame.transform.rotate(h.A2,h.degree)
                        Display.blit(h.pic,(h.x+(h.targetX-h.x)*(2/3),h.y+(h.targetY-h.y)*(2/3)))
                    elif h.drawatk==4:
                        h.pic = pygame.transform.rotate(h.A3,h.degree)
                        Display.blit(h.pic,(h.x+(h.targetX-h.x),h.y+(h.targetY-h.y)))
                    elif h.drawatk==3:
                        h.pic = pygame.transform.rotate(h.A4,h.degree)
                        Display.blit(h.pic,(h.x+(h.targetX-h.x),h.y+(h.targetY-h.y)))                         
                    elif h.drawatk==2:
                        h.pic = pygame.transform.rotate(h.A5,h.degree)
                        Display.blit(h.pic,(h.x+(h.targetX-h.x),h.y+(h.targetY-h.y)))
                    elif h.drawatk==1:
                        h.pic = pygame.transform.rotate(h.A6,h.degree)
                        Display.blit(h.pic,(h.x+(h.targetX-h.x),h.y+(h.targetY-h.y)))
                elif h.typeAtk=='Range':
                    if h.drawatk==4:
                        h.pic = pygame.transform.rotate(h.A1,h.degree)
                        Display.blit(h.pic,(h.x+(h.targetX-h.x)*(1/4),h.y+(h.targetY-h.y)*(1/4)))  
                    elif h.drawatk==3:
                        h.pic = pygame.transform.rotate(h.A1,h.degree)
                        Display.blit(h.pic,(h.x+(h.targetX-h.x)*(2/4),h.y+(h.targetY-h.y)*(2/4)))  
                    elif h.drawatk==2:
                        h.pic = pygame.transform.rotate(h.A1,h.degree)
                        Display.blit(h.pic,(h.x+(h.targetX-h.x)*(3/4),h.y+(h.targetY-h.y)*(3/4)))    
                    elif h.drawatk==1:
                        h.pic = pygame.transform.rotate(h.A1,h.degree)
                        Display.blit(h.pic,(h.x+(h.targetX-h.x),h.y+(h.targetY-h.y)))  
                elif h.typeAtk=='RangeHeal':
                    if h.drawatk==6:
                        h.pic = pygame.transform.rotate(h.A1,h.degree)
                        Display.blit(h.pic,(h.x+(h.targetX-h.x)*(1/3),h.y+(h.targetY-h.y)*(1/3)))  
                    elif h.drawatk==5:
                        h.pic = pygame.transform.rotate(h.A1,h.degree)
                        Display.blit(h.pic,(h.x+(h.targetX-h.x)*(2/3),h.y+(h.targetY-h.y)*(2/3)))    
                    elif h.drawatk==4:
                        h.pic = pygame.transform.rotate(h.A1,h.degree)
                        Display.blit(h.pic,(h.x+(h.targetX-h.x),h.y+(h.targetY-h.y)))
                    elif h.drawatk==3:
                        Display.blit(h.H1,(h.Heal[0].x,h.Heal[0].y))
                    elif h.drawatk==2:
                        Display.blit(h.H2,(h.Heal[0].x,h.Heal[0].y))                   
                    elif h.drawatk==1:
                        Display.blit(h.H3,(h.Heal[0].x,h.Heal[0].y))
                        h.Heal = []
                h.drawatk-=1
    def attack(self,partyHero,allMonster,allHero,allDropHero,allItem,allDropItem):
        for h in partyHero:
            if h.cdatk>=h.asp:
                h.selfAttack(allMonster)
                h.cdatk = 0
            h.cdatk+=1
            h.countRangeAtk+=1
            if h.typeAtk=='AOE' and h.countRangeAtk==3:
                for m in allMonster:
                    if (m.x in range(h.targetX-32*3,h.targetX+32*3)) and (m.y in range(h.targetY-32*3,h.targetY+32*3)):
                        m.hp-=h.dm
            elif h.typeAtk=='Range' and h.countRangeAtk<=4:
                if h.countRangeAtk==1:
                    h.weaponX = h.x+(h.targetX-h.x)*(1/4)
                    h.weaponY = h.y+(h.targetY-h.y)*(1/4)
                elif h.countRangeAtk==2:
                    h.weaponX = h.x+(h.targetX-h.x)*(2/4)
                    h.weaponY = h.y+(h.targetY-h.y)*(2/4)
                elif h.countRangeAtk==3:
                    h.weaponX = h.x+(h.targetX-h.x)*(3/4)
                    h.weaponY = h.y+(h.targetY-h.y)*(3/4)
                else:
                    h.weaponX = h.x+(h.targetX-h.x)
                    h.weaponY = h.y+(h.targetY-h.y)
                for m in allMonster:
                    if (h.weaponX in range(m.x,m.x+32)) and (h.weaponY in range(m.y,m.y+32)):
                        m.hp-=h.dm
                        h.countRangeAtk = 10
            elif h.typeAtk=='RangeHeal' and h.countRangeAtk<=3:
                h.Heal.append(random.choice(partyHero))
                if h.countRangeAtk==1:
                    h.weaponX = h.x+(h.targetX-h.x)*(1/3)
                    h.weaponY = h.y+(h.targetY-h.y)*(1/3)
                elif h.countRangeAtk==2:
                    h.weaponX = h.x+(h.targetX-h.x)*(2/3)
                    h.weaponY = h.y+(h.targetY-h.y)*(2/3)
                else:
                    h.weaponX = h.x+(h.targetX-h.x)
                    h.weaponY = h.y+(h.targetY-h.y)
                for m in allMonster:
                    if (h.weaponX in range(m.x,m.x+32)) and (h.weaponY in range(m.y,m.y+32)):
                        m.hp-=h.dm
                        h.countRangeAtk = 10
                        for hh in h.Heal:
                            hh.hp+=(0.075*hh.maxhp)
                            if hh.hp>hh.maxhp:
                                hh.hp = hh.maxhp
        for m in allMonster:
            if m.hp<=0:
                allMonster.remove(m)
                self.drop_Hero(allHero,allDropHero,allItem,allDropItem,m.x,m.y)

    def drop_Hero(self,allHero,allDropHero,allItem,allDropItem,x,y):
        drop = random.choice(['DropHero','DropItem','NoDrop','NoDrop','NoDrop','NoDrop','NoDrop','NoDrop'])
        if drop=='DropHero':
            while len(allHero)!=0:
                heroDrop = random.choice(allHero)
                heroDrop.x,heroDrop.y = x,y
                allDropHero.append(heroDrop)
                allHero.remove(heroDrop)
                break
        elif drop=='DropItem':
            itemDrop = random.choice(allItem)
            itemDrop.x,itemDrop.y = x,y
            allDropItem.append(itemDrop)
            
            
                
    def calDegree(self,h):
        dx = h.targetX-h.x
        dy = h.targetY-h.y
        if dx > 0:
            if dy > 0:
                h.degree = -(90+90-math.fabs(math.degrees(math.atan(dy/dx))))
            elif dy < 0:
                h.degree = -(90-math.fabs(math.degrees(math.atan(dy/dx))))
            else:
                h.degree = -90
        elif dx < 0:
            if dy > 0:
                h.degree = (90+90-math.fabs(math.degrees(math.atan(dy/dx))))
            elif dy < 0:
                h.degree = (90-math.fabs(math.degrees(math.atan(dy/dx))))
            else:
                h.degree = 90
        else:
            if dy > 0:
                h.degree = 180
            if dy < 0:
                h.degree = 0
                    
class Warrior(Hero):
    def __init__(self,direction):
        Hero.__init__(self,direction)
        self.x = random.choice(range(352,600,32))
        self.y = random.choice(range(192,400,32))
        self.maxhp = 30
        self.hp = self.maxhp
        self.dm = 9
        self.Range = 1
        self.asp = 10
        self.typeAtk = 'melee'
        self.D1 = pygame.image.load("Warrior_D1.png")
        self.D2 = pygame.image.load("Warrior_D2.png")
        self.D3 = pygame.image.load("Warrior_D3.png")
        self.L1 = pygame.image.load("Warrior_L1.png")
        self.L2 = pygame.image.load("Warrior_L2.png")
        self.L3 = pygame.image.load("Warrior_L3.png")
        self.R1 = pygame.image.load("Warrior_R1.png")
        self.R2 = pygame.image.load("Warrior_R2.png")
        self.R3 = pygame.image.load("Warrior_R3.png")
        self.U1 = pygame.image.load("Warrior_U1.png")
        self.U2 = pygame.image.load("Warrior_U2.png")
        self.U3 = pygame.image.load("Warrior_U3.png")
        self.A1 = pygame.image.load("WarA1.png")
        self.A2 = pygame.image.load("WarA2.png")
        self.A3 = pygame.image.load("WarA3.png")
        self.A4 = pygame.image.load("WarA4.png")
        self.hpGauge = pygame.image.load("HP_War.png")
    def selfAttack(self,allMonster):
        for m in allMonster:
            if math.sqrt((self.x-m.x)**2+(self.y-m.y)**2)<=32:
                m.hp-=self.dm
                self.drawatk = 4
class Mage(Hero):
    def __init__(self,direction):
        Hero.__init__(self,direction)
        self.x = random.choice(range(352,600,32))
        self.y = random.choice(range(192,400,32))
        self.maxhp = 22
        self.hp = self.maxhp
        self.dm = 5
        self.Range = 3
        self.asp = 10
        self.typeAtk = 'AOE'
        self.D1 = pygame.image.load("Mage_D1.png")
        self.D2 = pygame.image.load("Mage_D2.png")
        self.D3 = pygame.image.load("Mage_D3.png")
        self.L1 = pygame.image.load("Mage_L1.png")
        self.L2 = pygame.image.load("Mage_L2.png")
        self.L3 = pygame.image.load("Mage_L3.png")
        self.R1 = pygame.image.load("Mage_R1.png")
        self.R2 = pygame.image.load("Mage_R2.png")
        self.R3 = pygame.image.load("Mage_R3.png")
        self.U1 = pygame.image.load("Mage_U1.png")
        self.U2 = pygame.image.load("Mage_U2.png")
        self.U3 = pygame.image.load("Mage_U3.png")
        self.A1 = pygame.image.load("MagA1.png")
        self.A2 = pygame.image.load("MagA2.png")
        self.A3 = pygame.image.load("MagA3.png")
        self.A4 = pygame.image.load("MagA4.png")
        self.A5 = pygame.image.load("MagA5.png")
        self.A6 = pygame.image.load("MagA6.png")
        self.hpGauge = pygame.image.load("HP_Mag.png")
    def selfAttack(self,allMonster):
        ls = []
        for m in allMonster:
            ls.append(math.sqrt((self.x-m.x)**2+(self.y-m.y)**2))
        if min(ls)<=32*self.Range:
            for i in range(len(ls)):
                if ls[i] == min(ls):
                    self.targetX = allMonster[i].x
                    self.targetY = allMonster[i].y
                    self.calDegree(self)
            self.countRangeAtk = 0
            self.drawatk = 6        
class Archer(Hero):
    def __init__(self,direction):
        Hero.__init__(self,direction)
        self.x = random.choice(range(352,600,32))
        self.y = random.choice(range(192,400,32))
        self.maxhp = 20
        self.hp = self.maxhp
        self.dm = 8
        self.Range = 4
        self.asp = 8
        self.typeAtk = 'Range'
        self.D1 = pygame.image.load("Archer_D1.png")
        self.D2 = pygame.image.load("Archer_D2.png")
        self.D3 = pygame.image.load("Archer_D3.png")
        self.L1 = pygame.image.load("Archer_L1.png")
        self.L2 = pygame.image.load("Archer_L2.png")
        self.L3 = pygame.image.load("Archer_L3.png")
        self.R1 = pygame.image.load("Archer_R1.png")
        self.R2 = pygame.image.load("Archer_R2.png")
        self.R3 = pygame.image.load("Archer_R3.png")
        self.U1 = pygame.image.load("Archer_U1.png")
        self.U2 = pygame.image.load("Archer_U2.png")
        self.U3 = pygame.image.load("Archer_U3.png")
        self.A1 = pygame.image.load("ArcA1.png")
        self.hpGauge = pygame.image.load("HP_Arc.png")
    def selfAttack(self,allMonster):
        ls = []
        for m in allMonster:
            ls.append(math.sqrt((self.x-m.x)**2+(self.y-m.y)**2))
        if min(ls)<=32*self.Range:
            for i in range(len(ls)):
                if ls[i] == min(ls):
                    self.targetX = allMonster[i].x
                    self.targetY = allMonster[i].y
                    self.calDegree(self)
            self.countRangeAtk = 0
            self.drawatk = 4
    
class Priest(Hero):
    def __init__(self,direction):
        Hero.__init__(self,direction)
        self.x = random.choice(range(352,600,32))
        self.y = random.choice(range(192,400,32))
        self.maxhp = 25
        self.hp = self.maxhp
        self.dm = 4
        self.Range = 3
        self.asp = 15
        self.Heal = []
        self.typeAtk = 'RangeHeal'
        self.D1 = pygame.image.load("Priest_D1.png")
        self.D2 = pygame.image.load("Priest_D2.png")
        self.D3 = pygame.image.load("Priest_D3.png")
        self.L1 = pygame.image.load("Priest_L1.png")
        self.L2 = pygame.image.load("Priest_L2.png")
        self.L3 = pygame.image.load("Priest_L3.png")
        self.R1 = pygame.image.load("Priest_R1.png")
        self.R2 = pygame.image.load("Priest_R2.png")
        self.R3 = pygame.image.load("Priest_R3.png")
        self.U1 = pygame.image.load("Priest_U1.png")
        self.U2 = pygame.image.load("Priest_U2.png")
        self.U3 = pygame.image.load("Priest_U3.png")
        self.A1 = pygame.image.load("PriA1.png")
        self.H1 = pygame.image.load("HeroHeal1.png")
        self.H2 = pygame.image.load("HeroHeal2.png")
        self.H3 = pygame.image.load("HeroHeal3.png")
        self.hpGauge = pygame.image.load("HP_Pri.png")
    def selfAttack(self,allMonster):
        ls = []
        for m in allMonster:
            ls.append(math.sqrt((self.x-m.x)**2+(self.y-m.y)**2))
        if min(ls)<=32*self.Range:
            for i in range(len(ls)):
                if ls[i] == min(ls):
                    self.targetX = allMonster[i].x
                    self.targetY = allMonster[i].y
                    self.calDegree(self)
            self.countRangeAtk = 0
            self.drawatk = 6