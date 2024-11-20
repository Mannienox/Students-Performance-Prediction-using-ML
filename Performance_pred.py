import pickle
import streamlit as st 

file = open('model.pkl', 'rb')
model = pickle.load(file)

survey_data = []
survey_form = {
    'Are you in any romantic relationship?': ['0. No', '1. Yes'],
    'How much attendance will you want to have at the end of Real Analysis 1 Class?': ['4: More than 70% of the time', '3: Between 60% and 69% of the time', '2: Between 50% and 59% of the time', '1: Between 40% and 49% of the time', '0: Less than 40% of the time'],
    'How punctual will you be to the Real Analysis 1 class?': ['0: Always arrive late', '1: Frequently arrive late', '2: Occasionally arrive late', '3: Usually arrive on time', '4: Always arrive on time'],
    'How supportive is your family financially?': ['2: Total support (family covers all educational expenses)', '1: Partial support (family covers some educational expenses)', '0: No financial support from family'],
    'Do you like your course of study (mathematics/statistics) when you were?' : ['0. No', '1. Yes'],
    'Do you like Real Analysis 1?': ['0. No', '1. Yes'],
    'How well are you understanding Real Analysis 1 so far?': ['2: Totally (l understood everything or almost everything)', '1. Partially (l understood some parts and crammed some)', '0. No Understanding (l crammed everything)'],
    'What was you grade in the Pre-requisite Course (Sets and Numbers System)?': ['5. A', '4. B', '3. C', '2. D', '1. E', '0. F']}


def main():
    st.title('Real Analysis 1 Performance Prediction')

    #Collecting data from the survey_form dictionary and appending to survey_data
    for question, options in survey_form.items():
        resp = st.selectbox(question, sorted(options))
        try:
            survey_data.append(int(resp[0]))
        except:
            survey_data.append(resp)
    
    # Collecting the rest of the data and appending appropriately.
    attendance = st.slider('On a scale of O - 10, please rate your attendance to Real Analysis 1 tutorials so far', min_value = 0, max_value = 10, step = 1)
    survey_data.append(attendance)
    
    
    age = st.number_input('Age', min_value=16, max_value=70, value = 16)
    survey_data.append(age)

    # Predict button
    predict = st.button('Predict')

    if predict:
        prediction = model.predict([survey_data])
        if prediction == 1:
            st.success('You will PASS. Keep up the momentum!\n\nModel: Random Forest (Prediction Accuracy: 96%)')
        else:
            st.error("You will FAIL if you don't sit up\n\nModel: Random Forest (Prediction Accuracy: 96%)")
    

    

if __name__ == '__main__':
    main()
