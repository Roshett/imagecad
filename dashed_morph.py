import cv2 as cv2
import numpy as np
from math import sqrt, fabs

def middle(num1,num2):
    num = (num1 + num2) / 2
    return int(round(num))  

def tuples(A):
    try: return tuple(tuples(a) for a in A)
    except TypeError: return A


# filename = './testData/img/bp_3690bg1_two.png'
# filename = './testData/img/dashed_line.png'
filename = './testData/img/dl_two.png'
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

coefPoints = 3


#for X
for corner in corners:
    all_store = []
    for pl_corner in corners:

        if(corner[0] + coefPoints > pl_corner[0] and corner[0] - coefPoints < pl_corner[0]):
            all_store.append(pl_corner)

    a = all_store[0][0]
    b = all_store[0][0]

    for item in all_store:    

        if(a > item[0]):
            a = item[0] 

        if(b < item[0]):
            b = item[0]       

    middle = (a + b) / 2

    for corner in corners:
        for item in all_store:
            if(corner[0] == item[0] and corner[1] == item[1]):
                corner[0] = middle

#for X
for corner in corners:
    all_store = []
    for pl_corner in corners:

        if(corner[1] + coefPoints > pl_corner[1] and corner[1] - coefPoints < pl_corner[1]):
            all_store.append(pl_corner)

    a = all_store[0][1]
    b = all_store[0][1]

    for item in all_store:    

        if(a > item[1]):
            a = item[1] 

        if(b < item[1]):
            b = item[1]       

    middle = (a + b) / 2

    for corner in corners:
        for item in all_store:
            if(corner[0] == item[0] and corner[1] == item[1]):
                corner[1] = middle



for corner in corners:
    print(corner)


# for item in all_store:
    # print(item)
# print(len(all_store))



# # for x
# for corner in corners:

#     for pl_corner in corners:

#         if(corner[0] + coefPoints > pl_corner[0] and corner[0] - coefPoints < pl_corner[0]):

#             coef = (corner[0] + pl_corner[0]) / 2
#             corner[0] = coef

# # for y
# for corner in corners:

#     for pl_corner in corners:

#         if(corner[1] + coefPoints > pl_corner[1] and corner[1] - coefPoints < pl_corner[1]):

#             coef = (corner[1] + pl_corner[1]) / 2
#             corner[1] = coef

# print(corners)
# counter = 0
# clear_arr = []
# for corner in corners:
#     counter = counter + 1
#     for i in range(counter, len(corners)):
#         # print(corners[i][0])
#         if (corner[0] == corners[i][0] and corner[1] == corners[i][1]):
#             print('Some!')

img[dst>0.1*dst.max()]=[0,0,255]
cv2.imwrite('imgM.png',img)


