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
        im=cv2._____(self.path)
        imgray = cv2.__________(im, cv2.___________)
        ret, thresh = cv2.threshold(imgray, ___, ___, 0)
        image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        mmuyan=____(______, key= lambda c : ________(_,True),reverse=True )
        #Declaire list of center of mases,and list of angles
        self.cms=[];self.angles=[]
        for i in range(___):
            rect = cv2.minAreaRect(_____)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            #Compute angle of object
            angle = self._____(___)
            self.pic = cv2.drawContours(__, [box], 0, (0, 0, 255), 2)
            M=cv2.moments(____)
            cx=int(M['m10']/M['m00'])
            cy=int(M['m01']/M['m00'])
            self.pic=cv2.circle(__,(__,__),3,(0,255,0),2)
            #Put the angle values on the center of mass of the image
            cv2.putText(_____,str(round(____,2)),(cx,cy),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (100, 100, 100), 2)
            self.cms._____((__,__))
            #Add angle to the angles
            self._________________

    def show(self):
        """
        Shows the image with circles around cms, and the angles of the objects
        :return:
        """
        #Compute the center of mass for desired num of objects
        self.______()
        #Show the result as a picture
        cv2.____('pic',______)
        #Wait untill button is pressed
        ___________(_)
        #Clear memory.
        cv2.destroyAllWindows()

    def get_cm(self):
        """

        :return:List with n cms of mobjects
        """
        #Compute the center of mass for desired num of objects
        _____________()
        #Return list with all center of mases.
        return ______

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
        cos=______________________________
        return ____________________________

    def get_angles(self):
	"""

        :return:List angles of n objects.
        """
        self.compute()
        return ________

cont=Contour('img1.jpg',3)
cont.show()
print(cont.get_angles())
