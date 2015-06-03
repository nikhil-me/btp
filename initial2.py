from PIL import Image 
#import ImageEnhance
import ImageFilter
#from scipy.misc import imsave #scipy.misc.imsave saves an array as an image
#image_file = Image.open("download.jpg") # open colour image
#image_file= image_file.convert('L') # convert image to monochrome - this works
#image_file= image_file.convert('1') # convert image to black and white
#imsave('result_col.jpg', image_file)
img = Image.open('download.jpg').convert('L')
img.save('greyscale.jpg')
#img.show();
#img=img.fliter(ImageFilter.FIND_EDGES)
img =img.Contrast(img,0)
img.save('edges.jpg')
img.show();

