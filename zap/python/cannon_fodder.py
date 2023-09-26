#Import statements:
import sys
sys.path.append("/Users/emma/Desktop/coding/cpsc4160")
import pygame
import random

import zap.engine.play.entity.frameViewer as fv
import zap.engine.play.entity.gameLoop as gl
import zap.engine.play.action.terminate as tm
import zap.engine.play.action.displayAction as ds

import zap.engine.actor.entity.rectangle as r
import zap.engine.actor.action.drawRectangle as dr
import zap.engine.actor.entity.circle as c
import zap.engine.actor.action.drawCircle as dc
import zap.engine.actor.action.is_inside as ins

import zap.engine.utility.entity.timer as ti
import zap.engine.utility.action.alarm as al
import zap.engine.utility.action.startTimer as st
import zap.engine.utility.action.updateTimer as ut
import zap.engine.utility.action.activateEntity as ae

import zap.engine.physics.entity.particles as part
import zap.engine.physics.entity.gravity_force as gforce
import zap.engine.physics.action.gravity_force_action as gfa
import zap.engine.physics.action.position_solve as ps
import zap.engine.physics.action.velocity_solve as vs
import zap.engine.physics.action.euler_solve as es
import zap.engine.physics.action.pick_position as pick
import zap.engine.actor.action.put_position as put
import zap.engine.physics.entity.rectangle_collider as coll
import zap.engine.physics.action.inside_rect_collision as inc
import zap.engine.physics.action.outside_rect_collision as otc
import zap.engine.physics.entity.spring_force as spf
import zap.engine.physics.action.spring_force_action as spfa
import zap.engine.physics.entity.drag_force as dfc
import zap.engine.physics.action.drag_force_action as dfca
import zap.engine.physics.action.activate as actForce
import zap.engine.physics.action.deactivate as deactForce

#function to create a list of num number of circles
def get_circles(num):
    circle_list = []
    radius = 10
    for i in range(0, num):
        x = 1
        y = random.randrange(50, 400)
        circle_bounds = (x, y)
        findColor = True
        #loop to create a color, making sure the color is not black
        while findColor:
            R = random.randrange(0, 255)
            G = random.randrange(0, 255)
            B = random.randrange(0, 255)
            if R > 10 and G > 10 and B > 10:
                findColor = False
        circle_color = (R, G, B)
        newCirc = c.Circle(radius, circle_color, "circ_" + str(i), circle_bounds)
        newDraw = dc.DrawCircleAction()
        newCirc.insert_action(newDraw)
        circle_list.append(newCirc)
    return circle_list

#function to create a list of particles, as many as the length of circleList
def get_particles(circList, screenx, screeny, left, right):
    particles = []
    partEnt = part.Particle("particles")
    particles.append(partEnt)

    #loops through and creates particle entities
    for i in circList:
        position = list(i.position)
        velocity = [(60.0*random.random()), (7.4*random.random()+1)]
        mass = 1.0
        partEnt.add_particle(position, velocity, mass, False, True, True)

    #create spring force
    spring = spf.SpringForce("spring_force")
    spring.spring_constant = 0.006
    springForce = spfa.SpringForceAction()
    spring.insert_action(springForce)

    #create gravity force
    gravity = gforce.GravityForce("gravity_force")
    gravity.gravity = [0.0, 0.5]
    gravForce = gfa.GravityForceAction()
    gravity.insert_action(gravForce)

    #create drag force
    drag = dfc.DragForce("drag_force")
    drag.drag_constant = 0.03
    dragForce = dfca.DragForceAction()
    drag.insert_action(dragForce)
    
    #create solvers for position and velocity
    psolve = ps.PositionSolve()
    partEnt.insert_action(psolve)

    vsolve = vs.VelocitySolve()
    partEnt.insert_action(vsolve)
    vsolve.children.append(springForce)
    vsolve.children.append(gravForce)
    vsolve.children.append(dragForce)

    #create euler solver
    esolve = es.EulerSolve()
    esolve.dt = 0.105
    partEnt.insert_action(esolve)
    esolve.children.append(psolve)
    esolve.children.append(vsolve)
    esolve.types.append("loop")

    #for loop to find position, and to allow for activating/deactivating of forces
    for i in range(0, len(circle_list)):
        pickPos = pick.PickPosition(i)
        putPos = put.PutPosition(i)

        #create activation/deactivation actions for each force
        actSpring = actForce.ActivatePhys(i, 1)
        partEnt.insert_action(actSpring)
        deactSpring = deactForce.DeactivatePhys(i, 1)
        partEnt.insert_action(deactSpring)

        actDrag = actForce.ActivatePhys(i, 2)
        partEnt.insert_action(actDrag)
        deactDrag = deactForce.DeactivatePhys(i, 2)
        partEnt.insert_action(deactDrag)

        #add is_inside actions as children of activate and deactivate, in order
        #to allow position to be sent to activate/deactivate
        deactDrag.children.append(left)
        actSpring.children.append(left)

        deactSpring.children.append(right)
        actDrag.children.append(right)

        #add children to corresponding parent 
        partEnt.insert_action(pickPos)
        circle_list[i].insert_action(putPos)
        pickPos.children.append(putPos)
        esolve.children.append(pickPos)
        pickPos.children.append(actDrag)
        pickPos.children.append(deactDrag)
        pickPos.children.append(actSpring)
        pickPos.children.append(deactSpring)

    #Collision rectangles: one inner, the rest outer
    windowCol = coll.RectangleCollider([0, 0], [screenx, screeny], "window_collider")
    innerCol = inc.InsideRectCollision()
    windowCol.insert_action(innerCol)
    psolve.children.append(innerCol)

    rect1Col = coll.RectangleCollider([800, 300], [870, 720], "rect_1_collider")
    outerCol1 = otc.OutsideRectCollision()
    rect1Col.insert_action(outerCol1)
    psolve.children.append(outerCol1)
    game_content.append(rect1Col)

    rect2Col = coll.RectangleCollider([800, 0], [870, 220], "rect_2_collider")
    outerCol2 = otc.OutsideRectCollision()
    rect2Col.insert_action(outerCol2)
    psolve.children.append(outerCol2)
    game_content.append(rect2Col)

    rect3Col = coll.RectangleCollider([1020, 500], [1200 ,520], "rect_3_collider")
    outerCol3 = otc.OutsideRectCollision()
    rect3Col.insert_action(outerCol3)
    psolve.children.append(outerCol3)
    game_content.append(rect3Col)

    rect4Col = coll.RectangleCollider([920, 590], [1100, 610], "rect_4_collider")
    outerCol4 = otc.OutsideRectCollision()
    rect4Col.insert_action(outerCol4)
    psolve.children.append(outerCol4)
    game_content.append(rect4Col)

    #barrier collider that activates once alarm goes off
    barColRect = coll.RectangleCollider([800, 0], [870, 760], "barricade_collider")
    barCol = otc.OutsideRectCollision()
    barColRect.insert_action(barCol)
    barColRect.active = False
    activateCol = ae.ActivateEntity()
    barColRect.insert_action(activateCol)
    psolve.children.append(barCol)
    alarm.children.append(activateCol)
    game_content.append(barColRect)

    return particles


