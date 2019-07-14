# height or width

import cv2
import numpy as np
from math import sqrt, fabs

def middle(num1,num2):
    num = (num1 + num2) / 2
    return int(round(num))  


# filename = './testData/img/bp_3690bg1_two.png'
filename = './testData/img/dashed_line.png'
img = cv2.imread(filename)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv2.cornerHarris(gray,5,5,0.01)
ret, dst = cv2.threshold(dst,0.1*dst.max(),255,0)
dst = np.uint8(dst)
ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
corners = cv2.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)

# print(corners)

coefPoints = 1.3
# for x
for corner in corners:

    for pl_corner in corners:

        if(corner[0] + coefPoints > pl_corner[0] and corner[0] - coefPoints < pl_corner[0]):

            coef = (corner[0] + pl_corner[0]) / 2
            corner[0] = coef
            pl_corner[0] = coef

# for y
for corner in corners:

    for pl_corner in corners:

        if(corner[1] + coefPoints > pl_corner[1] and corner[1] - coefPoints < pl_corner[1]):

            coef = (corner[1] + pl_corner[1]) / 2
            corner[1] = coef
            pl_corner[1] = coef

spaces = []
# print(corners)

for corner in corners:
    for pl_corner in corners:
        x = fabs(corner[0] - pl_corner[0])
        y = fabs(corner[1] - pl_corner[1])
        lenghtVector = sqrt(fabs(x*x + y*y))
        
        mid_x = middle(corner[0], pl_corner[0])
        mix_y = middle(corner[1], pl_corner[1])
        space = img[mix_y][mid_x][0]

        if(fabs(lenghtVector) > 3 and fabs(lenghtVector) < 15 and space == 0):
            #print(lenghtVector)
            spaces.append([corner[0], corner[1], pl_corner[0], pl_corner[1]])

for space in spaces:
    cv2.line(img,(space[0],space[1]),(space[2],space[3]),(255,255,255),4)


# img[dst>0.1*dst.max()]=[0,0,255]
cv2.imwrite('img.png',img)