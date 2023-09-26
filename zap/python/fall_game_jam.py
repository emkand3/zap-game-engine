import sys
sys.path.append("/Users/emma/Desktop/coding/cpsc4160")
import pygame
import random

import zap.engine.play.action.displayAction as ds
import zap.engine.play.action.terminate as tm
import zap.engine.play.entity.frameViewer as fv
import zap.engine.play.entity.gameLoop as gl 

import zap.engine.ui.entity.background as bkgd
import zap.engine.ui.action.drawBackground as drawbkdg

import zap.engine.ui.entity.sprite as sp
import zap.engine.ui.action.drawSprite as drawS
import zap.engine.ui.action.moveSprite as moveS

import zap.engine.ui.entity.hud as hud
import zap.engine.ui.action.drawHud as dh

import zap.engine.utility.entity.counter as ctr
import zap.engine.utility.action.counterIncrement as ci

pygame.init()
FPS = 6

class UpdateLeaf:
    def __init__(self, sprite, screen):
        self.acting = True
        self.collect = pygame.mixer.Sound("zap/assets/collect.wav")
        self.sprite = sprite
        self.screen = screen.screen
        self.name = "update_leaf_action"
        self.types = ["loop"]
        self.entity_state = None
        self.children = []
        self.verbose = False
        return
    
    def condition_to_act(self):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        return True
    
    def act(self):
        if self.condition_to_act():
            self.gravity()

    def gravity(self):
        if self.acting:
            self.entity_state.move_down(1)
            if self.check_collision():
                pygame.mixer.Sound.play(self.collect)
                self.children[2].act()
                self.generate_new_leaf()
            elif self.entity_state.rect.y > 520:
               self.generate_new_leaf()
    
    def check_collision(self):
        collision = pygame.sprite.collide_rect(self.entity_state, self.sprite)
        return collision

    def generate_new_leaf(self):
        self.acting = False
        #self.entity_state.active = False
        self.entity_state.xCoord = random.randrange(50, 1270)
        self.entity_state.yCoord = 10
        self.entity_state.bounds = (self.entity_state.xCoord, self.entity_state.yCoord)
        size = self.entity_state.size
        self.entity_state.rect = pygame.Rect(self.entity_state.bounds, (size, size))
        self.entity_state.active = True
        self.children[0].act(self.screen)
        self.children[1].act()
        self.entity_state.update()
        self.acting = True

class GenerateMessage:
    def __init__(self, counter1, counter2):
        self.counter1 = counter1
        self.counter2 = counter2
        self.types = ["none"]
        self.entity_state = None
        self.name = "generate_message_action"
        self.children = []
        self.verbose = False
        return

    #Condition To Act: checks to see if the action should happen.
    #def condition_to_act(self, event):
    def condition_to_act(self):
        if self.entity_state == None:
            return False
        return True
    
    #Act: if the action should happen, call generateMessage
    def act(self):
        if self.condition_to_act():
            self.generateMessage()
        if self.verbose:
            print("attempting to " + self.name + " ...")
        
    #GenerateMessage: takes the values from the counters passed in in the constructor and sets them to
    #the hud's respective counter numbers
    def generateMessage(self):
        self.entity_state.numAppeared = self.counter1.counter
        self.entity_state.numSuccess = self.counter2.counter
        if self.verbose:
            print("generating message for " + self.entity_state.name)

#frameviewer and display initialization
viewer = fv.FrameViewer(1280, 720, (0, 0, 0), "game jam!", pygame.RESIZABLE)
surface = viewer.make_window()
program_ender = tm.Terminate()
viewer.insert_action(program_ender)
display = ds.DisplayAction()
viewer.insert_action(display)
game_content = [viewer]

#create background
background = bkgd.Background("zap/assets/fall_background_1280x720.webp", [0,0], "background")
backgroundDrawer = drawbkdg.DrawBackground()
background.insert_action(backgroundDrawer)
display.add_entity(background)
game_content.append(background)

#handle player sprite
IMG_SIZE = (128, 128)
rightImgList = []
sprite1 = pygame.image.load("zap/assets/flipped.png")
sprite1 = pygame.transform.scale(sprite1, IMG_SIZE)
sprite2 = pygame.image.load("zap/assets/flipped2.png")
sprite2 = pygame.transform.scale(sprite2, IMG_SIZE)
rightImgList.append(sprite1)
rightImgList.append(sprite2)

