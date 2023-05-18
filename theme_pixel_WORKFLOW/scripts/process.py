
from settings import *
import pandas as pd 
import abc
import argparse
args = abc.abstractproperty()


def process(data):
    

#def parse_args():
    parser = argparse.ArgumentParser(
        description='Model  scripts')
    args = parser.parse_args()
    return args



if __name__ == "__main__":
    global_args = parse_args()
    args.train = global_args.train
    args.test = global_args.test

    if args.raw:
        process('RawData')
   


 











