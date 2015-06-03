from PIL import Image
import ImageFilter
import numpy
import scipy
from scipy import ndimage
from skimage import data
from skimage import filter

im = Image.open('car.jpg').convert('L')
im.save('greyscale.jpg')
#im=im.convert('1');
th=150
im = im.point(lambda i: i < th and 255)
im.show()
im = scipy.misc.imread('greyscale.jpg')
im = im.astype('int32')
dx = ndimage.sobel(im, 0)  # horizontal derivative
dy = ndimage.sobel(im, 1)  # vertical derivative
mag = numpy.hypot(dx, dy)  # magnitude
mag *= 255.0 / numpy.max(mag)  # normalize (Q&D)
scipy.misc.imsave('sobel.jpg', mag)
im = Image.open("sobel.jpg")

im.show();


