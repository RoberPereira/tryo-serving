import cloudpickle
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn import set_config
set_config(transform_output="pandas")


# Class to select only the features needed for training
class FeatureSelector(BaseEstimator, TransformerMixin):
    def __init__(self, features):
        self.features = features

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X[self.features]


class CustomNumericImputer(BaseEstimator, TransformerMixin):
    def __init__(self, features, strategy_map):
        self.features = features
        self.strategy_map = strategy_map
        self.imputers = {}

        for feature, strategy in strategy_map.items():
            if isinstance(strategy, (int, float)):
                self.imputers[feature] = SimpleImputer(strategy='constant', fill_value=strategy)
            else:
                self.imputers[feature] = SimpleImputer(strategy=strategy)

    def fit(self, X, y=None):

        for feature, imputer in self.imputers.items():
            if feature not in self.features:
                continue
            imputer.fit(X[[feature]])
        return self

    def transform(self, X):
        X_transformed = X.copy()
        for feature, imputer in self.imputers.items():
            if feature not in self.features:
                continue
            X_transformed[feature] = imputer.transform(X[[feature]])
        return X_transformed


def save_pipeline(name, pipeline, features):
    with open(f'{name}.pkl', 'wb') as f:
        cloudpickle.dump({'pipeline': pipeline, 'features': features}, f)
