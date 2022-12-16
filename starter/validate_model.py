"""
Contains a function to validate the model
"""
import logging
from joblib import load
from .ml.model import compute_score_per_slice, write_model_metrics
from starter.ml.model import inference
from starter.train_model import get_train_test_data
from starter.ml.data import process_data
from starter.inference_model import run_inference

def val_model(test_df, cat_features, root_dir):
    """
    Validate the model overall and in slices
    Parameters
    ----------
    test_df
    cat_features
    root_dir
    Returns
    -------
    """
    # load model and encoder
    trained_model = load(f"{root_dir}/model/model.joblib")
    encoder = load(f"{root_dir}/model/encoder.joblib")
    lb = load(f"{root_dir}/model/lb.joblib")
     
    logging.info("Overall score check procedure started")
    write_model_metrics(trained_model, test_df, encoder,
                            lb, cat_features, root_dir)
    
    logging.info("Slice score check procedure started")
    compute_score_per_slice(
        trained_model,
        test_df,
        encoder,
        lb,
        cat_features,
        root_dir)
       
