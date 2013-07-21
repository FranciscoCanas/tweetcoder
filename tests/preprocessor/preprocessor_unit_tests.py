import sys, os
import unittest
from unittest import TestCase 
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
		
		self.w2 = ["cows","monsters","eat","the","terrible","coffee","table","cows",
				"cows","sandwich","sandwich","the","terrible","television","cars"]	
		self.wf2 = nltk.FreqDist(self.w2)
		return
	
	def test_construct_all_words(self):
		"""
		Test construct_all_words.
		"""
		body = construct_all_words("testbody")
		print body
		#TODO: Come up with some assertions for this here.
		return

	def test_bag_of_words(self):
		"""
		Test bag of words vectorization.
		"""
		body = [
			["d","c","b"],
			["a","a","e","f"],
			["g","a","e"]
			]
		dict_list = construct_dict_list(self.word_freq,3)
		vec = bag_of_words(body[0], dict_list)
		print vec 
		#TODO: Come up with some assertions for this here.
		return
	
	def test_construct_dict_list(self):
		"""
		Test construct_dict_list.
		Note: creates dict list using default language,
		ie english. "a" is a stop word in english!
		"""
		a = []
		
		dict_list = construct_dict_list(self.word_freq,3)
		
		print dict_list
		assert "a" not in dict_list
		assert "c" in dict_list
		assert "e" in dict_list
		assert "f" in dict_list
		
		print construct_dict_list(self.wf2,4)
		
		return
	
	def test_stemmer(self):
		a = ["running", "run","standing", "ate", "created"]
		
		# note: stemmers aren't perfect, hence "creat"
		expected = ["run", "stand","ate", "creat"]
		
		b = word_stemmer(a)
		print b
		self.assertItemsEqual(b,expected)
		
		 
	
if __name__ == '__main__':
    unittest.main()
    