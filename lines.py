from PIL import Image
from PIL import ImageDraw
from PIL import ImageFilter
import math, random, sys

#things you can change
movement = 600           #change the slant of the line
min_val = 0               #change the minimum line size
max_val = 100             #change the maximum line size
correct_size = (1440,900) #the ouput size of the picture
scale = 2                 #the upscale of the picture to process


if len(sys.argv) == 3:
	pic_1 = sys.argv[1]
	pic_2 = sys.argv[2]
	output = 'output.png'
elif len(sys.argv) == 4:
	pic_1 = sys.argv[1]
	pic_2 = sys.argv[2]
	output = sys.argv[3]
else:
	print "arguements should be file_locations"
	sys.exit()


background_im = Image.open(pic_1).resize((correct_size[0]*scale,correct_size[1]*scale), Image.ANTIALIAS)
overlay_im = Image.open(pic_2).resize((correct_size[0]*scale,correct_size[1]*scale), Image.ANTIALIAS)
im = Image.new("RGB",background_im.size,"white")
image_size = im.size
drw = ImageDraw.Draw(im, 'RGB')
a = min(0,-movement)
size = 0
while a < image_size[0] + abs(movement):
	points = [(a,0),
		(a+movement,image_size[1]),
		(a+movement+size,image_size[1]),
		(a+size,0)]
	drw.polygon(points,(0,0,0))
	add = random.randint(min_val,max_val)
	a += add + size
	size = random.randint(min_val,max_val)
pix = im.load()
npix = background_im.load()
opix = overlay_im.load()
for a in range(im.size[0]):
	for b in range(im.size[1]):
		c = pix[a,b]
		if c == (0,0,0):
			pix[a,b] = opix[a,b]
		else:
			pix[a,b] = npix[a,b]
im.resize((im.size[0]/scale,im.size[1]/scale), Image.ANTIALIAS).save(output)