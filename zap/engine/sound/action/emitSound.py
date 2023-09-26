##### EMIT SOUND ######
#Handles actions for emitting a sound
import pygame

class EmitSound:
    #Constructor
    def __init__(self, songStr, time):
        self.songStr = songStr
        self.time = time
        self.name = "play_sound_action"
        self.types = ["none"]
        self.children = []
        self.verbose = False
        return
    
    #Condition To Act: checks to see if the action should happen.
    #In the case of EmitSound, this is always true, as sound has no entity state nor event to check.
    #I decided to keep this format for consistency throughout my code.
    def condition_to_act(self):
        if self.verbose:
            print("playing sound")
        return True
    
    #Act: if condition_to_act is true, calls playSound
    #In the case of EmitSound, this is always true, as condition_to_act is always True.
    #I decided to keep this format for consistency throughout my code.
    def act(self):
        if self.condition_to_act():
            self.playSound()
    
    #Play Sound: uses pygames mixer functions to play sound
    def playSound(self):
        pygame.mixer.music.load(self.songStr)
        pygame.mixer.music.play(self.time)