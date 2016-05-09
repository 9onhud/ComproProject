import pygame,sys,random,math
from pygame.locals import *
class Monster():
    def __init__(self):
        self.countTime = 0
        self.timeatk = 0
        self.drawatk = 0
        self.cdatk = 0
        self.countRangeAtk = 10
        self.beforedirec = 'Stop'
        self.movestatus = 'Run'
    def move(self):
        if self.movestatus=='Run':
            if (self.direction=='left')and(self.x<224)and(self.y<64):
                self.direction = 'down'
                self.y += 32
                self.countTime-=35
                if self.countTime<0:
                    self.countTime = 0
            elif (self.direction=='left')and(self.x<224)and(self.y>503):
                self.direction = 'up'
                self.y -= 32
                self.countTime-=35
                if self.countTime<0:
                    self.countTime = 0            
            elif (self.direction=='left')and(self.x<224):
                self.direction = random.choice(['up','down'])
                if self.direction == 'up':
                    self.y -= 32
                else:
                    self.y += 32
                self.countTime-=35
                if self.countTime<0:
                    self.countTime = 0
            elif (self.direction=='left'):
                self.x -= 32
                if self.countTime>50:
                    if self.y<64:
                        self.direction = 'down'
                    elif self.y>503:
                        self.direction = 'up'
                    else:
                        self.direction = random.choice(['up','down'])
                    self.countTime-=50
            elif (self.direction=='right')and(self.x>718)and(self.y<64):
                self.direction = 'down'
                self.y += 32
                self.countTime-=35
                if self.countTime<0:
                    self.countTime = 0            
            elif (self.direction=='right')and(self.x>718)and(self.y>503):
                self.direction = 'up'
                self.y -= 32
                self.countTime-=35
                if self.countTime<0:
                    self.countTime = 0            
            elif (self.direction=='right')and(self.x>718):
                self.direction = random.choice(['up','down'])
                if self.direction == 'up':
                    self.y -= 32            
                else:
                    self.y += 32
                self.countTime-=35
                if self.countTime<0:
                    self.countTime = 0                
            elif (self.direction=='right'):
                self.x += 32
                if self.countTime>50:
                    if self.y<64:
                        self.direction = 'down'
                    elif self.y>503:
                        self.direction = 'up'
                    else:
                        self.direction = random.choice(['up','down'])           
                    self.countTime-=50            
            elif (self.direction=='up')and(self.x<224)and(self.y<64):
                self.direction = 'right'
                self.x += 32
                self.countTime-=35
                if self.countTime<0:
                    self.countTime = 0            
            elif (self.direction=='up')and(self.x>718)and(self.y<64):
                self.direction = 'left'
                self.x -= 32
                self.countTime-=35
                if self.countTime<0:
                    self.countTime = 0            
            elif (self.direction=='up')and(self.y<64):
                self.direction = random.choice(['left','right'])
                if self.direction == 'left':
                    self.x -= 32          
                else:
                    self.x += 32
                self.countTime-=35
                if self.countTime<0:
                    self.countTime = 0                
            elif (self.direction=='up'):
                self.y -= 32
                if self.countTime>50:
                    if self.x<224:
                        self.direction = 'right'
                    elif self.x>718:
                        self.direction = 'left'
                    else:
                        self.direction = random.choice(['left','right'])       
                    self.countTime-=50            
            elif (self.direction=='down')and(self.x<224)and(self.y>503):
                self.direction = 'right'
                self.x += 32
                self.countTime-=35
                if self.countTime<0:
                    self.countTime = 0            
            elif (self.direction=='down')and(self.x>718)and(self.y>503):
                self.direction = 'left'
                self.x -= 32
                self.countTime-=35
                if self.countTime<0:
                    self.countTime = 0            
            elif (self.direction=='down')and(self.y>503):
                self.direction = random.choice(['left','right'])
                if self.direction == 'left':
                    self.x -= 32         
                else:
                    self.x += 32
                self.countTime-=35
                if self.countTime<0:
                    self.countTime = 0                
            elif (self.direction=='down'):
                self.y += 32
                if self.countTime>50:
                    if self.x<224:
                        self.direction = 'right'
                    elif self.x>718:
                        self.direction = 'left'
                    else:
                        self.direction = random.choice(['left','right'])            
                    self.countTime-=50
            self.countTime+=3
        return (self.x,self.y)
    def drawParty(self,Display,party,time):
        lsmon = []
        if party[0].direction=='down':
            for i in range(len(party)-1,-1,-1):
                lsmon.append(party[i])
        else:
            lsmon = party        
        for member in party:
            if time%12 in [0,1,2,6,7,8]:
                if member.direction == 'down':
                    Display.blit(member.D1, (member.x,member.y))
                if member.direction == 'up':
                    Display.blit(member.U1, (member.x,member.y)) 
                if member.direction == 'left':
                    Display.blit(member.L1, (member.x,member.y))                        
                if member.direction == 'right':
                    Display.blit(member.R1, (member.x,member.y))
            elif time%12 in [3,4,5]:
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
    def drawAtk(self,Display,allMonster):
        for m in allMonster:
            if m.drawatk>0:
                if m.typeAtk=='Melee':
                    if m.drawatk==3:
                        Display.blit(m.A1,(m.x-16,m.y-16))
                    if m.drawatk==2:
                        Display.blit(m.A2,(m.x-16,m.y-16))
                    if m.drawatk==1:
                        Display.blit(m.A3,(m.x-16,m.y-16))
                elif m.typeAtk=='AOE':
                    if m.drawatk==6:
                        m.pic = pygame.transform.rotate(m.A1,m.degree)
                        Display.blit(m.pic,(m.x+(m.targetX-m.x)*(1/3),m.y+(m.targetY-m.y)*(1/3)))
                    if m.drawatk==5:
                        m.pic = pygame.transform.rotate(m.A2,m.degree)
                        Display.blit(m.pic,(m.x+(m.targetX-m.x)*(2/3),m.y+(m.targetY-m.y)*(2/3)))
                    if m.drawatk==4:
                        m.pic = pygame.transform.rotate(m.A3,m.degree)
                        Display.blit(m.pic,(m.x+(m.targetX-m.x),m.y+(m.targetY-m.y)))
                    if m.drawatk==3:
                        m.pic = pygame.transform.rotate(m.A4,m.degree)
                        Display.blit(m.pic,(m.x+(m.targetX-m.x),m.y+(m.targetY-m.y)))
                    if m.drawatk==2:
                        m.pic = pygame.transform.rotate(m.A5,m.degree)
                        Display.blit(m.pic,(m.x+(m.targetX-m.x),m.y+(m.targetY-m.y)))
                    if m.drawatk==1:
                        m.pic = pygame.transform.rotate(m.A6,m.degree)
                        Display.blit(m.pic,(m.x+(m.targetX-m.x),m.y+(m.targetY-m.y)))
                elif m.typeAtk=='Range':
                    if m.drawatk==4:
                        m.pic = pygame.transform.rotate(m.A1,m.degree)
                        Display.blit(m.pic,(m.x+(m.targetX-m.x)*(1/4),m.y+(m.targetY-m.y)*(1/4)))  
                    elif m.drawatk==3:
                        m.pic = pygame.transform.rotate(m.A2,m.degree)
                        Display.blit(m.pic,(m.x+(m.targetX-m.x)*(2/4),m.y+(m.targetY-m.y)*(2/4)))  
                    elif m.drawatk==2:
                        m.pic = pygame.transform.rotate(m.A3,m.degree)
                        Display.blit(m.pic,(m.x+(m.targetX-m.x)*(3/4),m.y+(m.targetY-m.y)*(3/4)))    
                    elif m.drawatk==1:
                        m.pic = pygame.transform.rotate(m.A4,m.degree)
                        Display.blit(m.pic,(m.x+(m.targetX-m.x),m.y+(m.targetY-m.y)))                     
                m.drawatk-=1
    def attack(self,partyHero,allMonster,allHero,time):
        for m in allMonster:
            if m.cdatk>=m.asp:
                m.selfAttack(partyHero)
                m.cdatk = 0
            m.cdatk+=1
            m.countRangeAtk+=1
            if m.typeAtk=='AOE' and m.countRangeAtk==3:
                for h in partyHero:
                    if (h.x in range(m.targetX-32*3,m.targetX+32*3)) and (h.y in range(m.targetY-32*3,m.targetY+32*3)):
                        h.hp-=m.dm
            elif m.typeAtk=='Range' and m.countRangeAtk<=4:
                if m.countRangeAtk==1:
                    m.weaponX = m.x+(m.targetX-m.x)*(1/4)
                    m.weaponY = m.y+(m.targetY-m.y)*(1/4)
                elif m.countRangeAtk==2:
                    m.weaponX = m.x+(m.targetX-m.x)*(2/4)
                    m.weaponY = m.y+(m.targetY-m.y)*(2/4)
                elif m.countRangeAtk==3:
                    m.weaponX = m.x+(m.targetX-m.x)*(3/4)
                    m.weaponY = m.y+(m.targetY-m.y)*(3/4)
                else:
                    m.weaponX = m.x+(m.targetX-m.x)
                    m.weaponY = m.y+(m.targetY-m.y)
                for h in partyHero:
                    if (m.weaponX in range(h.x,h.x+32)) and (m.weaponY in range(h.y,h.y+32)):
                        h.hp-=m.dm
                        m.countRangeAtk = 10
        for h in partyHero:
            if h.hp<=0:
                partyHero.remove(h)
            if time>25:
                for m in allMonster:
                    if h.x==m.x and h.y==m.y:
                        partyHero.remove(h)
                        h.hp = h.maxhp
                        allHero.append(h)
    def calDegree(self,m):
        dx = m.targetX-m.x
        dy = m.targetY-m.y
        if dx > 0:
            if dy > 0:
                m.degree = -(90+90-math.fabs(math.degrees(math.atan(dy/dx))))
            elif dy < 0:
                m.degree = -(90-math.fabs(math.degrees(math.atan(dy/dx))))
            else:
                m.degree = -90
        elif dx < 0:
            if dy > 0:
                m.degree = (90+90-math.fabs(math.degrees(math.atan(dy/dx))))
            elif dy < 0:
                m.degree = (90-math.fabs(math.degrees(math.atan(dy/dx))))
            else:
                m.degree = 90
        else:
            if dy > 0:
                m.degree = 180
            if dy < 0:
                m.degree = 0        
                
