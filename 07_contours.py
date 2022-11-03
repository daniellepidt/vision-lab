import cv2,numpy as np,math
class Contour():
    """
    Computes center of mass of n objects
    parameters:
        path: path to pic
        n: Num of objects
    """
    def __init__(self,path,n):
        self.path=path
        #Num objects
        self.n=n

    def compute(self):
        """
        Computes the cms using moments.
        :return:
        """
        im=cv2.imread(self.path)
        imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(imgray, 127, 255, 0)
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        mmuyan=sorted(contours, key= lambda c : cv2.arcLength(c,True),reverse=True )
        #Declaire list of center of mases,and list of angles
        self.cms=[];self.angles=[]
        for i in range(3):
            rect = cv2.minAreaRect(mmuyan[i])
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            #Compute angle of object
            angle = self.comp_angle(box)
            self.pic = cv2.drawContours(im, [box], 0, (0, 0, 255), 2)
            M=cv2.moments(mmuyan[i])
            cx=int(M['m10']/M['m00'])
            cy=int(M['m01']/M['m00'])
            self.pic=cv2.circle(self.pic,(cx,cy),3,(0,255,0),2)
            #Put the angle values on the center of mass of the image
            cv2.putText(self.pic,str(round(angle,2)),(cx,cy),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (100, 100, 100), 2)
            self.cms.append((cx,cy))
            #Add angle to the angles
            self.angles.append(angle)

    def show(self):
        """
        Shows the image with circles around cms, and the angles of the objects
        :return:
        """
        #Compute the center of mass for desired num of objects
        self.compute()
        #Show the result as a picture
        cv2.imshow('pic',self.pic)
        #Wait untill button is pressed
        cv2.waitKey(0)
        #Clear memory.
        cv2.destroyAllWindows()

    def get_cm(self):
        """

        :return:List with n cms of mobjects
        """
        #Compute the center of mass for desired num of objects
        self.compute()
        #Return list with all center of mases.
        return self.cms

    def comp_angle(self,box):
        """
        Computes angle of object
        :param box: 
        :return: Degrees of angle of the narrow side of object 
        """
        #Compute the angle of the narrow dimention of the object
        #Find the narrow dim of the object
        dist1=np.linalg.norm(box[1]-box[0])
        dist2=np.linalg.norm(box[3]-box[0])
        if dist1<dist2:
            #Using formula angle=arcos((x dot y)/|x|*|y|) first vector is the narrow side of object
            #dist1 second vector is x vector
            cos=np.dot((box[1]-box[0]),(10,0))/(dist1*10)
            return math.degrees(math.acos(cos))
        #dist2 is the narrow side
        cos=np.dot((box[3]-box[0]),(10,0))/(dist2*10)
        return math.degrees(math.acos(cos))

    def get_angles(self):
        """
        :return:List angles of n objects.
        """
        self.compute()
        return self.angles

cont=Contour('img1.jpg',3)
cont.show()
print(cont.get_angles())