#Initialize viewer with terminate action and creates display action
viewer = fv.FrameViewer(1280, 720, (0, 0, 0), "Cannon Fodder", pygame.RESIZABLE)
surface = viewer.make_window()
program_ender = tm.Terminate()
viewer.insert_action(program_ender)
display = ds.DisplayAction()
viewer.insert_action(display)
game_content = [viewer]

#timer/alarm for closing barricade
closeGap = ti.Timer("close gap timer")
alarm = al.Alarm(9000)
closeGap.insert_action(alarm)
startTimer = st.StartTimer()
closeGap.insert_action(startTimer)
updateTimer = ut.UpdateTimer()
closeGap.insert_action(updateTimer)
updateTimer.children.append(alarm)
alarm.children.append(startTimer)
game_content.append(closeGap)

#rectangles for checking particle position
leftRect = r.Rectangle(870, 300, (0, 0), (0, 0, 0), "leftRect", 0)
drawLeft = dr.DrawRectangleAction()
leftRect.insert_action(drawLeft)
display.add_entity(leftRect)
game_content.append(leftRect)
insideLeft = ins.IsInside()
leftRect.insert_action(insideLeft)

rightRect = r.Rectangle(480, 420, (870, 0), (0, 0, 0), "rightRect", 0)
drawRight = dr.DrawRectangleAction()
rightRect.insert_action(drawRight)
display.add_entity(rightRect)
game_content.append(rightRect)
insideRight = ins.IsInside()
rightRect.insert_action(insideRight)

#rectangle for lower barricade
botRect = r.Rectangle(70, 420, (800, 300), (255, 255 ,255), "botRect", 0)
drawBR = dr.DrawRectangleAction()
botRect.insert_action(drawBR)
display.add_entity(botRect)
game_content.append(botRect)

#rectangle for upper barricade
topRect = r.Rectangle(70, 220, (800, 0), (255, 255, 255), "topRect", 0)
drawTR = dr.DrawRectangleAction()
topRect.insert_action(drawTR)
display.add_entity(topRect)
game_content.append(topRect)

#rectangle for upper platform
upperRect = r.Rectangle(180, 20, (1020, 500), (255, 255, 255), "upperRect", 0)
drawUR = dr.DrawRectangleAction()
upperRect.insert_action(drawUR)
display.add_entity(upperRect)
game_content.append(upperRect)

#rectangle for lower platform
lowerRect = r.Rectangle(180, 20, (920, 590), (255, 255, 255), "lowerRect", 0)
drawLR = dr.DrawRectangleAction()
lowerRect.insert_action(drawLR)
display.add_entity(lowerRect)
game_content.append(lowerRect)

#rectangle for closing barricade
barricadeRect = r.Rectangle(70, 80, (800, 220), (255, 255, 255), "barricade", 0)
drawBar = dr.DrawRectangleAction()
barricadeRect.insert_action(drawBar)
display.add_entity(barricadeRect)
game_content.append(barricadeRect)

#set up timer for closing barricade after 9 seconds
drawBar.children.append(startTimer)
barricadeRect.active = False
activate = ae.ActivateEntity()
barricadeRect.insert_action(activate)
alarm.children.append(activate)

#create list of 100 circles
circle_list = get_circles(100)
#create list of 100 particles
particle_list = get_particles(circle_list, 1280, 720, insideLeft, insideRight)

#add all circles and particles to game_content
game_content = game_content + circle_list + particle_list

#add all circles to display
for i in circle_list:
    display.add_entity(i)

#Initialize game loop and starts loop
gameLoop = gl.GameLoop("Cannon Fodder Loop")
gameLoop.insert_entity(game_content)
gameLoop.loop()

pygame.quit()