"""
Contains a function to make batch or single prediction and
write predictioss into a file 
"""
from joblib import load
from .ml.data import process_data
from .ml.model import inference
import logging

def run_inference(data, cat_features):
    """
    Load model and run inference
    Parameters
    ----------
    root_path
    data
    cat_features
    Returns
    -------
    prediction
    """ 
    
    model = load("model/model.joblib")
    encoder = load("model/encoder.joblib")
    lb = load("model/lb.joblib")

    X, _, _, _ = process_data(
        data,
        categorical_features=cat_features,
        encoder=encoder, lb=lb, training=False)

    pred = inference(model, X)
    prediction = lb.inverse_transform(pred)[0]

    return prediction
   
    
    
    """trained_model = load(f"{root_dir}/model/model.joblib")
    encoder = load(f"{root_dir}/model/encoder.joblib")
    lb = load(f"{root_dir}/model/lb.joblib")

    with open(f'{root_dir}/model/predictions_output.txt', 'w') as file:
        X_test,y_test, _, _ = process_data(
	data,
	categorical_features=cat_features, label="salary",
	training=False, encoder=encoder, lb=lb) 
	
        pred = inference(trained_model, X_test)
        prediction = lb.inverse_transform(pred)[0]
        predictions = lb.inverse_transform(pred)
        predictions = "The test set predictions are %s" % (predictions)
        logging.info(predictions)
        file.write(predictions + '\n') 
        return prediction"""
