import pygame
from pygame import joystick

pygame.init()
controller = joystick.Joystick(0)
controller.init()

while True:
    pygame.event.pump()
    print(controller.get_hat(0))
