
# TRYO-SERVING 

App for model serving on GCP

## Installation

Python version==3.11.5

Start virtual enviroment. [venv](https://docs.python.org/3/library/venv.html#venv-def)
```bash
python -m venv .venv
source .venv/bin/activate
```

Use pip-tools package manager to install project dependencies. [pip-tools](https://pip-tools.readthedocs.io/en/stable/)
```bash
python -m pip install pip-tools
```

To install dependencies from requirements.in run: 
```bash
pip-compile requirements.in
pip install -r requirements.txt

```

## Local Usage

Run our local server [uvicorn]( https://www.uvicorn.org/ )  
```bash
uvicorn main:app --reload
```

#### Predict Curl example
```bash
curl --location 'http://127.0.0.1:8000/predict' \
--header 'Content-Type: application/json' \
--data '{"Id": 582,
 "MSSubClass": 20,
 "MSZoning": "RL",
 "LotFrontage": 98.0,
 "LotArea": 12704,
 "Street": "Pave",
 "Alley": null,
 "LotShape": "Reg",
 "LandContour": "Lvl",
 "Utilities": "AllPub",
 "LotConfig": "Inside",
 "LandSlope": "Gtl",
 "Neighborhood": "NridgHt",
 "Condition1": "Norm",
 "Condition2": "Norm",
 "BldgType": "1Fam",
 "HouseStyle": "1Story",
 "OverallQual": 8,
 "OverallCond": 5,
 "YearBuilt": 2008,
 "YearRemodAdd": 2009,
 "RoofStyle": "Hip",
 "RoofMatl": "CompShg",
 "Exterior1st": "VinylSd",
 "Exterior2nd": "VinylSd",
 "MasVnrType": "BrkFace",
 "MasVnrArea": 306.0,
 "ExterQual": "Ex",
 "ExterCond": "TA",
 "Foundation": "PConc",
 "BsmtQual": "Ex",
 "BsmtCond": "TA",
 "BsmtExposure": "No",
 "BsmtFinType1": "Unf",
 "BsmtFinSF1": 0,
 "BsmtFinType2": "Unf",
 "BsmtFinSF2": 0,
 "BsmtUnfSF": 2042,
 "TotalBsmtSF": 2042,
 "Heating": "GasA",
 "HeatingQC": "Ex",
 "CentralAir": "Y",
 "Electrical": "SBrkr",
 "1stFlrSF": 2042,
 "2ndFlrSF": 0,
 "LowQualFinSF": 0,
 "GrLivArea": 2042,
 "BsmtFullBath": 0,
 "BsmtHalfBath": 0,
 "FullBath": 2,
 "HalfBath": 1,
 "BedroomAbvGr": 3,
 "KitchenAbvGr": 1,
 "KitchenQual": "Ex",
 "TotRmsAbvGrd": 8,
 "Functional": "Typ",
 "Fireplaces": 1,
 "FireplaceQu": "Gd",
 "GarageType": "Attchd",
 "GarageYrBlt": 2009.0,
 "GarageFinish": "RFn",
 "GarageCars": 3,
 "GarageArea": 1390,
 "GarageQual": "TA",
 "GarageCond": "TA",
 "PavedDrive": "Y",
 "WoodDeckSF": 0,
 "OpenPorchSF": 90,
 "EnclosedPorch": 0,
 "3SsnPorch": 0,
 "ScreenPorch": 0,
 "PoolArea": 0,
 "PoolQC": null,
 "Fence": null,
 "MiscFeature": null,
 "MiscVal": 0,
 "MoSold": 8,
 "YrSold": 2009,
 "SaleType": "New",
 "SaleCondition": "Partial",
 "SalePrice": 253293
 }'
```

## Remote Usage

### Deploy to Google Cloud

Install SDK  
https://cloud.google.com/sdk/docs/install?hl=es-419  

Compile and run service with SDK  
https://cloud.google.com/run/docs/quickstarts/build-and-deploy/python?hl=es-419

This app is containerized by docker for deployment defined in Dockerfile.  
https://www.docker.com/resources/what-container/

```bash
gcloud builds submit --config cloudbuild.yaml
```

#### Predict Curl example 
- Change server_url 

```bash
curl --location 'https://tryo-xgboost-kqhzywglqa-ew.a.run.app/predict' \
--header 'Content-Type: application/json' \
--data '{"Id": 582,
 "MSSubClass": 20,
 "MSZoning": "RL",
 "LotFrontage": 98.0,
 "LotArea": 12704,
 "Street": "Pave",
 "Alley": null,
 "LotShape": "Reg",
 "LandContour": "Lvl",
 "Utilities": "AllPub",
 "LotConfig": "Inside",
 "LandSlope": "Gtl",
 "Neighborhood": "NridgHt",
 "Condition1": "Norm",
 "Condition2": "Norm",
 "BldgType": "1Fam",
 "HouseStyle": "1Story",
 "OverallQual": 8,
 "OverallCond": 5,
 "YearBuilt": 2008,
 "YearRemodAdd": 2009,
 "RoofStyle": "Hip",
 "RoofMatl": "CompShg",
 "Exterior1st": "VinylSd",
 "Exterior2nd": "VinylSd",
 "MasVnrType": "BrkFace",
 "MasVnrArea": 306.0,
 "ExterQual": "Ex",
 "ExterCond": "TA",
 "Foundation": "PConc",
 "BsmtQual": "Ex",
 "BsmtCond": "TA",
 "BsmtExposure": "No",
 "BsmtFinType1": "Unf",
 "BsmtFinSF1": 0,
 "BsmtFinType2": "Unf",
 "BsmtFinSF2": 0,
 "BsmtUnfSF": 2042,
 "TotalBsmtSF": 2042,
 "Heating": "GasA",
 "HeatingQC": "Ex",
 "CentralAir": "Y",
 "Electrical": "SBrkr",
 "1stFlrSF": 2042,
 "2ndFlrSF": 0,
 "LowQualFinSF": 0,
 "GrLivArea": 2042,
 "BsmtFullBath": 0,
 "BsmtHalfBath": 0,
 "FullBath": 2,
 "HalfBath": 1,
 "BedroomAbvGr": 3,
 "KitchenAbvGr": 1,
 "KitchenQual": "Ex",
 "TotRmsAbvGrd": 8,
 "Functional": "Typ",
 "Fireplaces": 1,
 "FireplaceQu": "Gd",
 "GarageType": "Attchd",
 "GarageYrBlt": 2009.0,
 "GarageFinish": "RFn",
 "GarageCars": 3,
 "GarageArea": 1390,
 "GarageQual": "TA",
 "GarageCond": "TA",
 "PavedDrive": "Y",
 "WoodDeckSF": 0,
 "OpenPorchSF": 90,
 "EnclosedPorch": 0,
 "3SsnPorch": 0,
 "ScreenPorch": 0,
 "PoolArea": 0,
 "PoolQC": null,
 "Fence": null,
 "MiscFeature": null,
 "MiscVal": 0,
 "MoSold": 8,
 "YrSold": 2009,
 "SaleType": "New",
 "SaleCondition": "Partial",
 "SalePrice": 253293
 }'
```

## Project Structure
```bash
tree -d -I __pycache__
```
- main.py : project acces point. Defines fastApi application.
- custom_preprocessor : contains sklearn transform classes.
- model_pipeline.pkl : model pipeline.
- preprocessing_pipeline.pkl : preprocessing model pipeline.
- cloudbuild.yaml: steps for google cloud build

```
.
├── cloudbuild.yaml
├── custom_preprocessor.py
├── main.py
├── model_pipeline.pkl
└── preprocessing_pipeline.pkl
└── cloudbuild.yaml

```
