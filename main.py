from fastapi import FastAPI
from fastapi.responses import JSONResponse
import cloudpickle
import pandas as pd
import numpy as np
from typing import Dict, Any
import custom_preprocessor


app = FastAPI()


with open('preprocessing_pipeline.pkl', 'rb') as f:
    preprocessing_pipeline = cloudpickle.load(f)

with open('model_pipeline.pkl', 'rb') as f:
    model_pipeline = cloudpickle.load(f)


@app.get("/health", status_code=200)
def health():
    return {'health': 'ok'}


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/predict")
def predict(data: Dict[str, Any]):

    df = pd.DataFrame([data])
    df = df.where(pd.notnull(df), np.nan)

    pre_pipeline = preprocessing_pipeline['pipeline']
    required_features = preprocessing_pipeline['features']
    model = model_pipeline['pipeline']
    model_features = model_pipeline['features']

    missing_features = [col for col in required_features
                        if col not in data.keys()]

    if (len(missing_features) > 0):
        return JSONResponse(content={"missing features": missing_features})

    preprocessed_data = pre_pipeline.transform(df[required_features])
    df = pd.DataFrame(preprocessed_data, columns=model_features)
    prediction = model.predict(df)

    return JSONResponse(content={"prediction": prediction.tolist()[0]})



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
