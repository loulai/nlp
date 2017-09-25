import nltk
simple_grammar_2 = nltk.CFG.fromstring("""
	S -> NP VP
	NP -> NP PP | DT JJ NNS PP | DT NN NN
	PP -> IN DT NN | VBP NP
	DT -> 'any' | 'the'
	JJ -> 'habitable'
	NNS -> 'areas'
	IN -> 'on'
	NN -> 'planet' | 'border' | 'region'

	VP -> VBP PP
	VBP -> 'are' | 'in'
	""")

simple_sentence_2 = ['any', 'habitable', 'areas', 'on','the','planet','are', 'in', 'the', 'border', 'region']
parser = nltk.ChartParser(simple_grammar_2)
for tree in parser.parse(simple_sentence_2):
	print(tree)
