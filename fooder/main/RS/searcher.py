# import the necessary packages
import numpy as np
import cv2
import pickle 
class Searcher:
	def __init__(self, indexPath,filesArray):
		# store our index path
		self.indexPath = indexPath
		self.filesArray = filesArray
 
	def search(self, queryFeatures, limit = 10):
		# initialize our dictionary of results
		results = {}
		
		indexList=[]
		
		#load multiple files
		for file in self.filesArray:
			infile = open(self.indexPath+'/'+file+'.csv','rb')
			while 1:
				try:
					indexList = pickle.load(infile)
					features = indexList[1]
				
					d = self.similarity(features, queryFeatures)
				
					results[indexList[0]] = d
			
				except(EOFError,pickle.UnpicklingError):
					break
		
			infile.close()
		
		
		
		
 
		# sort our results, so that the smaller distances (i.e. the
		# more relevant images are at the front of the list)
		results = sorted([(v, k) for (k, v) in results.items()], reverse=True)
		# return our (limited) results
		return results[:limit]
		
		
	def similarity(self, f1,f2):
		totalD=0
		
		for hist1,hist2 in zip(f1,f2):
			totalD+=cv2.compareHist(hist1,hist2,0 )
			
		return totalD