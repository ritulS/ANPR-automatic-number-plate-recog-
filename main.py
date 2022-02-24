import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import cv2
from tqdm import tqdm
import os
import glob
import os


for dirname, _, filenames in os.walk(r'C:\Users\Ritul\Documents\Python Scripts\IML_Final_project\input'):
    # print('here')
    for filename in filenames:
        print(os.path.join(dirname, filename))
        break
    break




img_size = 200
img_dir = r"C:\Users\Ritul\Documents\Python Scripts\IML_Final_project\input\images" # Enter Directory of all images 
data_path = os.path.join(img_dir,'*g')
files = glob.glob(data_path)
files.sort() 

imgs=[]
print(imgs)

# resizing all images
print('Resizing images....')
for f in tqdm(files):
    img = cv2.imread(f)
    img = cv2.resize(img, (img_size,img_size))
    imgs.append(np.array(img))
print('Resizing Complete!')
print(np.array(imgs).shape)


#Function for Extracting resized bounding box annotations from xml files
from lxml import etree
def bboxannotation(f):
    tree = etree.parse(f)
    for dim in tree.xpath("size"):
        width = int(dim.xpath("width")[0].text)
        height = int(dim.xpath("height")[0].text)
    for dim in tree.xpath("object/bndbox"):
        x_low = int(dim.xpath("xmin")[0].text)/(width/img_size)
        y_low = int(dim.xpath("ymin")[0].text)/(height/img_size)
        x_high = int(dim.xpath("xmax")[0].text)/(width/img_size)
        y_high = int(dim.xpath("ymax")[0].text)/(height/img_size)
    return [int(x_high), int(y_high), int(x_low), int(y_low)]


path = 'input/annotations'
path_f = path + '/'
img_annotations = [path_f + i for i in sorted(os.listdir(path))]
#array to store bounding box annotations
bbox = []

print('Extracting bounding box annotations....')
for i in img_annotations:
    bbox.append(bboxannotation(i))
print('bounding box annotations extracted!')

print(bbox[0])

image = cv2.rectangle(imgs[0],(bbox[0][0],bbox[0][1]),(bbox[0][2],bbox[0][3]),(0, 0, 255))
plt.imshow(image)
plt.show()


# Using a Haarcascade classifier to localize plates in image