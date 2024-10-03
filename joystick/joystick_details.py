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

# try :
#     while True:
#         pygame.event.pump()
        
#         for button in range(BUTTONS_COUNT):
#             if controller.get_button(button):
#                 val = int(input("Enter the pressed key"))
#                 hash_map[val] = button
#                 print(hash_map)

# except:
#     print(hash_map)
#     with open("joystick/keymap.txt","w+") as f:
#         f.write(str(hash_map))


# try:
#     while True:
#         pygame.event.pump()

#         for axis in range(AXES_COUNT):
#             axis_value = controller.get_axis(axis)

#             if abs(axis_value) > 0.5 and axis != 3:
#                 # val = str(input("Enter the value for axis : "))
#                 # hash_map[axis] = val
#                 print(axis, axis_value)
# except:
#     print(hash_map)
#     with open("joystick/temp.txt", "w+") as f:
#         f.write(str(hash_map))

