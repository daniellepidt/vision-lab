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
        if event == cv2.EVENT___________:
            self.startX,self.startY = ___,__
        #Left release stop drawing
        elif event == cv2.EVENT___________:
            self.x=___
            self.y=_____
            # Draw green rectangle
            cv2.________(self.img, (_______, __________), (_____,________), (0, 255, 0), 1)
        #Right dubble click delete old image read new one
        elif event==cv2.EVENT_RBUTTONDBLCLK:
            del(_____)
            self.____ = cv2.imread(param)
        #Right click save croped image to disk
        elif event==cv2.EVENT_________:
            #Sorting in order to slice image properly
            sortx=sorted([_______,_______])
            sorty=sorted([______,_______])
            #Write to disk
            cv2._____(self.path,self.img[_____:_____,____:____])

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
            cv2.imshow('image',_____)
            _ = cv2.waitKey(1) & 0xFF
            if k == 27:
                break
        cv2.destroyAllWindows()

crop=Crop()
crop.main('img.jpg','croped.jpg')
