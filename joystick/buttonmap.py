import pygame
from pygame import joystick

pygame.init()
controller = joystick.Joystick(0)
controller.init()

BUTTONS_COUNT = controller.get_numbuttons()
hash_map = {}
try :
    while True:
        pygame.event.pump()
        
        for button in range(BUTTONS_COUNT):
            if controller.get_button(button):
                val = int(input("Enter the pressed key/q (quit) : "))
                hash_map[val] = button

except:
    print(hash_map)
    '''
    Un comment only if you want to re-configure the keymaps
    '''
    # with open("joystick/keymap.txt","w+") as f:
    #     f.write(str(hash_map))