class Bat(Monster):
    def __init__(self,x,y):
        Monster.__init__(self)
        self.x = x
        self.y = y
        self.hp = 12
        self.dm = 3
        self.Range = 1
        self.asp = 14
        self.typeAtk = 'Melee'
        self.direction = 'right'
        self.D1 = pygame.image.load("Bat_D1.png")
        self.D2 = pygame.image.load("Bat_D2.png")
        self.D3 = pygame.image.load("Bat_D3.png")
        self.L1 = pygame.image.load("Bat_L1.png")
        self.L2 = pygame.image.load("Bat_L2.png")
        self.L3 = pygame.image.load("Bat_L3.png")
        self.R1 = pygame.image.load("Bat_R1.png")
        self.R2 = pygame.image.load("Bat_R2.png")
        self.R3 = pygame.image.load("Bat_R3.png")
        self.U1 = pygame.image.load("Bat_U1.png")
        self.U2 = pygame.image.load("Bat_U2.png")
        self.U3 = pygame.image.load("Bat_U3.png")
        self.A1 = pygame.image.load("BatA1.png")
        self.A2 = pygame.image.load("BatA2.png")
        self.A3 = pygame.image.load("BatA3.png")
        self.A4 = pygame.image.load("BatA4.png")
    def selfAttack(self,partyHero):
        for h in partyHero:
            if math.sqrt((self.x-h.x)**2+(self.y-h.y)**2)<=32:
                h.hp-=self.dm
                self.drawatk = 4    
