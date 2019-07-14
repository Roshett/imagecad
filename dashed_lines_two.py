import cv2
import numpy as np
from math import sqrt, fabs

def lineCoord(x1, y1, x2, y2, x):
    A = y1 - y2
    B = x2 - x1
    C = x1 * y2 - x2 * y1
    y = (-C - (A * x)) / B
    return [x, y]





filename = './testData/img/dashed_line.png'
img = cv2.imread(filename)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv2.cornerHarris(gray,5,3,0.01)
ret, dst = cv2.threshold(dst,0.1*dst.max(),255,0)
dst = np.uint8(dst)
ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
corners = cv2.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)


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
#print(corners)

for corner in corners:
    for pl_corner in corners:
        x = fabs(corner[0] - pl_corner[0])
        y = fabs(corner[1] - pl_corner[1])
        lenghtVector = sqrt(fabs(x*x + y*y))  
        if(fabs(lenghtVector) > 8 and fabs(lenghtVector) < 15):
            #print(lenghtVector)
            spaces.append([corner[0], corner[1], pl_corner[0], pl_corner[1]])


#print(spaces)
#for space in spaces:
#    print(space)
    #cv2.line(img,(space[0],space[1]),(space[2],space[3]),(255,255,255),4)
#print(spaces[0])
space = spaces[0]
print(space)
data = lineCoord(space[0], space[1], space[2], space[3], 21.437)
print(data)



#img[dst>0.1*dst.max()]=[0,0,255]
cv2.imwrite('img_two.png',img)