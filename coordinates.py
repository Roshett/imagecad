import cv2
import numpy as np
from random import randint
import json

def middle(num1,num2, cf):
    num = ((num1 + num2) / 2) + cf
    return num

def tuples(A):
    try: return tuple(tuples(a) for a in A)
    except TypeError: return A

def coordHarris(name, blockSize, kSize, k):
	blockSize = int(blockSize)
	kSize = int(kSize)
	k = float(k)
	name = name.split('/')
	filename = './static/src/assets/img/' + name[-1]
	img = cv2.imread(filename)
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	gray = np.float32(gray)
	dst = cv2.cornerHarris(gray,blockSize,kSize,k)
	ret, dst = cv2.threshold(dst,0.1*dst.max(),255,0)
	dst = np.uint8(dst)
	ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)
	criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.02)
	corners = cv2.cornerSubPix(gray,np.float32(centroids),(9,9),(-5,-5),criteria)
	img[dst>0.1*dst.max()]=[0,0,255]
	hashId = randint(1000, 9000)
	cv2.imwrite('./static/src/assets/img/bp_'+ str(hashId) + name[-1],img)

	# for x
	for corner in corners:

	    for pl_corner in corners:

	        if(corner[0] + 6 > pl_corner[0] and corner[0] - 6 < pl_corner[0]):

	            coef = (corner[0] + pl_corner[0]) / 2
	            corner[0] = coef
	            pl_corner[0] = coef

	# for y
	for corner in corners:

	    for pl_corner in corners:

	        if(corner[1] + 6 > pl_corner[1] and corner[1] - 6 < pl_corner[1]):

	            coef = (corner[1] + pl_corner[1]) / 2
	            corner[1] = coef
	            pl_corner[1] = coef

	#on the same line
	#for corner in corners:

	#    for pl_corner in corners:

	lines = []

	for b in range(-3,3):
	    for i in range(1, len(corners)):
	        corner = (corners[i])
	        for j in range(i+1, len(corners)):
	            x = int(round(middle(corner[0],corners[j][0],b)))
	            y = int(round(middle(corner[1],corners[j][1],b)))
	            x1 = int(round(middle(corner[0],x,b)))
	            y1 = int(round(middle(corner[1],y,b)))
	            x2 = int(round(middle(x,corners[j][0],b)))
	            y2 = int(round(middle(y,corners[j][1],b)))
	            if(img[y][x][2] != 0 and img[y1][x1][2] != 0 and img[y2][x2][2] != 0):
	                x1 = int(round(corner[0]))
	                y1 = int(round(corner[1]))
	                x2 = int(round(corners[j][0]))
	                y2 = int(round(corners[j][1]))
	                lines.append([x1,y1,x2,y2])

	b = set(tuples(lines))
	print(len(b))

	l = []
	for z in range(0, len(b)):
		l.append(b.pop())

	data = json.dumps({'lines' : l})
	print(data)
	file = open("data.json", "w")
	file.write(data) 
	file.close()


	return './src/assets/img/bp_'+ str(hashId) + name[-1]