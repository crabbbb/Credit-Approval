import streamlit as st
import joblib
import numpy as np 
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder, MinMaxScaler, LabelEncoder
from scipy.stats import zscore
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
import xgboost as xgb
from sklearn.metrics import *
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV, StratifiedKFold
import pickle

# due to the fitting problem cannot be skip, at here will create a custom pipeline by accessing 3 value as parameter 
class ModelPipeline:
    
    def __init__(self, encoder_path, scaler_path, model_path):
        # load the encoder, scaler and model by using joblib
        self.encoder = joblib.load(encoder_path)
        self.scaler = joblib.load(scaler_path)
        self.model = joblib.load(model_path)
    
    def predict(self, input_data):
        # due to input data is in dictionary type so need to do convert
        df = pd.DataFrame([input_data])
        
        # get the encode feature from encoder, to ensure consistency 
        categorical_columns = self.encoder.feature_names_in_

        # col that in int or float datatype
        continuous_columns = [col for col in df.columns if col not in categorical_columns]

        # encoder 
        df[categorical_columns] = self.encoder.transform(df[categorical_columns])

        # scaler
        x = df.values
        x_transform = self.scaler.transform(x)
        
        # model
        predictedY = self.model.predict(x_transform)
        
        return int(predictedY[0])