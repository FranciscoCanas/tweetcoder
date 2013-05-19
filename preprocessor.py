import sys
import nltk

if "__name__"=="__main__":
	if sys.argv>2:
		print "Useage: python preprocessor <tweetfile> <outputfile>"
		sys.exit()


def vectorize_bagofwords(input_file_name, output_file_name):
	'''
	Takes a file containing bodies of text separated by a
	line return. 
	Uses the "bag of words" technique to vectorize each body
	of txt in the input_file. 
	Ouputs vectors to text file.
	'''

	infile = open(input_file_name,'r')
	outfile = open(output_file_name,'w')

	#for txt in infile:
		# 	


def vectorize_percharacter(input_file_name, output_file_name, vector_length):
	'''
	Takes a file containing bodies of text separated by a
	line return. 
	The output vector represents the type of character found at
	each position in the body of text. 
	Ouputs vectors to text file.
	'''	
	infile = open(input_file_name,'r')
	outfile = open(output_file_name,'w')

	#for txt in infile:
		# 	



