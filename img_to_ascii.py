
import numpy as np
import math 
from PIL import Image
import sys, random, argparse
# 70 levels of gray
gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "


def getAverageL(image):
	#get image as a numpy array
	img = np.array(image)
	# get dimensions
	w, h = img.shape
	#return average L value
	return np.average(img.reshape(w*h))


def convert(filename, cols, scale):
	#convert image to greyscale 
	image = Image.open(filename).convert('L')
	#get dimensions
	W, H = image.size[0], image.size[1]
	#Compute width of each tile
	w = W/cols
	#Compute height of each tile base on scale
	h = w/scale
	#Compute number of rows
	rows = int(H/h)
	aimg = []
	
	for j in range(rows):
		y1 = int(h*j)
		y2 = int(h*(j+1))

		if j == rows - 1:
			y2 = H

		aimg.append("")

		for i in range(cols):
			x1 = int(w * i)
			x2 = int(w * (i +1))

			if i == cols - 1:
				x2 = W

			im = image.crop(x1, y1, x2, y2)
			average = getAverageL(im)
			gsval = gscale1[int((avg*69)/255)]
			aimg[j]+= gsval

	return aimg



def main():
    # create parser
    descStr = "This program converts an image into ASCII art."
    parser = argparse.ArgumentParser(description=descStr)
    # add expected arguments
    parser.add_argument('--file', dest='imgFile', required=True)
    parser.add_argument('--scale', dest='scale', required=False)
    parser.add_argument('--out', dest='outFile', required=False)
    parser.add_argument('--cols', dest='cols', required=False)

    # parse args
    args = parser.parse_args()
  
    imgFile = args.imgFile
    # set output file
    outFile = 'out.txt'
    if args.outFile:
        outFile = args.outFile
    # set scale default as 0.43 which suits a Courier font
    scale = 0.43
    if args.scale:
        scale = float(args.scale)
    # set cols
    cols = 80
    if args.cols:
        cols = int(args.cols)

    print('generating ASCII art...')
    # convert image to ascii txt
    aimg = covertImageToAscii(imgFile, cols, scale)

    # open file
    f = open(outFile, 'w')
    # write to file
    for row in aimg:
        f.write(row + '\n')
    # cleanup
    f.close()
    print("ASCII art written to %s" % outFile)




if __name__ == "__main__":
	main()