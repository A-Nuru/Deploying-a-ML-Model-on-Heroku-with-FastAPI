# Script to train machine learning model.
import pandas as pd
from joblib import dump
from .ml.data import process_data
from .ml.model import train_model
from sklearn.model_selection import train_test_split

# Optional enhancement: will use K-fold cross validation instead of a train-test split later.
def get_train_test_data(root_path):
    """
    Load clean data and split data into training and testing sets
    Parameters
    ----------
    root_path
    Returns
    -------
    train_df , test_df
    """
    data = pd.read_csv(f"{root_path}/data/clean/census.csv")
    train_df, test_df = train_test_split(data, test_size=0.20)

    return train_df, test_df

cat_features = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country",
]
