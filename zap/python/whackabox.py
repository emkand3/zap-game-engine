import sys
sys.path.append("/Users/emma/Desktop/coding/cpsc4160")
import pygame
import zap.engine.play.entity.frameViewer as fv
import zap.engine.play.entity.gameLoop as gl
import zap.engine.play.action.displayAction as ds
import zap.engine.play.action.terminate as tm

import zap.engine.ui.entity.button as bu
import zap.engine.ui.action.drawButton as db
import zap.engine.ui.action.pressButton as pb
import zap.engine.ui.entity.hud as hud
import zap.engine.ui.action.drawHud as dh

import zap.engine.utility.entity.counter as co
import zap.engine.utility.entity.timer as ti
import zap.engine.utility.action.counterIncrement as ci
import zap.engine.utility.action.activateEntity as ae
import zap.engine.utility.action.deactivateEntity as de
import zap.engine.utility.action.startTimer as st
import zap.engine.utility.action.alarm as al 
import zap.engine.utility.action.updateTimer as ut

import zap.engine.sound.action.emitSound as es
import random

pygame.init()
pygame.mixer.music.set_volume(0.7)

#####   MOVE ACTION   #####
#Moves the box to a random position
class Move:
    #Constructor
    def __init__(self, screen):
        self.screen = screen
        self.types = ["none"]
        self.entity_state = None
        self.name = "move_action"
        self.children = []
        self.verbose = False
    
    #Condition To Act: checks to see if the action should happen.
    def condition_to_act(self):
        if self.entity_state == None:
            return False
        return True
    
    #Act: if the action should happen, call moveButton
    def act(self):
        if self.condition_to_act():
            self.moveButton()
            for c in self.children:
                c.act()
        return
    
    #MoveButton: gets the size of the current screen, then starts a loop to find a random x and y coordinate
    #within the bounds of the screen. If the position is not in the Hud display, the coordinates are used.
    #The box's x and y coordinates are changed to their respective newly generated random coordinates.
    #Starts another loop to get a random color for the button. If the generated random color is not black, 
    #the color is used. The box's color is then set to the newly generated random color.
    def moveButton(self):
        x,y = self.screen.screen.get_size()
        newCoordsFound = False
        newColorFound = False
        while (newCoordsFound == False):
            newX = random.randrange(x-55)
            newY = random.randrange(y-55)
            if (newX > 50) or (newY > 50):
                newCoordsFound = True
        self.entity_state.bounds[0] = newX
        self.entity_state.bounds[1] = newY
        while (newColorFound == False):
            newColorR = random.randrange(255)
            newColorG = random.randrange(255)
            newColorB = random.randrange(255)
            if (newColorR < 250) or (newColorG < 250) or (newColorB < 250):
                newColorFound = True
        self.entity_state.color = (newColorR, newColorG, newColorB)

#####   GENERATE MESSAGE    #####
#Generates a message for the Hud to show the correct counter values
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

#Initialize viewer with terminate action and creates display action
viewer = fv.FrameViewer(1280, 720, (0, 0, 0), "Whack-A-Box", pygame.RESIZABLE)
surface = viewer.make_window()
program_ender = tm.Terminate()
viewer.insert_action(program_ender)
display = ds.DisplayAction()
viewer.insert_action(display)
game_content = [viewer]

#randomizes starting position and color of button
randX = random.randrange(40, 1200)
randY = random.randrange(50,600)
R = random.randrange(0, 220)
G = random.randrange(0, 220)
B = random.randrange(0, 220)

#Initialize button with draw and press actions and adds to display
button = bu.Button((randX, randY, 50, 50), (R,G,B), "button")
drawButton = db.DrawButton()
button.insert_action(drawButton)
display.add_entity(button)
pressButton = pb.PressButton()
button.insert_action(pressButton)
game_content.append(button)

#Initialize timer with alarm, startTimer, and updateTimer actions
timer = ti.Timer("game_timer")
alarm = al.Alarm(1000)
timer.insert_action(alarm)
startTimer = st.StartTimer()
timer.insert_action(startTimer)
updateTimer = ut.UpdateTimer()
timer.insert_action(updateTimer)
updateTimer.children.append(alarm)
alarm.children.append(startTimer)
game_content.append(timer)

#Initialize total counter with increment action
totalCounter = co.Counter(0, "totalCounter")
totalInc = ci.CounterIncrement()
totalCounter.insert_action(totalInc)

#Initialize success counter with increment action
successCounter = co.Counter(0, "successCounter")
successInc = ci.CounterIncrement()
successCounter.insert_action(successInc)

#Initialize hud with draw and generateMsg actions and adds to display
newHud = hud.Hud((252, 186, 3), (10, 10), (10, 30), 12, "Total: ", "Successes: ")
drawHud = dh.DrawHud()
genMsg = GenerateMessage(totalCounter, successCounter)
newHud.insert_action(genMsg)
newHud.insert_action(drawHud)
display.add_entity(newHud)
game_content.append(newHud)

#Adds hud display to respective counter's children actions
totalInc.children.append(genMsg)
successInc.children.append(genMsg)

#Creates activate and deactivate actions, and adds them to button's actions
activate = ae.ActivateEntity()
deactivate = de.DeactivateEntity()
button.insert_action(activate)
button.insert_action(deactivate)

#Adds necessary counter and deactivate actions to children of needed parent actions
pressButton.children.append(successInc)
pressButton.children.append(deactivate)

#Initialize move action and adds to button, then adds necessary children to parent actions
moveButton = Move(viewer)
button.insert_action(moveButton)
pressButton.children.append(moveButton)
moveButton.children.append(activate)
moveButton.children.append(totalInc)
alarm.children.append(moveButton)
pressButton.children.append(startTimer)

#Initialize sound actions and add them to appropriate actions as children
successSound = es.EmitSound("zap/assets/success.mp3")
failSound = es.EmitSound("zap/assets/fail.wav")
pressButton.children.append(successSound)
alarm.children.append(failSound)

#Initialize game loop and starts loop
gameLoop = gl.GameLoop("Whack-A-Box Loop")
gameLoop.insert_entity(game_content)
gameLoop.loop()

pygame.quit()