import abc
import argparse
from xgboost import XGBRegressor
from settings import *
import pandas as pd 
from sklearn.model_selection import train_test_split
from  sklearn.metrics import mean_squared_error
import numpy as np 
import pickle 


args = abc.abstractproperty()



def parse_args():
    parser = argparse.ArgumentParser(
        description='Model training scripts')
    parser.add_argument('--save-model', action='store_true')


def train(model_name, save):
    data = pd.read_csv(os.path.join(DATA_PROCESSED, ''))
    
    if model_name == '': 
        model = model()


    model.fit(X_train)

    

    with open(os.path.join(LOG_DIR,"log.txt")) as file: 

        file.write(f'{model_name}')

    if save:
        pickle.dump(model, open(os.path.join('model.pkl'), 'wb'))





if __name__ == "__main__":
    global_args = parse_args()
    args.save_model = global_args.save_model

    if args.save_model == True:
        #function to save the model
        pass

