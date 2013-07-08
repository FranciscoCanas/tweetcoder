#tweetcoder
==========
Alexander Biggs
Francisco Canas
Sasa Milics

## What be this?
A very work-in-progress twitter trends visualization device using autoencoders.

## What does this need? 

NLTK python lib -- www.nltk.org
	Install with:
	pip install nltk

Theano -- http://deeplearning.net/software/theano/
	I recommend following the easy installation instructions here for your particular brand of operating system:
	http://deeplearning.net/software/theano/install.html#install

Note that Theano has its own set of dependencies as outlined in the install guide linked to above, including:

NumPy -- http://www.numpy.org/
SciPy -- http://scipy.org/

## What are these files?
src/jtotext.py -- Script used to produce plain text, line-return separated list of tweet text from a json file dumped by the db we are using. 

src/preprocessory.py -- Script used to extract feature vectors from a file containing the body text from tweets. Will use two separate and mutually exclusive methods: "Bag of Words" and "per Character" feature extraction. 

src/autoencoder/autoencoder.py -- The main code file for the autoencoder. This file will contain the code that trains RBMs, links them together, and encodes input vectors into tinier input vectors. 

src/autoencoder/deeplearning/rbm.py -- The Restricted Boltzmann Machine class that is a building block for the autoencoder.


