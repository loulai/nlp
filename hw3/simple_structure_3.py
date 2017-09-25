import nltk
simple_grammar_2 = nltk.CFG.fromstring("""
	VP -> VBP PP
	PP -> VBP NP
	NP -> DT NN NN
	VBP -> 'are'
	VBP -> 'in'
	DT -> 'the'
	NN -> 'border' | 'region'
	""")

simple_sentence_2 = ['are', 'in', 'the', 'border', 'region']
parser = nltk.ChartParser(simple_grammar_2)
for tree in parser.parse(simple_sentence_2):
	print(tree)
