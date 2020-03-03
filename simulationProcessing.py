import numpy as np
import cv2
import time
from mainCamera import MainCamera
from sideCamera import SideCamera
from pynput.keyboard import Key, Controller
from PIL import ImageGrab

class SimulationProcessing:
    def __init__(self, x, y, w, h, camera):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.camera = camera
        self.left = False
        self.right = False
        self.forward = True
        self.error = False

    def simulationFunction(self):
        keyboard = Controller()
        time.sleep(5)
        while(True):
            if self.camera == "MainCamera":
                img = ImageGrab.grab((self.x, self.y, self.w, self.h))
                mainCamera = MainCamera(np.array(img))
                self.forward, self.left, self.right = mainCamera.capturingFunction()
            elif self.camera == "SideCamera":
                img = ImageGrab.grab((self.x, self.y, self.w, self.h))
                sideCamera = SideCamera(np.array(img))
                self.forward, self.left, self.right,self.error = sideCamera.capturingFunction()
            if self.camera is "MainCamera":
                keyboard.press('w')
                if self.left == True:
                    keyboard.release('d')
                    print("TURN LEFT.")
                    keyboard.press('a')
                if self.right == True:
                    keyboard.release('a')
                    print("TURN RIGHT.")
                    keyboard.press('d')
                if self.forward == True:
                    keyboard.release('a')
                    keyboard.release('d')
                    print("OK. Slope:")
            elif self.camera is "SideCamera":
                if self.error is True:
                    keyboard.release('w')
                    keyboard.release('a')
                    keyboard.release('d')
                    print("No lane detected..")
                else:
                    keyboard.press('w')
                    if self.left == True:
                        keyboard.release('d')
                        print("TURN LEFT.")
                        keyboard.press('a')
                    if self.right == True:
                        keyboard.release('a')
                        print("TURN RIGHT.")
                        keyboard.press('d')
                    if self.forward == True:
                        keyboard.release('a')
                        keyboard.release('d')
                        print("OK. Slope:")
            if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        cv2.destroyAllWindows()
        keyboard.release('w')