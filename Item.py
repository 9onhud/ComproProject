import pygame
class Potion:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.item_img = pygame.image.load('Potion.png')
        self.H1 = pygame.image.load("ItemHeal1.png")
        self.H2 = pygame.image.load("ItemHeal2.png")
        self.H3 = pygame.image.load("ItemHeal3.png")
        self.timeHeal = 10
    def active(self,partyHero,allMonster,allDropItem):
        for h in partyHero:
            h.hp+=(0.15*h.maxhp)
            if h.hp>h.maxhp:
                h.hp = h.maxhp
        self.timeHeal = 3
    def drawHeal(self,Display,partyHero):
        for h in partyHero:
            if self.timeHeal==3:
                Display.blit(self.H1,(h.x,h.y))
            elif self.timeHeal==2:
                Display.blit(self.H2,(h.x,h.y))
            elif self.timeHeal==1:
                Display.blit(self.H3,(h.x,h.y))
        self.timeHeal-=1