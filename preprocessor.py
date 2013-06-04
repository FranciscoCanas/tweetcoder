import sys
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

def construct_all_words(input_file):
	'''
	Given some input file containing a body of text, constructs 
	a list of all unique words.
	'''
	tokenizer = RegexpTokenizer(r'\w+')

	body = tokenizer.tokenize(input_file.read())
	all_words = nltk.FreqDist(w.lower() for w in body)
	return all_words.keys()

def construct_corpus_list(word_list, size=2000):
	'''
	Given some input file containing a body of text, contructs
	a dictionary (list, actually ) of the  most-frequently used 
	words containing 'size' number of entries.
	Removes stopwords by default.
	'''
	print "Constructing Corpus Dictionary:"
	non_stop_words = []
	for w in word_list:
		sys.stdout.write('.')
		if w not in stopwords.words('english'):
			non_stop_words.append(w)
	corpus_list = non_stop_words[:size]
	sys.stdout.write('\n')
	return corpus_list


def bag_of_words(body, corpus):
	'''
	Return a list of the frequency of the words from corpus found
	in body.
	'''
	freq = nltk.FreqDist(body)
	return [freq[word] for word in corpus]


def vectorize_bag_of_words(infile, outfile, corpus):
	'''
	Takes a file containing bodies of text separated by a
	line return. 
	Uses the "bag of words" technique to vectorize each body
	of txt in the input_file. 
	Ouputs vectors to text file.
	'''
	print "Vectorizing:"
	for body in infile:
		sys.stdout.write('.')
		outfile.write(str(bag_of_words(body, corpus)) + '\n')
	sys.stdout.write('\n')


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
	if len(sys.argv)!=4:
		print len(sys.argv)
		print "Useage: python preprocessor <tweetfile> <outputfile> <dictionaryfile>"
		sys.exit()

	infile = open(sys.argv[1],'r')
	outfile = open(sys.argv[2],'w')
	dictfile = open(sys.argv[3],'r')
	corpus_list = construct_corpus_list(dictfile)
	vectorize_bag_of_words(infile, outfile, corpus_list)
	infile.close()
	outfile.close()
	dictfile.close()


