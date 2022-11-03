import cv2
import numpy as np
class Crop:
    """
    Draws rect with mouse, crop image
    according to the rect.
    Operate:instance.main(pathRead,pathWrite)
    parameters:
    pathRead raw image
    pathWrite cropped image
    left button draws rectangle
    right button crop
    """
    def draw_rect(self,event,x,y,flags,param):
        #Left mouse press start drawing
        if event == cv2.EVENT_LBUTTONDOWN:
            self.startX, self.startY = x, y
        #Left release stop drawing
        elif event == cv2.EVENT_LBUTTONUP:
            self.x=x
            self.y=y
            # Draw green rectangle
            cv2.rectangle(self.img, (self.startX, self.startY), (self.x,self.y), (0, 255, 0), 1)
        #Right dubble click delete old image read new one
        elif event==cv2.EVENT_RBUTTONDBLCLK:
            del(self.img)
            self.img = cv2.imread(param)
        #Right click save croped image to disk
        elif event==cv2.EVENT_RBUTTONDOWN:
            #Sorting in order to slice image properly
            sortx=sorted([self.startX,self.x])
            sorty=sorted([self.startY,self.y])
            #Write to disk
            cv2.imwrite(self.path,self.img[sorty[0]:sorty[1], sortx[0]:sortx[1]])

    def main(self,pathRead,pathWrite):
        """
            :param pathRead: 
            :param pathWrite: 
            :return: 
            """
        self.img = cv2.imread(pathRead)
        self.path=pathWrite
        cv2.namedWindow('image')
        cv2.setMouseCallback('image',self.draw_rect,param=pathRead)
        while True:
            cv2.imshow('image',self.img)
            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                break
        cv2.destroyAllWindows()

crop=Crop()
crop.main('img.jpg','croped.jpg')
