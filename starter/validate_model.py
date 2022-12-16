import logging
from joblib import load
from .ml.model import compute_score_per_slice
from starter.ml.model import inference
from starter.train_model import get_train_test_data
from starter.ml.data import process_data
from starter.inference_model import run_inference

def val_model(test_df, cat_features, root_dir):
    """
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
    
    #_, test_data = get_train_test_data(root_path)
    
    
    
    """x_test, y_test, encoder, lb = process_data(
        train, categorical_features=cat_features, label="salary", training=False
    )
    
    
    
    preds = inference(trained_model, x_test)"""

    #preds = run_inference(test_data, cat_features)
    
    #logging.info("Overall score check procedure started")
    #compute_model_metrics(y_test, preds)
    
    #logging.info("Slice score check procedure started")
    compute_score_per_slice(
        trained_model,
        test_df,
        encoder,
        lb,
        cat_features,
        root_dir)
           
def val_overall_model(root_path, cat_features):
     _, test_data = get_train_test_data(root_path)
     y_test, preds = run_inference(test_data, cat_features, root_path)
     return y, preds
     
     
