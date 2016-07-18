add:
	@python addRS_DB.py --ID $(ID) --long $(long) --lat $(lat) --gValue $(g) --bValue $(b)
	
analysis:
	python analysisRS.py --ID $(ID) --long $(long) --lat $(lat) --featureFile ../DB/featureRS \
	--queryPath ./queryPool --answerPath ./answerPool --gpsOffset 10.0