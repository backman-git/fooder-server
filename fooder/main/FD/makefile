add:
	@python addFD_DB.py --RSID $(RSID) --ID $(ID) --gValue $(g) --bValue $(b)
analysis:
	@python analysisFD.py --ID $(ID) --RSID $(RSID) --queryPath ./queryPool --answerPath ./answerPool --featureFile ../DB/featureFD
	
voting:
	@python votingFD_DB.py --ID $(ID) --RSID $(RSID) --type $(t)