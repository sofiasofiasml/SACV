from scipy.fftpack import dct, idct
from skimage.io import imread, imsave
from skimage.color import rgb2gray
import numpy as np
import matplotlib.pylab as plt

im = rgb2gray(imread('rain.jpg'))
im2= np.float32(im)/255
imF = dct(im2.T, norm='ortho').T
im_dct = np.uint8(imF)*255
imCompress = idct(np.float32(imF).T, norm='ortho').T
plt.gray()
plt.imshow(imCompress)
plt.show()


