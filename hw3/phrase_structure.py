import nltk
my_grammar = nltk.CFG.fromstring("""
	S -> NP VP
	NP -> NNS | NP PP | DT JJ NNS IN | DT NN | DT NN NN
	VP -> NBP SBAR | VBP PP
	SBAR -> IN S
	PP -> IN NP
	NNS -> 'Scientists' | 'areas'
	NN -> 'planet' | 'border' | 'region'
	VBP -> 'think' | 'are'
	IN -> 'in' | 'on' | 'that'
	DT -> 'any' | 'the'
	JJ -> 'habitable'
	""")

sentence = ['Scientists', 'think', 'that', 'any', 'habitable', 'areas', 'on', 'the', 'planet', 'are', 'in', 'the', 'border', 'region']
parser = nltk.ChartParser(my_grammar)
for tree in parser.parse(sentence):
	print(tree)
