import sys, os
sys.path.append("../../src/preprocessor")
from preprocessor import *

if __name__=="__main__":
	print os.getcwd()
	test_file ='../../dumps/500texts'
	all_words = construct_all_words(test_file)
	n = len(all_words)
	print str(n) + " unique words found: "
	print str(all_words)
	print
	

	corpus_dict = construct_dict_list(all_words,500)
	n = len(corpus_dict)
	print str(n) + " most used words: "
	print str(corpus_dict)

	tweet_file = '../../dumps/500texts'
	out_file = '../../dumps/500bag_vectorized'
	bag = vectorize_bag_of_words(tweet_file,out_file,corpus_dict)
	
	


