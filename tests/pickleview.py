import sys, os
import cPickle
import argparse

if __name__=="__main__":
    parser = argparse.ArgumentParser(
        description="Converts pickled vector files to unicode and outputs to terminal for your viewing pleasure.")
    parser.add_argument("thefile",
        help="A file containing cPickled vectors.")

    args=parser.parse_args()

    with open(args.thefile, 'rb') as input:
        x = cPickle.load(input)
        
    for guy in x:
        print guy

