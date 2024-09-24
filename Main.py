import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Load the saved model
try:
    with open('decision_tree_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    st.write("Model loaded successfully.")
except FileNotFoundError:
    st.error("Model file not found. Please check the file name and path.")
except EOFError:
    st.error("Model file is empty or corrupted.")
except Exception as e:
    st.error(f"An error occurred: {e}")

# Title and introduction
st.title('Airline Passenger Satisfaction Prediction App')
st.write('Please fill out the details below to predict passenger satisfaction.')

# Sidebar for user input
with st.sidebar:
    st.subheader('Customer Information')
    with st.form(key='input_form'):
        # Collect user input
        custype = st.selectbox('Customer Type:', ['First-time', 'Returning'])
        age = st.slider('Age:', 0, 120, 30)
        travel_type = st.selectbox('Type of Travel:', ['Business', 'Personal'])
        flight_distance = st.slider('Flight Distance (in km):', 0, 10000, 500)
        inflight_wifi = st.slider('Inflight wifi service:', 0, 5, 3)
        departure_arrival_time = st.slider('Departure/Arrival time convenient:', 0, 5, 3)
        ease_online_booking = st.slider('Ease of Online booking:', 0, 5, 3)
        gate_location = st.slider('Gate location:', 0, 5, 3)
        food_drink = st.slider('Food and drink:', 0, 5, 3)
        online_boarding = st.slider('Online boarding:', 0, 5, 3)
        seat_comfort = st.slider('Seat comfort:', 0, 5, 3)
        inflight_entertainment = st.slider('Inflight entertainment:', 0, 5, 3)
        onboard_service = st.slider('On-board service:', 0, 5, 3)
        leg_room_service = st.slider('Leg room service:', 0, 5, 3)
        baggage_handling = st.slider('Baggage handling:', 0, 5, 3)
        checkin_service = st.slider('Checkin service:', 0, 5, 3)
        cleanliness = st.slider('Cleanliness:', 0, 5, 3)
        departure_delay = st.slider('Departure Delay:', 0, 180, 10)
        arrival_delay = st.slider('Arrival Delay:', 0, 180, 10)

        # Submit button
        submit_button = st.form_submit_button(label='Submit')

# Make predictions based on user input
if submit_button:
    # Prepare input data
    input_data = pd.DataFrame({
        'Customer Type': [custype],
        'Age': [age],
        'Type of Travel': [travel_type],
        'Flight Distance': [flight_distance],
        'Inflight wifi service': [inflight_wifi],
        'Departure/Arrival time convenient': [departure_arrival_time],
        'Ease of Online booking': [ease_online_booking],
        'Gate location': [gate_location],
        'Food and drink': [food_drink],
        'Online boarding': [online_boarding],
        'Seat comfort': [seat_comfort],
        'Inflight entertainment': [inflight_entertainment],
        'On-board service': [onboard_service],
        'Leg room service': [leg_room_service],
        'Baggage handling': [baggage_handling],
        'Checkin service': [checkin_service],
        'Cleanliness': [cleanliness],
        'Departure Delay': [departure_delay],
        'Arrival Delay': [arrival_delay],
    })

    # Convert categorical variables if necessary
    input_data['Customer Type'] = input_data['Customer Type'].map({'First-time': 0, 'Returning': 1})
    input_data['Type of Travel'] = input_data['Type of Travel'].map({'Business': 0, 'Personal': 1})

    # Initialize prediction variable
    prediction = None

    try:
        # Make prediction
        prediction = model.predict(input_data)
        
        # Display the prediction result
        st.subheader('Prediction Result')
        if prediction[0] == 1:  # Assuming 1 means satisfied
            st.write('Passenger Satisfaction: **Satisfied**')
        else:
            st.write('Passenger Satisfaction: **Not Satisfied**')

    except ValueError as e:
        st.error(f"ValueError: {e}")

    # Debugging output (optional)
    if prediction is not None:
        print("Input Data for Prediction:", input_data)
        print("Prediction Output:", prediction)
