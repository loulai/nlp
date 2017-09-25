import nltk
simple_grammar_2 = nltk.CFG.fromstring("""
	NP -> NP PP
	NP -> DT JJ NNS PP
	PP -> IN DT NN
	DT -> 'any' | 'the'
	JJ -> 'habitable'
	NNS -> 'areas'
	IN -> 'on'
	NN -> 'planet'
	""")

simple_sentence_2 = ['any', 'habitable', 'areas', 'on','the','planet']
parser = nltk.ChartParser(simple_grammar_2)
for tree in parser.parse(simple_sentence_2):
	print(tree)