class Godzilla(Monster):
    def __init__(self,x,y):
        Monster.__init__(self)
        self.x = x
        self.y = y
        self.hp = 15
        self.dm = 1.5
        self.Range = 3
        self.asp = 12
        self.typeAtk = 'AOE'
        self.direction = 'right'
        self.D1 = pygame.image.load("Goz_D1.png")
        self.D2 = pygame.image.load("Goz_D2.png")
        self.D3 = pygame.image.load("Goz_D3.png")
        self.L1 = pygame.image.load("Goz_L1.png")
        self.L2 = pygame.image.load("Goz_L2.png")
        self.L3 = pygame.image.load("Goz_L3.png")
        self.R1 = pygame.image.load("Goz_R1.png")
        self.R2 = pygame.image.load("Goz_R2.png")
        self.R3 = pygame.image.load("Goz_R3.png")
        self.U1 = pygame.image.load("Goz_U1.png")
        self.U2 = pygame.image.load("Goz_U2.png")
        self.U3 = pygame.image.load("Goz_U3.png")
        self.A1 = pygame.image.load("GozA1.png")
        self.A2 = pygame.image.load("GozA2.png")
        self.A3 = pygame.image.load("GozA3.png")
        self.A4 = pygame.image.load("GozA4.png")
        self.A5 = pygame.image.load("GozA5.png")
        self.A6 = pygame.image.load("GozA6.png")
    def selfAttack(self,partyHero):
        ls = []
        for h in partyHero:
            ls.append(math.sqrt((self.x-h.x)**2+(self.y-h.y)**2))
        if min(ls)<=32*self.Range:
            for i in range(len(ls)):
                if ls[i] == min(ls):
                    self.targetX = partyHero[i].x
                    self.targetY = partyHero[i].y
                    self.calDegree(self)
            self.countRangeAtk = 0
            self.drawatk = 6    
