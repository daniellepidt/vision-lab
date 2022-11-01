import cv2
import numpy as np
class DetectColor():
    """
    Dynamic tracking system. The user chooses with the left button of the mouse which
    color to track.
    Parameters: None.
    Return: None.
    """	
    def __init__(self):
        cv2.namedWindow('img')
        cv2.setMouseCallback(___,___)
        #Variable that enable the tracking only after the first click.
        self.firstClick=False

    def get_color(self,event,x,y,flags,param):
        #if left mouse was clicked
        if event == cv2.___________:
            self.x=__
            self.y=___
            self.firstClick=True
            #Variable that enable the computation of the color to track only once
            #after each click
            self.notClickedYet = True

    def main(self):
        #Enable video
        cap = ________________(0)
        while ___________:
            #Read from camera
            _, frame = ____.read()
            #Show stream on 'img' window
            cv2.___________(_____________)
            #Wait to show stream
            k = ____________
            #Escape breaks the code
            if ___________:
                ___________
            if self.firstClick:
                #Convert image to hsv format.
                hsv = _____________________
                if self.notClickedYet:
                    #Lower bound is determined by taking the h value and subtracting 10
                    #and s and v values are fixed to 50
                    lower=np.array([_______________,____________,____________])
                    #Upper bound is determined by taking the h value and adding 10
                    #and s and v values are fixed to 255
                    upper=np.array([____________,_____________,____________])
                    self.notClickedYet=False
                #Mask of 0 and 1 of the pixels within the range between lower and upper
                mask = cv2.inRange(hsv, lower, upper)
                #Apply the mask to the original pic
                res = cv2.bitwise_and(frame,frame, mask= mask)
                #Show the mask
                cv2.imshow('mask',___)
                #Show the tracked color
                cv2.imshow('res',___)
        cv2.destroyAllWindows()

detect=DetectColor()
detect.main()
