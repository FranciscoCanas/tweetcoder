import cPickle
import sys
import nltk
from nltk.corpus import stopwords
from nltk.corpus import words
from nltk.tokenize import RegexpTokenizer
import argparse

VERBOSE=False
LANG='english'
SIZE = 2000

def construct_all_words(input_file):
	'''
	Given some input file containing a body of text, constructs 
	a frequency distribution list of all stemmed and unique words.
	'''
	tokenizer = RegexpTokenizer(r'\w+')
	with open(input_file, 'r') as input:
		body = tokenizer.tokenize(input.read())

	# Stem the body of words first:
	body = word_stemmer(body)
	all_words = nltk.FreqDist(w.lower() for w in body)
	return all_words.keys()

def construct_dict_list(word_freq,SIZE):
	'''
	Given a freq dist of words in list form, contructs
	a dictionary (list, actually ) of the  most-frequently used 
	words containing 'size' number of entries.
	Removes stopwords by default.
	'''
	if VERBOSE:
		print "Constructing Dictionary:"
		
	non_stop_words = []

	for w in word_freq:
		if VERBOSE:
			sys.stdout.write('.')
		if w not in stopwords.words(LANG):
			non_stop_words.append(w)
	dict_list = non_stop_words[:SIZE]
	if VERBOSE:
		sys.stdout.write('\n')

	if VERBOSE:
		print "Corpus Dictionary:"
		print dict_list
	return dict_list


def bag_of_words(body, dictionary):
	'''
	Return a list of the frequency of the words from dictionary found
	in body.
	''' 
	# stem the words first:
	body = word_stemmer(body)
	
	# get a frequency distribution for this body of words
	freq = nltk.FreqDist(body)

	# for each word in body, the frequency that the word appears
	# if and only if that word is also in the dict 
	vec = [freq[word] for word in dictionary]
	if VERBOSE:
		print vec
	
	return vec


def vectorize_bag_of_words(infile, target_file, dictionary):
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
			body = word_list(body)
			out.append(bag_of_words(body,dictionary))
			
			if VERBOSE:
				sys.stdout.write('.')
	
	# open the target file and dump that pickle
	print target_file
	with open(target_file, 'wb') as of:
		cPickle.dump(out,of)
		
	if VERBOSE:
		print
		print "Vectorized {} text bodies.".format(count)
		

def word_stemmer(word_list):
	'''
	Takes a list of words as input, returns a list of the
	words' stems.
	'''
	stemmer = nltk.PorterStemmer()
	stemmed_word_set = set(map(stemmer.stem, word_list))
	stemmed_word_list = list(stemmed_word_set)
	
	return stemmed_word_list

def word_list(body):
	'''
	Given a body of text as a string, constructs a list
	of words from it.
	'''
	tokenizer = RegexpTokenizer(r'\w+')
	return tokenizer.tokenize(body)
	

def vectorize_percharacter(infile, outfile, vector_length):
	'''
	Takes a file containing bodies of text separated by a
	line return. 
	The output vector represents the type of character found at
	each position in the body of text. 
	Outputs vectors to text file.
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
	parser.add_argument("-l", "--lang", choices=["english","spanish"],
					default="english",
					help="Language: english|spanish")
	parser.add_argument("inputfile",
		help="File containing line-separated text bodies.")
	parser.add_argument("outputfile",
		help="A path to the output file.")
	parser.add_argument("dictfile",
		default=None,
		help="A file containing the body of text to construct corpus dictionary from.")
	
	args=parser.parse_args()

	VERBOSE = args.verbose
	LANG = args.lang
	SIZE = args.dictsize
	
	
	all_words=construct_all_words(args.dictfile)
	N = len(all_words)
	if VERBOSE:
		print "Found {} unique words.".format(N)

	dict_list = construct_dict_list(all_words,SIZE)
	print dict_list
	
	if (args.output=="char"):
		vectorize_percharacter(args.inputfile, args.outputfile, dict_list)
	else:
		vectorize_bag_of_words(args.inputfile, args.outputfile, dict_list)

	
