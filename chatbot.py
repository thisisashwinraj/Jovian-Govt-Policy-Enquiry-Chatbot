# Import necessary libraries
import streamlit as st
import google.cloud.dialogflow_v2 as dialogflow
import os
from google.oauth2.service_account import Credentials

# Dialogflow credentials
credentials = Credentials.from_service_account_file(
    'service_account.json')

# Dialogflow project ID
project_id = 'dakshinamobiles-qpud'

# Create a session client
session_client = dialogflow.SessionsClient(credentials=credentials)

# Define the Streamlit app
def chatbot():
    # Get user input
    user_input = st.text_input('Ask a question')

    # Send user input to Dialogflow and receive response
    if user_input:
        session = session_client.session_path(project_id, "unique_session_id")
        text_input = dialogflow.types.TextInput(text=user_input, language_code="en-US")
        query_input = dialogflow.types.QueryInput(text=text_input)
        response = session_client.detect_intent(session=session, query_input=query_input)
        answer = response.query_result.fulfillment_text

        # Display response in the chatbot interface
        st.write(answer)

# Run the Streamlit app
if __name__ == '__main__':
    chatbot()
