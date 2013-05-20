import sys, os
sys.path.append("..")
from preprocessor import *

if __name__=="__main__":
	print os.getcwd()
	#test_file = open('../tests/testcorpus','r')
	test_file = open('../dumps/texts','r')
	corpus_dict = construct_corpus_list(test_file,2000)
	print "50 most used words: "
	print str(corpus_dict)
	test_file.close()
