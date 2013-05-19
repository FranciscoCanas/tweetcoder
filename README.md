tweetcoder
==========

Alexander Biggs
Francisco Canas
Sasa Milics

A twitter trends visualization device using neural network auto-encoders!

jtotext.py -- Script used to produce plain text, line-return separated list of tweet text from a json file.
preprocessor.py -- A class that transforms a twitter text body into a feature vector suitable for training the auto-encoder.

preprocessory.py -- Script used to extract feature vectors from a file containing the body text from tweets. Will use two separate and mutually exclusive methods: "Bag of Words" and "per Character" feature extraction. 
