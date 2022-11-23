import hydra
import logging
from omegaconf import DictConfig


@hydra.main(config_name="config.yml")
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
                   
if __name__ == "__main__":
    """
    Main entrypoint
    """
    go()
     
