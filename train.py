import hydra
import logging
from starter.ml.data import data_cleaning_stage, process_data
from starter.train_model import get_train_test_data, train_save_model
from starter.validate_model import val_model
from omegaconf import DictConfig
from starter.ml.model import compute_model_metrics
#from starter.validate_model import val_overall_model
from starter.inference_model import run_inference
from joblib import load

_steps = [
    "data_cleaning",
    "train_model",
    "check_score",
    ]

@hydra.main(config_name="config.yaml", config_path="./")
def go(config: DictConfig):
    """
    Run pipeline stages
    """
    logging.basicConfig(level=logging.INFO)
    root_path = hydra.utils.get_original_cwd()
    # Steps to execute
    steps_par = config['main']['steps']
    active_steps = steps_par.split(",") if steps_par != "all" else _steps
    cat_features = config['data']['cat_features']

    if "data_cleaning" in active_steps:
        logging.info("Cleaning and saving clean data")
        data_cleaning_stage(root_path)
        
    train_df, test_df = get_train_test_data(root_path)
    
    if "train_model" in active_steps:
        logging.info("Train/Test model procedure started")
        train_save_model(train_df, cat_features, root_path)
        print("done")
    if "check_score" in active_steps:
        logging.info("Score check procedure started")
        val_model(test_df, cat_features, root_path)
        print("done")
       
if __name__ == "__main__":
    """
    Main entrypoint
    """
    go()
     
