import Image
import string
import sys

if len(sys.argv)<=1:
	print "exit"
	exit()
print "reading ", sys.argv[1]
im = Image.open(sys.argv[1]+".tif")
height = int(im.size[1])
print height
box_file = open(sys.argv[1]+".box")
while True :
	box_str = box_file.readline().split()
	if len(box_str)<5:
		break
	box =[int(box_str[1]), int(box_str[4]), int(box_str[3]), int(box_str[2]) ]
	box[1] = height-box[1]
	box[3] = height-box[3]
	print box[1], box[3]
	region = im.crop(box)
	name = unicode(box_str[0],'utf-8')
	if name[0]>'z': 
		region.save( sys.argv[1]+"."+name+".png", "PNG")
		print "save "+name
	else :
		print "Cannot save "+name
print "done"


