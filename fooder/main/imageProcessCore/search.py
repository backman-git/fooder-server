# import the necessary packaimport argparse
import cv2
import json
import argparse
from gpsSearcher import gpsSearcher
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()

ap.add_argument("-ID","--ID",required= True, help = "process ID")

ap.add_argument("-lg","--long",required= True, help = "longitude")
ap.add_argument("-la","--lat",required= True, help = "latitude")




ap.add_argument("-f", "--featureFile", required = True,
	help = "Path to where the computed feature files is stored")
	
	
ap.add_argument("-q", "--queryPath", required = True,help = "Path to the query image")
	
	
ap.add_argument("-a","--answerPath",required = True,help = "Path to the answer json file")

	
args = vars(ap.parse_args())


from colordescriptor import colorDescriptor
from searcher import Searcher


 
# initialize the image descriptor
cd = colorDescriptor((8, 12, 3))

# load the query image and describe it
query = cv2.imread(args["query"]+'/'+args["ID"]+'.jpg')
features = cd.describe(query)
 
gS = gpsSearcher(10)

dataList= gS.search(float(args['long']),float(args['lat']))
fooderList={}
for data in dataList:
	fooderList[str(data[0])+'.jpg']=data;



IDList =[]

for obj in dataList:
	IDList.append(str(obj[0]))
	
	
 
 
# perform the search
searcher = Searcher(args["featureFile"],IDList)
gS.close()
results = searcher.search(features)

# output index answer file
with open(args["answerPath"]+"\\"+args["ID"]+".json",'wb') as f:
# loop over the results
# should make more beautiful json format
	ansIndex={}
	
	i=0;
	ansIndex["status"]='true';
	ansIndex["numberOfImgs"]=len(results);
	for (score, imageName) in results:
		
		
		
		
		ansIndex[i]=(fooderList[imageName][0],fooderList[imageName][3],fooderList[imageName][4],fooderList[imageName][5],score)
		i+=1
		#should fixed!!
		
			
	tmp=json.dumps(ansIndex)
	print >>f, tmp
	f.close()
	print "- python: analysis finish!!";