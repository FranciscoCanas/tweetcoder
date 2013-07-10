import sys, os
import unittest
sys.path.append("../../src/preprocessor")
from preprocessor import *
import nltk


class preprocessor_unit_tests(unittest.TestCase):
	word_list = []
	
	def setUp(self):
		"""
		Any code to run before each test.
		"""
		self.word_list = ["a","b","c","d","e","a","c","a","e", "f","f"]
		self.word_freq = nltk.FreqDist(self.word_list)	
		return
	
	def test_construct_all_words(self):
		"""
		Test construct_all_words.
		"""
		return

	def test_bag_of_words(self):
		"""
		Test bag of words vectorization.
		"""
		return
	
	def test_construct_dict_list(self):
		"""
		Test construct_dict_list.
		Note: creates dict list using default language,
		ie english. "a" is a stop word in english!
		"""
		dict_list = construct_dict_list(self.word_freq,3)
		
		print dict_list
		assert "a" not in dict_list
		assert "c" in dict_list
		assert "e" in dict_list
		assert "f" in dict_list
		return
	
if __name__ == '__main__':
    unittest.main()
    