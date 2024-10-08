import pygame
import time
from threading import Thread
from pygame import joystick

direction_mapper = {
    (0,0)  : 'S',
    (0,1)  : 'F',
    (1,0)  : 'R',
    (-1,0) : 'L',
    (0,-1) : 'B'
}

class Joystick():

    def __init__(self, details = False):

        # Initialize paramters
        pygame.init()
        self.stop = False

        '''
        Parameter to be Passed
        '''
        # Movement Paramter
        self.direction = direction_mapper[(0,0)]
        # Button
        self.button = None
        # Speed
        self.speed = 0
        '''
        End of parameters
        '''

        # Checking for Joystick 
        joystick_count = joystick.get_count()
        if joystick_count == 0:
            print("Joystick Not Found !")
            print("Connect the Joystick...")
            while joystick.get_count() == 0:
                time.sleep(3)

        # Details 
        self.controller = joystick.Joystick(0)
        self.controller.init()
        print("Joystick Found !")
        print(f"Joystick Name : {self.controller.get_name()}")

        # Keys Counts
        self.button_count = self.controller.get_numbuttons()
        self.hat_count = self.controller.get_numhats()
        self.axis_count = self.controller.get_numaxes()

        if details:
            print(f"No of Buttons :{self.button_count}")
            print(f"No of Axes : {self.axis_count}")
            print(f"No of Hats : {self.hat_count}")

        # Start Thread
        self._thread = Thread(target=self.read_joystick)
        self._thread.start()

    def _get_button(self):
        for button in range(self.button_count):
            if self.controller.get_button(button):
                return button
        return None
    
    def _get_speed(self):
        axis_value = self.controller.get_axis(3)
        # (-1,1) range is converted into (0,1)
        return (axis_value + 1) / 2

    def read_joystick(self):

        while not self.stop:
            pygame.event.pump()

            # hat values
            hat_value = self.controller.get_hat(0)
            # print(hat_value)
            self.direction = direction_mapper[hat_value]

            self.button = self._get_button()
            self.speed = self._get_speed()
            time.sleep(0.5)


if __name__ == '__main__':
    joystick = Joystick()
    try:
        while True:
            print(joystick.direction)
            # time.sleep(3)
    except:
        joystick.stop = True
