import cv2
import numpy as np

def fun():
    picture = str(input("Enter File Name : "))
    
    img = cv2.imread(picture, 0)
    cv2.imshow("Image1",img)
    
    invert = cv2.bitwise_not(img)
    #cv2.imshow("Invert",invert)
    
    blur = cv2.GaussianBlur(invert, (21,21), 0)
    #cv2.imshow("Blur", blur)
    
    invert_blur = cv2.bitwise_not(blur)
    #cv2.imshow("Invert Blur", invert_blur)
    
    sketch = cv2.divide(img,invert_blur, scale=256.0)  
    #cv2.imshow("Image2",sketch)
    
    if cv2.waitKey(0) == 27:
        cv2.destroAllWindows()
    elif cv2.waitKey(0) == 's':
        cv2.imwrite(f"new_{picture}")
fun()
