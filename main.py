import os
import yaml
from fastapi import FastAPI
from pandas import DataFrame
from starter.inference_model import run_inference

if "DYNO" in os.environ and os.path.isdir(".dvc"):
    os.system("dvc config core.no_scm true")
    if os.system("dvc pull") != 0:
        exit("dvc pull failed")
    os.system("rm -r .dvc .apt/usr/lib/dvc")

with open('config.yaml') as f:
    config = yaml.load(f, Loader= yaml.FullLoader)

app = FastAPI()

@app.get("/")
async def get_items():
    return {"greeting": "Hello!"}
