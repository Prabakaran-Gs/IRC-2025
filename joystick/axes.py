import pygame
from pygame import joystick

pygame.init()
controller = joystick.Joystick(0)
controller.init()

'''
3 is refers to speed so it is not displayed
'''

AXES_COUNT = controller.get_numaxes()

while True:
    pygame.event.pump()

    for axis in range(AXES_COUNT):
        axis_value = controller.get_axis(axis)

        if abs(axis_value) > 0.5 and axis != 3:
            print(f"axes {axis} \t values {axis_value}")
