tweetcoder
==========

Alexander Biggs
Francisco Canas
Sasa Milics

Dependencies: 
NLTK python lib -- www.nltk.org
Install with:
pip install nltk

A twitter trends visualization device using neural network auto-encoders!

jtotext.py -- Script used to produce plain text, line-return separated list of tweet text from a json file dumped by the db.

preprocessory.py -- Script used to extract feature vectors from a file containing the body text from tweets. Will use two separate and mutually exclusive methods: "Bag of Words" and "per Character" feature extraction. 
