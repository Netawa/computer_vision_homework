import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.misc import face
from skimage.measure import regionprops
from skimage import color

def counting(image):
	count = [0, 0, 0, 0, 0, 0]
	for y in range(0, image.shape[0], 2):
		for x in range(0, image.shape[1], 2):
			if image[y,x] == 1:
				c = n8sum(image, y, x, mult = 2)
				if c == 4:
					if zero(image, y-2,x) == 0:
						count[0] += 1
					if zero(image, y,x-2) == 0:
						count[1] += 1
					if zero(image, y+2,x) == 0:
						count[2] += 1
					if zero(image, y,x+2) == 0:
						count[3] += 1
				if c == 5:
					if zero(image, y+2,x) + zero(image, y-2,x)  == 1:
						count[4] += 1
					if zero(image, y,x-2) + zero(image, y,x+2)  == 1:
						count[5] += 1
	ar = np.array([[1,0,1],[1,1,1]])
	ar2 = np.array([[1,1,1],[1,1,1]])
	for i in range(len(count) - 2):
		print(ar)
		print(count[i])
		ar = np.rot90(ar)
	for i in range(4, len(count)):
		print(ar2)
		print(int(count[i]/2))
		ar2 = np.rot90(ar2)
	
def n8sum(image, y, x, mult = 1):
	return (zero(image, y-mult, x) + zero(image, y+mult, x) + zero(image, y, x-mult) + zero(image, y, x+mult) + zero(image, y-mult, x-mult) + zero(image, y+mult, x+mult) + zero(image, y+mult, x-mult) + zero(image, y-mult, x+mult))

def zero(image, y, x):
	if(y >= 0 and x >= 0 and y < image.shape[0] and x < image.shape[1]):
		if image[y,x] == 1:
			return 1
	return 0

image = np.load("ps.npy").astype("uint")
counting(image)
plt.figure(figsize=(6, 6))
plt.imshow(image)
plt.show()