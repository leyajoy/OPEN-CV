
//we need to install opencv

! pip install opencv-python

import cv2
import matplotlib.pyplot as plt
import numpy as np

//upload an image using the upload icon and copy path and paste it for reading 

image = cv2.imread("./photo-1503023345310-bd7c1de61c7d.jpeg")

//the following command is to know the type of image

type(image)

//the below command gives the height , width and number of channels of the image

image.shape

//below command is for plotting the uploaded image

plt.imshow(image)

// following command is for changing the colour of image from RGB(red, green, blue) to BGR(blue, green, red) and named it as new_image and plotted it.

new_image = cv2.cvtColor(image , cv2.COLOR_RGB2BGR)

plt.imshow(new_image)

//for splitting image 

"""
1. Splitting image channels
"""
r,g,b =cv2.split(new_image)
print('r', r.shape)
print('g', g.shape)
print('b', b.shape)

//for merging splitted image

"""print('r', r.shape)
print('g', g.shape)
print('b', b.shape)"""
new_image = cv2.merge((r,g,b))

//for changing dimensions

s = 10
w = int(new_image.shape[1]*s/100)
h = int(new_image.shape[0]*s/100)
dim = (w,h)
re_size = cv2.resize(new_image ,dim ,interpolation = cv2.INTER_AREA)
re_size.shape

//for rotating

"""
3. rotate operation
"""
(h,w) = new_image.shape[:2]
c = (w/2,h/2)
angle = 90
m = cv2.getRotationMatrix2D(c, angle, 1.0)
rotate_90 = cv2.warpAffine(new_image, m, (h,w))

//for plotting rotated image

plt.imshow(rotate_90)

//for plotting resized image

plt.imshow(re_size)
