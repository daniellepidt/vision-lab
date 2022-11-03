import cv2, numpy as np
class FetureMatch:
    """
    Use Orb, Brisk, Kaze, Akaze methods to detect a predefined object.
    Parameters:
        modes: list of methods
        img2Find: A croped image we have 2 find
        img2Search: An image contains few objects includes the croped one.
    Methods:
        compute: Computes the center of mass of the predefined object
        show: Show the img2Search with box around the img2Find
        getCm: Returns dictionary key=methodName value=centerOfMass,#goodPoints
    """
    def __init__(self,modes,img2Find,img2Search):
        self.MIN_MATCH_COUNT = 8
        self.img1 = cv2.imread(img2Find)   # queryImage
        self.img2 = cv2.imread(img2Search) # trainImage
        self.modes = modes
        #Dictinary for center of masses key=mode val=cm
        self.cms = {}

    def compute(self):
        #Convert images to gray scale  cv2.cvtColor
        gray1 = cv2.cvtColor(self.img1,cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(self.img2,cv2.COLOR_BGR2GRAY)
        #Dictinary for center of masses key=mode val=cm
        myDic = {}
        # Declare distance type 4 the matcher to orb and brisk.
        distanceType = cv2.NORM_HAMMING
        for mode in self.modes:
            # All modes have same signature cv2.mode_create() mode is defined in big letters.
            # Parameters: orb:nfeatures=10000, brisk:thresh=10, kaze and akaze:distanceType:cv2.DIST_L2
            # ToDo declare all detectors
            if mode == 'orb':
                detector = cv2.ORB_create(nfeatures=10000)
            elif mode == 'brisk':
                detector = cv2.BRISK_create(thresh=10)
            elif mode == 'kaze':
                detector = cv2.KAZE_create()
                distanceType = cv2.DIST_L2
            elif mode == 'akaze':
                detector = cv2.AKAZE_create()
                distanceType = cv2.DIST_L2
            # Declare matcher
            matcher = cv2.BFMatcher(distanceType)
            #kp pos of keyPoints, des descriptors interesting points.
            kp1, des1 = detector.detectAndCompute(gray1,None)
            kp2, des2 = detector.detectAndCompute(gray2,None)
            matches = matcher.knnMatch(des1,des2,k=2)
            good = []
            for m,n in matches:
                if m.distance < 0.7*n.distance:
                    good.append(m)
            if len(good)>self.MIN_MATCH_COUNT:
                src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
                dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)
                M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
                h,w = gray1.shape
                pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
                dst = cv2.perspectiveTransform(pts,M)
                #Flatten the points of the object to a list.
                rvl=dst.ravel()
                cmx=cmy=nPts=0
                # Calculate the center of mass
                # Traverse the Flatten list of points
                for i in range(len(rvl)):
                    # Sum the x value of the points, and count num of points
                    if i % 2 != 0:
                        cmx += rvl[i]
                        nPts += 1
                    else:
                        # Sum the Y value of the points
                        cmy += rvl[i]
                #Calculate C.M should be integer (pixel)
                self.cm=(int(cmx/nPts),int(cmy/nPts))
                #Update dictionary cms with the cm position and the number of
                #good points in every method.
                self.cms[mode] = (self.cm, nPts)
                #Draw green poligon around the searched object on the original picture
                self.img2 = cv2.polylines(self.img2,[np.int32(dst)],True,(0,255,0),3, cv2.LINE_AA)
                #Draw blue circle of the C.M on the original image
                #circle(img,pos,radius,color,thikness
                self.img2=cv2.circle(self.img2,self.cm,3,(255,0,0),5)
            else:
                print ("mode=%s ,Not enough matches are found - %d/%d" % (mode,len(good),self.MIN_MATCH_COUNT))

    def show(self):
        """
        Shows the boxed colored detected object in the searched image
        :return:
        """
        #Compute the center of mass for desired num of objects
        self.compute()
        #Show the result as a picture
        cv2.imshow('pic', self.img2)
        #Wait untill button is pressed
        cv2.waitKey(0)
        #Clear memory.
        cv2.destroyAllWindows()

    def getCm(self):
        """
        :return: dictionary with the method as key, center of mass and #good matches
        as a tuple value
        """
        return self.cms
fm=FetureMatch(['orb','brisk','kaze','akaze'],'croped.jpg','img.jpg')
fm.show()
print(fm.getCm())
