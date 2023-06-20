import cv2
import numpy as np
import matplotlib.pyplot as plt 
import cvlib as cv
from cvlib.object_detection import draw_bbox
from numpy.lib.polynomial import poly

image = cv2.imread("Cats and Fruits.jpg")
box, label, count = cv.detect_common_objects(image)
output = draw_bbox(image, box, label, count)
output = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
plt.imshow(output)
plt.show()
frequencies = {'cat': 0, 'apple': 0, 'orange': 0}
objects = ['cat', 'apple', 'orange']
for obj in objects:
    frequencies[obj] = label.count(obj)
print(frequencies)
