import nltk
simple_grammar = nltk.CFG.fromstring("""
	S -> NP VP
	NP -> 'Scientists'
	VP -> 'think' SBAR
	SBAR -> 'that' S
	""")

simple_sentence = ['Scientists', 'think', 'that']
parser = nltk.ChartParser(simple_grammar)
for tree in parser.parse(simple_sentence):
	print(tree)
