import os
from starter.ml.data import data_cleaning_stage
from starter.train_model import get_train_test_data, train_save_model

def test_clean_data():
    data_cleaning_stage(root_path='./')

    assert os.path.isfile('./data/clean_census.csv')
    
