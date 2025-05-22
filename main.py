# ==== Import Statements ==== #

import streamlit as st
from processing.interpreters import interpreter_btest, interpreter_sympt
from processing.pdf_generator import generate_pdf
import pandas as pd
import json

# ==== Page configuration ==== #

st.set_page_config(page_title="Medical Assistant AI", layout="centered")


# ==== Initial state ==== #

if "treatment" not in st.session_state:
    st.session_state.treatment = None


# ==== Header ==== #

st.markdown(
    """
    <h1 style='text-align: center; color: #2E86C1;'>🩺 Medical Assistant AI</h1>
    <hr style="border:1px solid #CCC"/>
    """,
    unsafe_allow_html=True
)


# ==== Styling ==== #

st.markdown("""
<style>

/* Title */
.center-text {
    text-align: center;
    font-size: 1.5em;
    margin-bottom: 30px;
}

/* Subheader */
h2 {
    text-align: center;
}

/* Buttons Style */
.stButton > button {
    background-color: #2E86C1;
    color: white;
    padding: 12px 26px;
    border: none;
    border-radius: 10px;
    font-size: 16px;
    margin: 10px 0px;
    width: 56%;
}

/* Alignment */
div.stButton {
    display: flex;
    justify-content: center;
}

</style>
""", unsafe_allow_html=True)




# ==== MAIN PAGE ==== #

def main_menu():
    st.session_state.treatment = None

def s_analyzer_main_page():
    st.session_state.treatment = "Symptoms Main Page"

def s_analyzer_second_page():
    st.session_state.treatment = "Symptoms Second Page"

if st.session_state.treatment is None:
    st.markdown("<div class='center-text'>How can I help you today?</div>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        if st.button("Analyze my Symptoms", icon='🤒', help = "Predicts a disease based on symptoms"):
            st.session_state.treatment = "Symptoms Main Page"
            st.rerun()
        if st.button("Analyze my Blood Test", icon = '🧪', help = "Reads a blood test and gives feedback"):
            st.session_state.treatment = "Blood Test Analyzer"
            st.rerun()




# ==== BLOOD TEST ANALYZER PAGE ==== #

elif st.session_state.treatment == "Blood Test Analyzer":
    st.markdown("<h2 style='text-align: center; font-size: 2.0em;'>Blood Test Analyzer</h2>", unsafe_allow_html=True)


    # ==== Receive file and generate the pdf ==== #

    with st.container(border=True):
        exam = st.file_uploader('Upload your Blood Test (.csv)', type='csv')
        if exam is not None:
            df = pd.read_csv(exam)
            prediction_df = interpreter_btest(df)
            diagnosis = prediction_df['Condition']
            status = prediction_df.drop('Condition', axis=1)
            pdf_bytes = generate_pdf(df, diagnosis, status)


            # ==== Download button ==== #

            st.success("Analysis complete!")
            st.download_button(
                "Download Analysis PDF",
                data=pdf_bytes,
                file_name='blood_test_analysis.pdf',
                mime='application/pdf'
            )


    # ==== Back to menu button ==== #

    if st.button("Back to menu", on_click=main_menu, icon = '⬅️'):
        st.rerun()




# ==== SYMPTOMS ANALYZER MAIN PAGE ==== #

elif st.session_state.treatment == "Symptoms Main Page":
    st.markdown("<h2 style='text-align: center; font-size: 2.0em;'>Symptoms Analyzer</h2>", unsafe_allow_html=True)


    # ==== Dctionary with user inputs ==== #

    with st.expander('Please answer the following questions:'):
        st.session_state.input_dataframe = {
            'Sex': st.selectbox("Sex", ['Male', 'Female']),
            'Age': st.number_input("Age", min_value=0, max_value=120, step=1),
            'Season': st.selectbox("Season", ['Winter', 'Spring', 'Summer', 'Fall']),
            'Exercise': st.selectbox("Exercise", ['Yes', 'No']),
            'HealthyEating': st.selectbox("Healthy Eating", ['Yes', 'No']),
            'ExcessiveDrinking': st.selectbox("Excessive Drinking", ['Yes', 'No']),
            'Smoking': st.selectbox("Smoking", ['Yes', 'No']),
            'BMI': st.selectbox("Body Type (BMI Category)", ['Underweight', 'Normal', 'Overweight', 'Obese']),
            'IndividualHistory': st.text_input("Individual History (e.g., Asthma)"),
            'FamilyHistory': st.text_input("Family History (e.g., Diabetes)"),
        }


    # ==== Back to menu/Next page button ==== #

    if st.button("Next", on_click=s_analyzer_second_page, icon ='➡️'):
        st.rerun()

    if st.button("Back to menu", on_click=main_menu, icon = '⬅️'):
        st.rerun()




# ==== SYMPTOMS ANALYZER SECOND PAGE ==== #

elif st.session_state.treatment == "Symptoms Second Page":
    st.markdown("<h2 style='text-align: center; font-size: 2.0em;'>Symptoms Analyzer</h2>", unsafe_allow_html=True)


    # ==== Load symptoms list and add to multiselect widget ==== #

    with open("model/models_datasets/symptom_list.json", "r", encoding="utf-8") as f:
        symptom_list = json.load(f)

    st.session_state.selected_symptoms = st.multiselect("Select your symptoms", symptom_list)


    # ==== Add symptoms to dictionary ==== #

    for symptom in symptom_list:
        st.session_state.input_dataframe[symptom] = 'Yes' if symptom in st.session_state.selected_symptoms else 'No'


    # ==== Create dataframe and predict button ==== #

    symp_dataframe = pd.DataFrame([st.session_state.input_dataframe])

    button_predict = st.button("Predict Disease")

    if button_predict:
        if st.session_state.selected_symptoms:
            disease = interpreter_sympt(symp_dataframe)
            disease_text = disease[0]
            st.success(f"You have been diagnosed with **{disease_text}**.")
        else:
            st.warning("You have not selected your symptoms")


    # ==== Back button ==== #

    if st.button("Back", on_click=s_analyzer_main_page,icon="⬅️"):
        st.rerun()

  





            
