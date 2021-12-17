import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.misc import face
from skimage.measure import label, regionprops
from skimage import color

def check(image, y, x): 
    if not 0 <= x < image.shape[1]: 
        return False 
    if not 0 <= y < image.shape[0]: 
        return False 
    if image[y, x] != 0: 
        return True 
    return False 
 
def neighbours_around(image, y, x): 
    left = y, x - 1 
    top = y - 1, x 
    right = y, x + 1 
    down = y + 1, x 
    if not check(image, *left): 
        left = None, None 
    if not check(image, *top): 
        top = None, None 
    if not check(image, *right): 
        right = None, None 
    if not check(image, *down): 
        down = None, None 
    return left, top, right, down 

def isRec(im):
    count = 0;
    for y in range(im.shape[0]):
        for x in range(im.shape[1]):
            if (im[y,x] == 1):
                n4 = neighbours_around(im, y, x)
                left = 0
                top = 0
                right = 0
                down = 0
                if(n4[0][0] != None):
                    left = im[n4[0]]
                if(n4[1][0] != None):
                    top = im[n4[1]]
                if(n4[2][0] != None):
                    right = im[n4[2]]
                if(n4[3][0] != None):
                    down = im[n4[3]]
                    
                if (left == 1 and top == 1 and im[y-1, x-1] == 0):
                    return False
                if (top == 1 and right == 1 and im[y-1, x+1] == 0):
                    return False
                if (right == 1 and down == 1 and im[y+1, x+1] == 0):
                    return False
                if (down == 1 and left == 1 and im[y+1, x-1] == 0):
                    return False
    return True

image = plt.imread("balls_and_rects.png")
binary = np.sum(image, 2)
binary[binary > 0] = 1

labeled = label(binary)
print("Objects: " + str(labeled.max()))

imagehsv = color.rgb2hsv(image)
cols = np.unique(imagehsv[:,:,0]);
regions = regionprops(labeled)
circles = {}
rectangles = {}
errorCount = 0

for reg in regions:
    y = int(reg.centroid[0])
    x = int(reg.centroid[1])
    hue = imagehsv[y,x][0]

    isrec = isRec(reg.image)
    flag = False
    for c in cols:
        if abs(hue - c) < 0.1:
            if(isrec):
                if c not in rectangles:
                    rectangles[c] = 0
                rectangles[c] += 1
                flag = True
                break
            else:
                if c not in circles:
                    circles[c] = 0
                circles[c] += 1
                flag = True
                break
    if not flag:
        errorCount += 1

print("Cycles:")
print(circles)
print("Rectangles:")
print(rectangles)
print("Whatever:")
print(errorCount)

