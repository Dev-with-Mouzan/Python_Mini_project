import imageio.v3 as iio
import pyfiglet
banner = pyfiglet.figlet_format("Gif Creater")
print(banner)
filenames = ['First_pic.png', 'Second_pic.png']#place all the image in the same folder

images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('final.gif', images, duration = 500, loop = 0)