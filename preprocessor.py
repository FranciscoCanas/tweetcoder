import sys
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer


if __name__=="__main__":
	if sys.argv>2:
		print "Useage: python preprocessor <tweetfile> <outputfile>"
		sys.exit()

	infile = open(sys.argv[1],'r')
	outfile = open(sys.argv[2],'w')
	corpus_list = construct_corpus_list(infile,2000)

	infile.close()
	outfile.close()

def construct_corpus_list(input_file, size):
	'''
	Given some input file containing a body of text, contructs
	a dictionary (list, actually ) of the  most-frequently used 
	words containing 'size' number of entries.
	Removes stopwords by default.
	'''
	tokenizer = RegexpTokenizer(r'\w+')

	body = tokenizer.tokenize(input_file.read())
	all_words = nltk.FreqDist(w.lower() for w in body \
		if w.lower() not in stopwords.words('english'))
	corpus_list = all_words.keys()[:size]
	return corpus_list



def vectorize_bagofwords(infile, outfile):
	'''
	Takes a file containing bodies of text separated by a
	line return. 
	Uses the "bag of words" technique to vectorize each body
	of txt in the input_file. 
	Ouputs vectors to text file.
	'''


	#for txt in infile:
		# 	


def vectorize_percharacter(infile, outfile, vector_length):
	'''
	Takes a file containing bodies of text separated by a
	line return. 
	The output vector represents the type of character found at
	each position in the body of text. 
	Ouputs vectors to text file.
	'''	

	#for txt in infile:
		# 	



