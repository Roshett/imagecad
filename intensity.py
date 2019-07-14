import cv2
import numpy as np
from random import randint

def deleteNoices(name, intensity):
    name = str(name)
    intensity = int(intensity)
    blueprint = cv2.imread('./static/src/assets/img/' + name, cv2.COLOR_BGR2GRAY)
    low_black = (0,0,0)
    high_black = (intensity,intensity,intensity)
    only_blueprint = cv2.inRange(blueprint, low_black, high_black)
    hashId = randint(1000, 9000)
    cv2.imwrite('./static/src/assets/img/bp_'+ str(hashId) + name,only_blueprint)
    return str(hashId)