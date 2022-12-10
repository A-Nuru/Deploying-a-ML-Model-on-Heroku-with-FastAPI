import os
import yaml
import uvicorn
from fastapi import FastAPI
from pandas import DataFrame
from schema import ModelInput
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
        
@app.post("/inference")
async def inference(input_data: ModelInput):

    input_data = input_data.dict()
    print(input_data)
    change_keys = config['infer']['update_keys']
    columns = config['infer']['columns']
    cat_features = config['data']['cat_features']

    for new_key, old_key in change_keys:
        input_data[new_key] = input_data.pop(old_key)
    print(input_data)
    input_df = DataFrame(data=input_data.values(), index=input_data.keys()).T
    input_df = input_df[columns]

    prediction = run_inference(input_df, cat_features)

    return {"prediction": prediction}
        
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
     