class Imp(Monster):
    def __init__(self,x,y):
        Monster.__init__(self)
        self.x = x
        self.y = y
        self.hp = 17
        self.dm = 2
        self.Range = 3
        self.asp = 10
        self.typeAtk = 'AOE'
        self.direction = 'right'
        self.D1 = pygame.image.load("Imp_D1.png")
        self.D2 = pygame.image.load("Imp_D2.png")
        self.D3 = pygame.image.load("Imp_D3.png")
        self.L1 = pygame.image.load("Imp_L1.png")
        self.L2 = pygame.image.load("Imp_L2.png")
        self.L3 = pygame.image.load("Imp_L3.png")
        self.R1 = pygame.image.load("Imp_R1.png")
        self.R2 = pygame.image.load("Imp_R2.png")
        self.R3 = pygame.image.load("Imp_R3.png")
        self.U1 = pygame.image.load("Imp_U1.png")
        self.U2 = pygame.image.load("Imp_U2.png")
        self.U3 = pygame.image.load("Imp_U3.png")
        self.A1 = pygame.image.load("ImpA1.png")
        self.A2 = pygame.image.load("ImpA1.png")
        self.A3 = pygame.image.load("ImpA1.png")
        self.A4 = pygame.image.load("ImpA2.png")
        self.A5 = pygame.image.load("ImpA3.png")
        self.A6 = pygame.image.load("ImpA4.png")
    def selfAttack(self,partyHero):
        ls = []
        for h in partyHero:
            ls.append(math.sqrt((self.x-h.x)**2+(self.y-h.y)**2))
        if min(ls)<=32*self.Range:
            for i in range(len(ls)):
                if ls[i] == min(ls):
                    self.targetX = partyHero[i].x
                    self.targetY = partyHero[i].y
                    self.calDegree(self)
            self.countRangeAtk = 0
            self.drawatk = 6
class Goblin(Monster):
    def __init__(self,x,y):
        Monster.__init__(self)
        self.x = x
        self.y = y
        self.hp = 15
        self.dm = 8
        self.Range = 4
        self.asp = 8
        self.typeAtk = 'Range'
        self.direction = 'right'
        self.D1 = pygame.image.load("Gob_D1.png")
        self.D2 = pygame.image.load("Gob_D2.png")
        self.D3 = pygame.image.load("Gob_D3.png")
        self.L1 = pygame.image.load("Gob_L1.png")
        self.L2 = pygame.image.load("Gob_L2.png")
        self.L3 = pygame.image.load("Gob_L3.png")
        self.R1 = pygame.image.load("Gob_R1.png")
        self.R2 = pygame.image.load("Gob_R2.png")
        self.R3 = pygame.image.load("Gob_R3.png")
        self.U1 = pygame.image.load("Gob_U1.png")
        self.U2 = pygame.image.load("Gob_U2.png")
        self.U3 = pygame.image.load("Gob_U3.png")
        self.A1 = pygame.image.load("GobA1.png")
        self.A2 = pygame.image.load("GobA2.png")
        self.A3 = pygame.image.load("GobA3.png")
        self.A4 = pygame.image.load("GobA4.png")
    def selfAttack(self,partyHero):
        ls = []
        for h in partyHero:
            ls.append(math.sqrt((self.x-h.x)**2+(self.y-h.y)**2))
        if min(ls)<=32*self.Range:
            for i in range(len(ls)):
                if ls[i] == min(ls):
                    self.targetX = partyHero[i].x
                    self.targetY = partyHero[i].y
                    self.calDegree(self)
            self.countRangeAtk = 0
            self.drawatk = 4