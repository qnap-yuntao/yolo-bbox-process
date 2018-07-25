# Convert From Ratio to Pixel_Val
import os
import matplotlib.pyplot as plt
from PIL import Image
import cv2

def convert(size,file):
    box = ''
    with open (file,'r') as f:
        for line in f:
            elems = line.split(' ')       
            [cls_id, x, y, w, h] = [int(elems[0]), float(elems[1]), float(elems[2]), float(elems[3]), float(elems[4])]
            w_px = w * size[0]
            h_px = h * size[1]
            c_x = x * size[0]
            c_y = y * size[1]
            xmin = c_x - w_px/2.0
            ymin = c_y - h_px/2.0
            xmax = c_x + w_px/2.0
            ymax = c_y + h_px/2.0
            box += str(cls_id)+' ' + str(xmin).split('.')[0] + ' ' + str(ymin).split('.')[0] + ' ' + str(xmax).split('.')[0] + ' ' + str(ymax).split('.')[0] + '\n'
        with open('/Users/wenkai/Desktop/conver_to_BBOX_val/{}'.format(file_name),'w') as out_txt:
            out_txt.write(box)

path1 = '/Users/wenkai/Desktop/BBox-Label-Tool/convert_to_yolo/'
path2 = '/Users/wenkai/Desktop/BBox-Label-Tool-py3/Images/001'

for file_name in os.listdir(path1): 
    if file_name.startswith('.'):
        continue
    input_img = file_name[:-4] + '.JPEG'
    img_path = os.path.join(path2, input_img)
    img = cv2.imread(img_path)
    height, width, channels = img.shape
    size = (width, height)
    file = os.path.join(path1, file_name)
    convert(size,file)