"""
    The purpose of this code is to segment 
    the fruit images so they can be ready for augmentation 

"""
import cvzone
import numpy as np
import cv2
import argparse
from rembg import remove
from PIL import Image
import sys
sys.path.append("..")




test_image="data/fruits-360-original-size/Training/apple_6/r0_0.jpg"


def main():
    # Processing the image
    input = Image.open(test_image)
    # Removing the background from the given Image
    output = remove(input)
    output.save("test.png")
    output = np.array(output) 
    output = cv2.cvtColor(output, cv2.COLOR_RGBA2BGRA)
    background = cv2.imread("data/background.jpg",cv2.IMREAD_UNCHANGED)
    img_result=cvzone.overlayPNG(background,output,[20,20])
    #Saving the image in the given path
    cv2.imwrite(filename="test.png",img=img_result)



    return 0

if __name__=="__main__":
    main()
