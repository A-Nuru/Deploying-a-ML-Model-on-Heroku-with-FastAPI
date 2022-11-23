import hydra
import logging
from starter.ml.data import data_cleaning_stage
from starter.train_model import get_train_test_data
from omegaconf import DictConfig

_steps = [
    "data_cleaning",
]


@hydra.main(config_name="config.yaml")
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
    print('done')
        
if __name__ == "__main__":
    """
    Main entrypoint
    """
    go()
     
