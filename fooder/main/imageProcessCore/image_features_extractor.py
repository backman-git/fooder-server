# import the necessary packages
from colordescriptor import colorDescriptor
import argparse

import cv2
import pickle

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()

#possible calculate in mobile 
ap.add_argument("-id","--identity", required= True,help ="process id");

ap.add_argument("-d", "--imgPath", required = True,help = "Path to the directory that contains the images to be indexed")

ap.add_argument("-r", "--resultPath", required = True,help = "Path to the directory that contains csv")


	
	
args = vars(ap.parse_args())
 
# initialize the color descriptor
cd = colorDescriptor((8, 12, 3))

with open(args['resultPath']+"/"+args["identity"]+'.csv','wb') as f:

	#define image format, now is jpg
	imagePath = args["imgPath"]+"/"+args["identity"]+".jpg";
	imageID = imagePath[imagePath.rfind("/") + 1:]
	image = cv2.imread(imagePath)
	features = cd.describe(image)
	outList=[]
	outList.append(imageID)
	outList.append(features)
	pickle.dump(outList, f)
	
	f.close()
	

	
	
