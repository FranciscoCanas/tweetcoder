import sys, os
sys.path.append("..")
from preprocessor import *

if __name__=="__main__":
	print os.getcwd()
	test_file = open('../dumps/texts','r')
	all_words = construct_all_words(test_file)
	n = len(all_words)
	print str(n) + " unique words found: "
	print str(all_words)
	print
	test_file.close()

	corpus_dict = construct_corpus_list(all_words,500)
	n = len(corpus_dict)
	print str(n) + " most used words: "
	print str(corpus_dict)
	test_file.close()

	tweet_file = open('../dumps/texts','r')
	out_file = open('../dumps/bag_vectorized','w')
	bag = vectorize_bag_of_words(tweet_file,out_file,corpus_dict)
	tweet_file.close()
	out_file.close()


