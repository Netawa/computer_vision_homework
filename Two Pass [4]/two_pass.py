import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.misc import face
from skimage.measure import regionprops, label
import random

def check(image, y, x):
	if not 0 <= x < image.shape[1]:
		return False
	if not 0 <= y <= image.shape[0]:
		return False
	if image[y,x] != 0:
		return True
	return False

def neighbours2(image, y, x):
	left = y, x - 1
	top = y - 1, x
	if not check(image, *left):
		left = None
	if not check(image, *top):
		top = None
	return left,top
def find(label, linked):
	j = label
	while linked[j] != 0:
		j = linked[j]
	return j

def union(label1,label2,linked):
	j = find(label1,linked)
	k = find(label2, linked)
	if j != k:
		linked[k] = j

def two_pass_labeling(binary_image):
	labeled = np.zeros_like(binary_image)
	label = 1
	linked = np.zeros(len(binary_image), dtype="uint")
	for y in range(binary_image.shape[0]):
		for x in range(binary_image.shape[1]):
			if binary_image[y,x] != 0:
				ns = neighbours2(binary_image, y, x)
				if ns[0] is None and ns[1] is None:
					m = label
					label += 1
				else:
					lbs = [labeled[i] for i in ns if i is not None]
					m = min(lbs)
				labeled[y, x] = m
				for n in ns:
					if n is not None:
						lb = labeled[n]
						if lb != m:
							union(m,lb,linked)
	for y in range(binary_image.shape[0]):
		for x in range(binary_image.shape[1]):
			if binary_image[y,x] != 0:
				new_label = find(labeled[y,x], linked)
				if new_label != labeled[y,x]:
					labeled[y ,x] = new_label
	ar = []
	for y in range(binary_image.shape[0]):
		for x in range(binary_image.shape[1]):
			if not (labeled[y ,x] in ar) and labeled[y ,x] != 0:
				ar.append(labeled[y ,x])
	for y in range(binary_image.shape[0]):
		for x in range(binary_image.shape[1]):
			if labeled[y ,x] != 0:
				labeled[y ,x] = ar.index(labeled[y ,x])+1
	return labeled

B = np.zeros((20, 20), dtype='int32')

B[1:-1, -2] = 1

B[1, 1:5] = 1
B[1, 7:12] = 1
B[2, 1:3] = 1
B[2, 6:8] = 1
B[3:4, 1:7] = 1

B[7:11, 11] = 1
B[7:11, 14] = 1
B[10:15, 10:15] = 1

B[5:10, 5] = 1
B[5:10, 6] = 1

lab = two_pass_labeling(B)
count = len(list(set(lab.ravel()))[1:])
print(count)
print(list(set(lab.ravel()))[1:])

plt.figure(figsize=(12, 5))
plt.subplot(121)
plt.imshow(B, cmap="hot")
plt.colorbar(ticks=range(int(2)))
plt.axis("off")
plt.subplot(122)
plt.imshow(lab.astype("uint8"), cmap="hot")
plt.colorbar()
plt.axis("off")
plt.tight_layout()
plt.show()

