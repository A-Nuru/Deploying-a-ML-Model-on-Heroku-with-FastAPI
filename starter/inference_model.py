from joblib import load
from .ml.data import process_data
from .ml.model import inference


def run_inference(data, cat_features, root_dir):
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
    """model = load("model/model.joblib")
    encoder = load("model/encoder.joblib")
    lb = load("model/lb.joblib")"""
    
    trained_model = load(f"{root_dir}/model/model.joblib")
    encoder = load(f"{root_dir}/model/encoder.joblib")
    lb = load(f"{root_dir}/model/lb.joblib")

    X,_, _, _ = process_data(
        data,
        categorical_features=cat_features,
        encoder=encoder, lb=lb, training=False)

    pred = inference(trained_model, X)
    prediction = lb.inverse_transform(pred)[0]
    print(pred)
    print(prediction)

    return prediction
