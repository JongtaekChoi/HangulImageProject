#!/bin/bash
#
#
# Make training image for hangul recognition
# It uses tesseract training tools.

echo "make image"


echo "$# parameters"
echo "$@";

echo "making font image and box file"
for p in $*;
do
	echo "make image with fond $p"
	text2image --text=hangul_complete.txt --outputbase=hangul.$p --fonts_dir=./ --font=$p true --ptsize 50 
	
done


