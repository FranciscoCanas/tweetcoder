import cPickle
import sys
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import argparse

VERBOSE=False

def construct_all_words(input_file):
	'''
	Given some input file containing a body of text, constructs 
	a list of all unique words.
	'''
	tokenizer = RegexpTokenizer(r'\w+')
	with open(input_file, 'r') as input:
		body = tokenizer.tokenize(input.read())

	all_words = nltk.FreqDist(w.lower() for w in body)
	return all_words.keys()

def construct_corpus_list(word_list, size=2000):
	'''
	Given some input file containing a body of text, contructs
	a dictionary (list, actually ) of the  most-frequently used 
	words containing 'size' number of entries.
	Removes stopwords by default.
	'''
	if VERBOSE:
		print "Constructing Corpus Dictionary:"
	non_stop_words = []
	for w in word_list:
		if VERBOSE:
			sys.stdout.write('.')
		if w not in stopwords.words('english'):
			non_stop_words.append(w)
	corpus_list = non_stop_words[:size]
	if VERBOSE:
		sys.stdout.write('\n')

	if VERBOSE:
		print "Corpus Dictionary:"
		print corpus_list
	return corpus_list


def bag_of_words(body, corpus):
	'''
	Return a list of the frequency of the words from corpus found
	in body.
	'''
	freq = nltk.FreqDist(body)
	return [freq[word] for word in corpus]


def vectorize_bag_of_words(infile, target_file, corpus):
	'''
	Takes a file containing bodies of text separated by a
	line return. 
	Uses the "bag of words" technique to vectorize each body
	of txt in the input_file. 
	Dumps pickled vectors to target_file.
	'''
	count = 0
	if VERBOSE:
		print "Vectorizing:"
	
	out = []
	with open(infile, 'r') as input:	
		for body in input:
			count += 1
			out.append(bag_of_words(body,corpus))
			#outfile.write(str(bag_of_words(body, corpus)) + '\n')
			if VERBOSE:
				sys.stdout.write('.')
	
	# open the target file and dump that pickle
	print target_file
	with open(target_file, 'wb') as of:
		cPickle.dump(out,of)
		
	if VERBOSE:
		print
		print "Vectorized {} text bodies.".format(count)
		


def vectorize_percharacter(infile, outfile, vector_length):
	'''
	Takes a file containing bodies of text separated by a
	line return. 
	The output vector represents the type of character found at
	each position in the body of text. 
	Ouputs vectors to text file.
	'''	
	return 


if __name__=="__main__":
	parser = argparse.ArgumentParser(
		description="Converts bodies of text from the input file into a line-separated set of vectors.")
	parser.add_argument("-v", "--verbose", 
		help="Display progress on terminal.",
		action="store_true")
	parser.add_argument("-o", "--output", choices=["bag","char"],
		default="bag",
		help="The type of vectorization to use: [bag] of words, or per-[char]acter.")
	parser.add_argument("-d", "--dictsize", default=200, type=int,
		help="Length of output vectors and corpus dictionary.")
	parser.add_argument("inputfile",
		help="File containing line-separated text bodies.")
	parser.add_argument("outputfile",
		help="A path to the output file.")
	parser.add_argument("dictfile",
		help="A file containing the body of text to construct corpus dictionary from.")

	args=parser.parse_args()

	VERBOSE = args.verbose

	
	
	all_words=construct_all_words(args.dictfile)
	N = len(all_words)
	if VERBOSE:
		print "Found {} unique words.".format(N)

	corpus_list = construct_corpus_list(all_words,args.dictsize)
	
	if (args.output=="char"):
		vectorize_percharacter(args.inputfile, args.outputfile, corpus_list)
	else:
		vectorize_bag_of_words(args.inputfile, args.outputfile, corpus_list)

	
