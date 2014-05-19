#!/bin/bash

##
## Resize JPG images 
##
## Uses the convert program from http://www.imagemagick.org
##

## find images in folder
for i in `find . -name "*.JPG"`; do 

echo "Converting $i"
convert $i -resize 50% -quality 95 $(dirname $i)/$(basename $i .JPG)_small.JPG; 

done
