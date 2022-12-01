import os
from starter.ml.data import data_cleaning_stage
from starter.train_model import get_train_test_data, train_save_model
from starter.validate_model import val_model
from starter.inference_model import run_inference

def test_clean_data():
    data_cleaning_stage(root_path='./')

    assert os.path.isfile('./data/clean_census.csv')
 
def test_get_train_test_data():
    train_df, test_df = get_train_test_data(root_path='./')

    assert train_df.shape[0] > 0
    assert train_df.shape[1] == 12

    assert test_df.shape[0] > 0
    assert test_df.shape[1] == 12
    
def test_train_save_model(clean_data, cat_features):

    train_save_model(clean_data, cat_features, root_path='./')

    assert os.path.isfile("./model/model.joblib")
    assert os.path.isfile("./model/encoder.joblib")
    assert os.path.isfile("./model/lb.joblib")
    
def test_model(clean_data, cat_features):
    val_model(clean_data, cat_features, root_dir='./')

    assert os.path.isfile("./model/slice_output.txt")
    
def test_run_inference_low(inference_data_low, cat_features):
    prediction = run_inference(inference_data_low, cat_features)

    assert prediction == "<=50K"


def test_run_inference_high(inference_data_high, cat_features):
    prediction = run_inference(inference_data_high, cat_features)

    assert prediction == ">50K"

def test_get(client):
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == {"greeting": "Hello!"}
    
def test_post_high(client):
    request = client.post("/", json={'age': 33,
                                     'workclass': 'Private',
                                     'fnlgt': 149184,
                                     'education': 'HS-grad',
                                     'marital_status': 'Never-married',
                                     'occupation': 'Prof-specialty',
                                     'relationship': 'Not-in-family',
                                     'race': 'White',
                                     'sex': 'Male',
                                     'hoursPerWeek': 60,
                                     'nativeCountry': 'United-States'
                                     })
    assert request.status_code == 200
    assert request.json() == {"prediction": ">50K"}
    
def test_post_low(client):
    request = client.post("/", json={'age': 19,
                                     'workclass': 'Private',
                                     'fnlgt': 149184,
                                     'education': 'HS-grad',
                                     'marital_status': 'Never-married',
                                     'occupation': 'Prof-specialty',
                                     'relationship': 'Not-in-family',
                                     'race': 'White',
                                     'sex': 'Male',
                                     'hoursPerWeek': 60,
                                     'nativeCountry': 'United-States'
                                     })
    assert request.status_code == 200
    assert request.json() == {"prediction": "<=50K"}

def test_post_malformed(client):
    r = client.post("/", json={
        "age": "",
        "workclass": "Private",
        'fnlgt': 149184,
        "education": "Some-college",
        "maritalStatus": "",
        "occupation": "",
        "race": "Black",
        "sex": "Male",
        "hoursPerWeek": 60,
        "nativeCountry": "United-States"
    })
    assert r.status_code == 422    
