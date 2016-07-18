update:
	@python image_features_extractor.py --dataset dataset --identity $(id)
	@python addFooderDB.py --ID $(id) --long $(long) --lat $(lat) --gValue $(g) --bValue $(b)
	
	

find: 
	python search.py --ID $(id) --long $(lg) --lat $(la) --featureFile imgFeatureSet --query queryPool   --answerPath answerPool
	

voting:
	@python fooderVotingDB.py --ID $(ID) --type $(votingType)