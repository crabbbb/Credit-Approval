import streamlit as st
import joblib
from sklearn.preprocessing import OrdinalEncoder, MinMaxScaler
import numpy as np 

# load encoder, scaler and model 
encoder = joblib.load('pklFolder/encoder.pkl')
scaler = joblib.load('pklFolder/scaler.pkl')
model = joblib.load('pklFolder/model/LogisticRegression.pkl')

# Dropdown list options 
A4 = ['u', 'y', 'l']
A5 = ['g', 'p', 'gg']
A6 = ['w', 'q', 'm', 'r', 'cc', 'k', 'c', 'd', 'x', 'i', 'e', 'aa', 'ff', 'j']
A9 = ['t', 'f']
A10 = ['t', 'f']
A13 = ['g', 's', 'p']

def main() :
    # Title 
    st.title("Credit Approval Prediction")

    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Credict Approval App </h2>
    </div>
    """
    
    response = {
        'A2' : np.NAN,
        'A3' : np.NAN,
        'A4' : '',
        'A5' : '',
        'A6' : '',
        'A8' : np.NAN,
        'A9' : '',
        'A10' : '',
        'A11' : np.NAN,
        'A13' : '',
        'A14' : np.NAN,
        'A15' : np.NAN
    }

    ## A2 
    numberA2 = st.number_input("A2 > ", min_value=0)

    # Display the entered number
    st.write(f"You entered > {numberA2}")

    response['A2'] = numberA2

    ## A4
    # Creating the dropdown list
    optionA4 = st.selectbox("Choose an option", A4)

    # Display the selected option
    st.write(f"A4 > {optionA4}")

    response['A4'] = optionA4

    ## A5
    # Creating the dropdown list
    optionA5 = st.selectbox("Choose an option", A5)

    # Display the selected option
    st.write(f"A5: {optionA5}")

    response['A5'] = optionA5

    ## A6
    # Creating the dropdown list
    optionA6 = st.selectbox("Choose an option", A6)

    # Display the selected option
    st.write(f"A6: {optionA6}")

    response['A6'] = optionA6

    ## A9
    # Creating the dropdown list
    optionA9 = st.selectbox("Choose an option", A9)

    # Display the selected option
    st.write(f"A9: {optionA9}")

    response['A9'] = optionA9

    ## A10
    # Creating the dropdown list
    optionA10 = st.selectbox("Choose an option", A10)

    # Display the selected option
    st.write(f"A10: {optionA10}")

    response['A10'] = optionA10

    ## A13
    # Creating the dropdown list
    optionA13 = st.selectbox("Choose an option", A13)

    # Display the selected option
    st.write(f"A13: {optionA13}")

    response['A13'] = optionA13


if __name__=='__main__':
    main()

