import pygame

class Sprite(pygame.sprite.Sprite):
    def __init__(self, bounds, name, leftImg, rightImg, anim, size, time):
        super().__init__()
        self.xCoord = bounds[0]
        self.yCoord = bounds[1]
        self.name = name
        self.images = rightImg
        self.rightImg = rightImg
        self.leftImg = leftImg
        self.index = 0
        self.size = size
        self.image = rightImg[self.index]
        self.rect = pygame.Rect(bounds, (size, size))
        self.rect.center = [self.xCoord, self.yCoord]
        self.size = size
        self.framesAnim = anim
        self.framesCurr = 0
        self.timeUntil = time
        self.actions = []
        self.active = True
        return
    
    def insert_action(self, action):
        action.entity_state = self
        self.actions.append(action)
        return
    
    def move_left(self, pix):
        self.images = self.leftImg
        self.update()
        self.rect.move_ip(-pix, 0)
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > 1152-pix:
            self.rect.x = 1152-pix
        return

    def move_right(self, pix):
        self.images = self.rightImg
        self.update()
        self.rect.move_ip(pix, 0)
        if self.rect.x > 1152-pix:
            self.rect.x = 1152-pix
        if self.rect.x < 0:
            self.rect.x = 0
        return
    
    def move_down(self, pix):
        self.update()
        self.rect.move_ip(0, pix)
        return
    
    def deactivate(self):
        self.active = False
    
    def update(self):
        self.framesCurr += 1/10 
        if self.framesCurr >= self.framesAnim:
            self.framesCurr = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]
