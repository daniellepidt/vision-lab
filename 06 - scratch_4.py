import cv2,numpy as np,math
class Contour():
    def __init__(self,path,n):
        self.path=path
        #Num objects
        self.n=n

    def compute(self):
        #Read image from path
        im=cv2._____(self.path)
        #Convert to gray scale
        imgray = cv2.__________(im, cv2.___________)
        #Convert to one bit above 127 white, below black
        ret, thresh = cv2.threshold(imgray, ___, ___, 0)
        #Find contours
        image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        #Sort the contours in reverse order using Lambda, sorted,cv2.arcLength
        mmuyan=____(______, key= lambda c : ________(_,True),reverse=True )
        #Declaire list of center of mases.
        self.cms=[]
        #Search only for a given num of objects
        for i in range(___):
            #Define a rectangle around each contour
            rect = cv2.minAreaRect(_____)
            #Define a box 4 drawing
            box = cv2.boxPoints(rect)
            #Convert box points to integers (pixeles)
            box = np.int0(box)
            #Draw contours boundary on colored image
            self.pic = cv2.drawContours(__, [box], 0, (0, 0, 255), 2)
            #Get the momets dictionary
            M=cv2.moments(____)
            #Get x,y of the center of mass point.
            cx=int(M['m10']/M['m00'])
            cy=int(M['m01']/M['m00'])
            #Draw green circles on the centers.
            self.pic=cv2.circle(__,(__,__),3,(0,255,0),2)
            #Add the center point to the list
            self.cms._____((__,__))

    def show(self):
        #Compute the center of mass for desired num of objects
        self.______()
        #Show the result as a picture
        cv2.____('pic',______)
        #Wait untill button is pressed
        ___________(_)
        #Clear memory.
        cv2.destroyAllWindows()

    def get_cm(self):
        #Compute the center of mass for desired num of objects
        _____________()
        #Return list with all center of mases.
        return ______

cont=Contour('img1.jpg',3)
cont.show()
print(cont.get_cm())
