import pygame
import time
from pygame import joystick

pygame.init()
print(f"No of joysticks Found : {joystick.get_count()}")

controller = joystick.Joystick(0)

print(f"Joystick Name : {controller.get_name()}")
print(f"No of Axes : {controller.get_numaxes()}")
print(f"No of Buttons :{controller.get_numbuttons()}")
print(f"No of Hats : {controller.get_numhats()}")
