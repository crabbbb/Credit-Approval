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
import ModelPipeline


# load pipeline to execute encoder, scaler and model
pipeline = joblib.load('pklFolder\pipeline.pkl')

# Dropdown list options 
A4 = ['u', 'y', 'l']
A5 = ['g', 'p', 'gg']
A6 = ['w', 'q', 'm', 'r', 'cc', 'k', 'c', 'd', 'x', 'i', 'e', 'aa', 'ff', 'j']
A9 = ['t', 'f']
A10 = ['t', 'f']
A13 = ['g', 's', 'p']

def predict(response) : 
    # pipeline
    return pipeline.predict(response)


def main() :
    # Title 
    st.title("Credit Approval Prediction")

    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Credict Approval App </h2>
    </div>
    """
    
    response = {
        'A2' : np.nan,
        'A3' : np.nan,
        'A4' : '',
        'A5' : '',
        'A6' : '',
        'A8' : np.nan,
        'A9' : '',
        'A10' : '',
        'A11' : np.nan,
        'A13' : '',
        'A14' : np.nan,
        'A15' : np.nan
    }

    ## A2 
    numberA2 = st.number_input("Enter value for A2 > ", min_value=0)

    # Display the entered number
    st.write(f"A2 > {numberA2}")

    response['A2'] = numberA2

    ## A3
    numberA3 = st.number_input("Enter value for A3 > ", min_value=0)

    # Display the entered number
    st.write(f"A3 > {numberA3}")

    response['A3'] = numberA3

    ## A4
    # Creating the dropdown list
    optionA4 = st.selectbox("Choose an option for A4 > ", A4)

    # Display the selected option
    st.write(f"A4 > {optionA4}")

    response['A4'] = optionA4

    ## A5
    # Creating the dropdown list
    optionA5 = st.selectbox("Choose an option for A5 > ", A5)

    # Display the selected option
    st.write(f"A5 > {optionA5}")

    response['A5'] = optionA5

    ## A6
    # Creating the dropdown list
    optionA6 = st.selectbox("Choose an option for A6 > ", A6)

    # Display the selected option
    st.write(f"A6 > {optionA6}")

    response['A6'] = optionA6

    ## A8
    numberA8 = st.number_input("Enter value for A8 > ", min_value=0)

    # Display the entered number
    st.write(f"A8 > {numberA8}")

    response['A8'] = numberA8

    ## A9
    # Creating the dropdown list
    optionA9 = st.selectbox("Choose an option for A9 > ", A9)

    # Display the selected option
    st.write(f"A9 > {optionA9}")

    response['A9'] = optionA9

    ## A10
    # Creating the dropdown list
    optionA10 = st.selectbox("Choose an option for A10 > ", A10)

    # Display the selected option
    st.write(f"A10 > {optionA10}")

    response['A10'] = optionA10

    ## A11
    numberA11 = st.number_input("Enter value for A11 > ", min_value=0)

    # Display the entered number
    st.write(f"A11 > {numberA11}")

    response['A11'] = numberA11

    ## A13
    # Creating the dropdown list
    optionA13 = st.selectbox("Choose an option for A13 > ", A13)

    # Display the selected option
    st.write(f"A13 > {optionA13}")

    response['A13'] = optionA13

    ## A14
    numberA14 = st.number_input("Enter value for A14 > ", min_value=0)

    # Display the entered number
    st.write(f"A14 > {numberA14}")

    response['A14'] = numberA14

    ## A15
    numberA15 = st.number_input("Enter value for A15 > ", min_value=0)

    # Display the entered number
    st.write(f"A15 > {numberA15}")

    response['A15'] = numberA15

    # create a button - this button name "Predict"
    if st.button("Predict"):
        result = predict(response=response) # when click will run this function 
        
    st.success('The output is {}'.format(result)) 


if __name__=='__main__':
    main()

