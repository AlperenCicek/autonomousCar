import numpy as np
from imageProcessing import ImageProcessing
import cv2

class RightSideCamera:
    def __init__(self, image):
        self.image = image
        self.minX1 = None
        self.minY1 = None
        self.maxX2 = None
        self.maxY2 = None

    def capturingFunction(self):
        white_image = ImageProcessing.whiteDetection(self, self.image, 210, 255)
        canny_image = ImageProcessing.canny(self, white_image)
        lines = ImageProcessing.cHoughLinesP(self, canny_image, 45, 5)
        if lines is not None:
            sumX, sumY, count = ImageProcessing.sideCamLines(self, lines)
            #avgX = int(sumX / count)
            avgY = int(sumY / count)
            ImageProcessing.showingLines(self, self.image, 0, int(self.image.shape[0] / 2), self.image.shape[1], int(self.image.shape[0] / 2), 255, 0, 0)
            ImageProcessing.showingLines(self, self.image, 0, avgY, self.image.shape[1], avgY, 255, 255, 0)
            ImageProcessing.showingScreen(self, "Right Line", self.image)
            cv2.imshow("Right Line", self.image)
            if int(self.image.shape[0] / 2) - 5 <= avgY <= int(self.image.shape[0] / 2) + 5:
                return True, False, False, False #F L R E
            if int(self.image.shape[0] / 2) - 5 > avgY:
                return False, False, True, False #F L R E
            if avgY > int(self.image.shape[0] / 2) + 5:
                return False, True, False, False #F L R E
        else:
            return  False, False, False, True #F L R E