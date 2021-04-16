import numpy as np
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
import cv2 as cv
import math

"""
Install the corresponding library
"""

"""
Given a set of 2D bounding box on an image, try to visualize them using opencv. The line should be drew in green and 
bold way. Also try to visualize both the gray and color image with bounding box using matplotlib.
params:
    - v_box: (N * 4) (N is the number of boxes. Each row is ordered as x1,y1,x2,y2 to represent a bounding box on the image)
Note:
    - The bounding box may be overrun the range of the image, try make the code robust
    - Links might be help:
        - https://docs.opencv.org/master/d6/d00/tutorial_py_root.html
        - https://matplotlib.org/stable/tutorials/index.html
"""
def limit_range(value,min,max): # Name
    if value<min:
        return min
    if value>max:
        return max
    return value

def draw_box(v_box):
    img = cv.imread(cv.samples.findFile("test.png"))
    sp = img.shape
    height = sp[0]
    width = sp[1]
    for box in boxes: # v_box
        box[0] = limit_range(box[0],0,width)
        box[1] = limit_range(box[1],0,height)
        box[2] = limit_range(box[2],0,width)
        box[3] = limit_range(box[3],0,height)
        
    for box in boxes:
        cv.rectangle(img,(box[0],box[1]),(box[2],box[3]),(0,255,0),3)
    cv.imshow("test", img)
    # Wait key


    # im = mpimg.imread('test.png')
    plt.title("test")
    for row in im:
        for i in row:
            gray = i[2]*0.299 + i[1]*0.587 + i[0]*0.114
            i[0]=gray;
            i[1]=gray;
            i[2]=gray;
    # cvtColor
    plt.imshow(im)
    for box in boxes:
        plt.vlines(box[0],box[1],box[3],"g")
        plt.vlines(box[2],box[1],box[3],"g")
        plt.hlines(box[1],box[0],box[2],"g")
        plt.hlines(box[3],box[0],box[2],"g")
    plt.show()

    pass


if __name__ == '__main__':
    boxes = [
        [47, 246, 133, 468],
        [316, 142, 416, 471],
        [0, 400, 700, 600],
    ]
    draw_box(boxes)
