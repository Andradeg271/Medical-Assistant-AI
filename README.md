# Medical AI Assistant

This project is an intelligent assistant designed to help with medical data interpretation and early health analysis. It currently includes two main components:

## Features

### Blood Test Analyzer

Automatically interprets blood test results and provides feedback based on standard medical reference values. It identifies abnormal indicators and highlights possible concerns for further medical attention. This module uses a dedicated machine learning model (`btest`) trained with synthetic medical data generated using AI. The model evaluates indicators such as hemoglobin, hematocrit, WBC, platelets, and others to provide condition suggestions.

### Symptom Analyzer

Processes user-provided symptoms and uses a separate machine learning model (`symptoms`) to suggest possible related conditions.  
This model was trained on a large dataset of **over 6,000 synthetic records**, created using AI, ensuring a broad and representative range of symptom combinations and medical conditions.

## Try the App Online

You can access the app live through Streamlit:

👉 [Launch the app on Streamlit](https://medical-assistant-ai.streamlit.app/)

## Future Plans

In future versions, the system will include a personalized risk calculator for common chronic diseases such as heart attack, stroke, and type 2 diabetes.

## How to Use

1. Input your blood test data or list of symptoms.
2. The system processes the input using trained models.
3. You receive an interpretation and possible condition suggestions.

## Disclaimer

This tool is for educational and informational purposes only and does not replace professional medical advice, diagnosis, or treatment.
