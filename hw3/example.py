import nltk
test_grammar = nltk.CFG.fromstring("""
	S -> NP VP
	PP -> P NP
	NP -> Det N | Det N PP | 'I'
	VP -> V NP | VP PP
	Det -> 'an' | 'my'
	N -> 'elephant' | 'pajamas'
	V -> 'shot'
	P -> 'in'
	""")

sent = ['I', 'shot', 'an', 'elephant', 'in', 'my', 'pajamas']
parser = nltk.ChartParser(test_grammar)
for tree in parser.parse(sent):
	print(tree)
