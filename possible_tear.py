# Initialize
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from skimage.morphology import erosion
from skimage.transform import downscale_local_mean
import cv2
import os

path = '/home/zachr/tear_mask/249_samples/0/0046'
os.chdir(path)
files = os.listdir(path)

possibly_torn = np.zeros((60,1),dtype=np.uint8)
means = np.zeros((60,1))
stds = np.zeros((60,1))
for i in range(1,60):
    im = cv2.imread(files[i],0)
    im = downscale_local_mean(im,(5,5))
    for j in range(1,8):
        im = erosion(im)
    im = cv2.GaussianBlur(im,(5,5),0)
    imarray = np.array(im)
    means[i] = imarray.mean()
    stds[i] = imarray.std()
possibly_torn[means + stds > 150] = 1
for z in range(1,len(possibly_torn)):
    if possibly_torn[z] ==1:
        print z





