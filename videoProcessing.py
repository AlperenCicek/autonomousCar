import time
import cv2
from imageProcessing import imageProcessing

class videoProcessing:
    def __init__(self, videoName):
        self.videoName = videoName
        
    def videoProcess(self, servoSignalPerFrame = 1):
        cap = cv2.VideoCapture(self.videoName)
        frameCounter = 0
        second = 0
        first = time.time()
        while(cap.isOpened()):
            _, frame = cap.read()
            if frame is not None:
                imageProcessing.image = frame
                cv2.imshow(self.videoName, imageProcessing.imageProcess())
                last = time.time() - first
                if 0.95 < last < 1.01:
                    second += 1
                    print(second, "second(s),", "FPS:", frameCounter)
                    frameCounter = 0
                    first = time.time()
                frameCounter = frameCounter + 1  
                if frameCounter % servoSignalPerFrame == 0:
                    imageProcessing.servoSignal()              
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                print("The video is finished.")
                cap.release()
                cv2.destroyAllWindows()

imageProcessing = imageProcessing()