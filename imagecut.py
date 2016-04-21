import Image
import string
import sys

if len(sys.argv)<=1:
	print "exit"
	exit()
print "reading ", sys.argv[1]
im = Image.open(sys.argv[1]+".tif")
print im.format, im.size, im.mode
box = open(sys.argv[1]+".box")
box_str = box.readline().split()
for w in box_str:
	ch = unicode(w,'utf-8')
	print ch


