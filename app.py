import numpy as np
import pickle
import streamlit as st
import sklearn
# loading the saved model
loaded_model = pickle.load(open('rf_class.sav', 'rb'))


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
    st.markdown('<h1 style="font-size:large;">Enter numeric data only!. Use examples.</h1>', unsafe_allow_html=True)

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

    with st.container():
        st.success(churn)
        st.markdown('<h1 style="font-size:large;">My Social Links</h1>', unsafe_allow_html=True)
        st.markdown('[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?&style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sitbayevalibek)')
        st.markdown('[![GitHub](https://img.shields.io/badge/GitHub-%2312100E.svg?&style=flat-square&logo=github&logoColor=white)](https://github.com/sitbayevalibek)')
        st.markdown('[![Kaggle](https://img.shields.io/badge/Kaggle-%2320BEFF.svg?&style=flat-square&logo=kaggle&logoColor=white)](https://www.kaggle.com/sitbayevalibek)')


if __name__ == '__main__':
    main()
