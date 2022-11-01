import cv2,os
def savePic(path='img1.jpg',flag=None):
    """
    Show stream s key save img q key aborts.
    parameters:
    path path 4 saving image
    flag flag to convert image
    """
    cap = cv2.VideoCapture(0)
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        # Display the resulting frame
        cv2.imshow('frame',frame)
        # Wait for press
        w=_____________________
        # Quit
        if w==__________:
            break
        # Saving
        elif w==________:
            if ____:
                frame=_______________
            #Save to disk.
            cv2.imwrite(path,frame)
    #Release memory.
    cap.release()
    cv2.destroyAllWindows()

