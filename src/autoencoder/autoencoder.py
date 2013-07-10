import numpy
import theano
import theano.tensor as T
import deeplearning.rbm

class Autoencoder(object):
    """
    Multi-layered autoencoder built by stacking RBMs.
    """
    
    rbms = []
    
    def __init__(self, rbm_size_list):
        """
        Initialize the autoencoder by creating a sequence of RBMs, each of 
        input size as specified by the rbm_size_list.
        """

        for i in xrange(rbm_size_list):
            # construct the RBM class
            rbm = RBM(input=x, 
                      n_visible=rbm_size_list[i] * 28,
                      n_hidden=n_hidden, 
                      numpy_rng=rng, 
                      theano_rng=theano_rng)
            rbms.append(rbm)
            
            
        
    
    
    
    def train_autoencoder(datafile, v_in_size, v_out_size):
        """
        Given the path to a datafile containing vectors of v_in_size,
        this function will train the autoencoder to produce output
        vectors of v_out_size.
        """
        
        return
        
    def data_file_to_matrix(datafile):
        """
        Given the data file, this function will return a matrix
        of sample data.
        """
        
        return
    
    def train_layer(rbm, training_data):
        """
        Given an RBM object and some training data in a matrix,
        train the RBM and update its weights.
        """
        
        return 