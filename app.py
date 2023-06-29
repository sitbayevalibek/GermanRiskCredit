import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open('C:/Users/dizda/risk/deploy/rf_class.sav', 'rb'))


# creating a function for Prediction
def diabetes_prediction(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshaped)
    if prediction[0] == 0:
        return 'Bad'
    else:
        return 'Good'


def main():
    # giving a title
    st.title('Risk Credit Prediction Web App')
    st.title('Enter numeric data only!. Use examples.')

    # getting the input data from the user
    Age = st.text_input('Age (example >>>	19-75)')
    Sex = st.text_input('Sex (example >>> male=1 female=0)')
    Job = st.text_input('Job (example >>> 2, 1, 3, 0)')
    Housing = st.text_input('Housing (example >>> own=3, free=2, rent=1)')
    Saving_accounts = st.text_input('Saving accounts (example >>> moderate=1, little=0, quite rich=3, rich=2)')
    Checking_account = st.text_input('Checking account (example >>> little=1, moderate=2, rich=3)')
    Credit_amount = st.text_input('Credit amount (example >>> 100-20 000 (Deutsch Mark))')
    Duration = st.text_input('Duration (example >>> 4-60 (month))')
    Purpose = st.text_input('Purpose (example >>> radio/TV = 0, education = 1, furniture/equipment = 2, car = 3, business = 4,domestic_appliances = 5, repairs = 6, vacation/others = 7)')

    # code for Prediction
    risk = ''

    # creating a button for Prediction
    if st.button('Submit'):
        risk = diabetes_prediction([Age, Sex, Job, Housing, Saving_accounts, Checking_account, Credit_amount, Duration, Purpose])

    st.success(risk)


if __name__ == '__main__':
    main()