leftImgList = []
sprite3 = pygame.image.load("zap/assets/chicken.png")
sprite3 = pygame.transform.scale(sprite3, IMG_SIZE)
sprite4 = pygame.image.load("zap/assets/chicken2.png")
sprite4 = pygame.transform.scale(sprite4, IMG_SIZE)
leftImgList.append(sprite3)
leftImgList.append(sprite4)

#create player object
chicken = sp.Sprite((640, 520), "chicken_sprite", rightImgList, leftImgList, 2, 128, 0)
chickenGrp = pygame.sprite.Group()
drawChicken = drawS.DrawSprite(chickenGrp)
chicken.insert_action(drawChicken)
display.add_entity(chicken)
moveChicken = moveS.MoveSprite()
chicken.insert_action(moveChicken)
game_content.append(chicken)
moveChicken.children.append(drawChicken)

#create leaf sprites
l1 = pygame.image.load("zap/assets/leaf1.png")
l2 = pygame.image.load("zap/assets/leaf2.png")
l3 = pygame.image.load("zap/assets/leaf3.png")
l1L = [l1]
l2L = [l2]
l3L = [l3]
randx1 = random.randrange(50, 1270)
leaf1 = sp.Sprite((randx1, 10), "leaf1", l1L, l1L, 1, 32, 0)
leafGrp = pygame.sprite.Group()
drawLeaf1 = drawS.DrawSprite(leafGrp)
leaf1.insert_action(drawLeaf1)
update1 = UpdateLeaf(chicken, viewer)
leaf1.insert_action(update1)
display.add_entity(leaf1)
game_content.append(leaf1)
update1.children.append(drawLeaf1)

randx2 = random.randrange(50, 1270)
while (randx2 <= randx1 + 20 and randx2 >= randx1 - 20):
    randx2 = random.randrange(10, 1270)
leaf2 = sp.Sprite((randx2, 10), "leaf2", l2L, l2L, 1, 32, 2000)
drawLeaf2 = drawS.DrawSprite(leafGrp)
leaf2.insert_action(drawLeaf2)
update2 = UpdateLeaf(chicken, viewer)
leaf2.insert_action(update2)
display.add_entity(leaf2)
game_content.append(leaf2)
update2.children.append(drawLeaf2)

randx3 = random.randrange(50, 1270)
while (randx3 <= randx1 + 20 and randx3 >= randx1 - 20) or (randx3 <= randx2 + 20 and randx3 >= randx2 - 20):
    randx3 = random.randrange(10, 1270)
leaf3 = sp.Sprite((randx3, 10), "leaf3", l3L, l3L, 1, 32, 4000)
drawLeaf3 = drawS.DrawSprite(leafGrp)
leaf3.insert_action(drawLeaf3)
update3 = UpdateLeaf(chicken, viewer)
leaf3.insert_action(update3)
display.add_entity(leaf3)
game_content.append(leaf3)
update3.children.append(drawLeaf3)

#create total counter
totalCounter = ctr.Counter(0, "total")
totalInc = ci.CounterIncrement()
totalCounter.insert_action(totalInc)

#create collection counter
collectedCtr = ctr.Counter(0, "collected")
collectedInc = ci.CounterIncrement()
collectedCtr.insert_action(collectedInc)

#create generate message action
genMsg = GenerateMessage(totalCounter, collectedCtr)

#add counters to message
totalInc.children.append(genMsg)
collectedInc.children.append(genMsg)

#make counters children to update actions
update1.children.append(totalInc)
update1.children.append(collectedInc)
update2.children.append(totalInc)
update2.children.append(collectedInc)
update3.children.append(totalInc)
update3.children.append(collectedInc)

#create scoreboard
hud = hud.Hud((0,0,0), (10,10), (10,30), 20, "SCORE: ", "TOTAL: ", "zap/assets/origami-mommy.regular.ttf")
drawHud = dh.DrawHud()
hud.insert_action(genMsg)
hud.insert_action(drawHud)
display.add_entity(hud)
game_content.append(hud)

#create soundtrack
pygame.mixer.music.load("zap/assets/soundtrack.mp3")
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play(-1)

#create gameloop and start game
gameLoop = gl.GameLoop("game jam loop")
gameLoop.insert_entity(game_content)
gameLoop.loop()

pygame.quit()