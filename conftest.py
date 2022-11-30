import pytest
import pandas as pd
import yaml
from starter.ml.data import clean_dataset


@pytest.fixture
def raw_data():
    """
    Get dataset
    """
    df = pd.read_csv("data/census.csv", skipinitialspace=True)

    return df
    
@pytest.fixture
def clean_data(raw_data):
    """
    Get dataset
    """
    df = clean_dataset(raw_data)
    return df

@pytest.fixture
def cat_features():
    """
    Get dataset
    """
    with open('config.yaml') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)

    return config['data']['cat_features']
    
