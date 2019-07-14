import cv2
import numpy as np

# filename = './static/src/assets/img/' + name
path = './src/assets/img/bp_1703bp1_three.png'
# path = path[1:]
# filename = './static/' + path

# img = cv2.imread(filename)
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

path = path.split('/')
print(path[-1])
