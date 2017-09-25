import nltk
my_grammar = nltk.CFG.fromstring("""
	S -> NP VP
	VP -> VBP SBAR | VBP PP
	SBAR -> IN S
	NP -> NNS | NP PP | DT JJ NNS PP | DT NN NN
	PP -> IN DT NN | VBP NP
	
	VBP -> 'think' | 'are' | 'in'
	DT -> 'any' | 'the'
	JJ -> 'habitable'
	NNS -> 'Scientists'|'areas'
	NN -> 'planet' | 'border' | 'region'
	IN -> 'that'|'on'
	""")

sentence = ['Scientists', 'think', 'that', 'any', 'habitable', 'areas', 'on', 'the', 'planet', 'are', 'in', 'the', 'border', 'region']
parser = nltk.ChartParser(my_grammar)
for tree in parser.parse(sentence):
	print(tree)
