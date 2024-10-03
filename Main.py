import streamlit as st
import numpy as np
import time
import pickle

# Load the pre-trained model
try:
    with open('xgb_model.pkl', 'rb') as file:
        xgb_model = pickle.load(file)
except Exception as e:
    st.error(f"Error loading model: {e}")

# Set the title background image
title_background_image = """
<style>
h1 {
    background-image: url("https://img.freepik.com/premium-photo/flying-airplane-sky-sunset_225446-13106.jpg");
    background-size: cover;
    background-position: center;  
    background-repeat: no-repeat;
    color: white; /* Change title text color to white */
    padding: 20px; /* Add padding to the title */
    border-radius: 10px; /* Rounded corners for the title background */
    text-align: center; /* Center the title text */
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7); /* Add shadow effect */
}
</style>
"""
st.markdown(title_background_image, unsafe_allow_html=True)

# Input styles for the rest of the app
input_style = """
<style>
div[data-baseweb="base-input"] {
    background-color: transparent !important;
}
[data-testid="stAppViewContainer"] {
    background-color: transparent !important;
}
</style>
"""
st.markdown(input_style, unsafe_allow_html=True)

# Title and introduction
st.title('Airline Passenger Satisfaction Prediction App')
st.write('Please fill out the details to predict passenger satisfaction.')

with st.form(key='input_form'):
    st.subheader('Customer Information')
    # Create two columns for the Customer Information section
    col1, col2 = st.columns(2)

    # Column 1: Customer Information
    with col1:
        custype = st.selectbox('Customer Type:', ['First-time', 'Returning'])
        gender = st.selectbox('Gender:', ['Male', 'Female'])
        age = st.slider('Age:', 0, 120, 30)

    with col2:
        travel_type = st.selectbox('Type of Travel:', ['Business', 'Personal'])
        class_type = st.selectbox('Class:', ['Business', 'Economy', 'Economy Plus'])
        flight_distance = st.slider('Flight Distance (in km):', 0, 10000, 500)

    # Create two columns for the Rate the services section
    st.subheader('Rate the services (0-5):')
    service_col1, service_col2 = st.columns(2)

    with service_col1:
        inflight_wifi = st.slider('Inflight wifi service:', 0, 5, 3)
        departure_arrival_time = st.slider('Departure/Arrival time convenient:', 0, 5, 3)
        ease_online_booking = st.slider('Ease of Online booking:', 0, 5, 3)
        food_drink = st.slider('Food and drink:', 0, 5, 3)
        online_boarding = st.slider('Online boarding:', 0, 5, 3)
        seat_comfort = st.slider('Seat comfort:', 0, 5, 3)

    with service_col2:
        inflight_entertainment = st.slider('Inflight entertainment:', 0, 5, 3)
        onboard_service = st.slider('On-board service:', 0, 5, 3)
        leg_room_service = st.slider('Leg room service:', 0, 5, 3)
        baggage_handling = st.slider('Baggage handling:', 0, 5, 3)
        checkin_service = st.slider('Checkin service:', 0, 5, 3)
        inflight_service = st.slider('Inflight service:', 0, 5, 3)
        cleanliness = st.slider('Cleanliness:', 0, 5, 3)

    # Delay inputs (Below both columns)
    st.subheader('Delays (in minutes):')
    departure_delay = st.slider('Departure Delay:', 0, 180, 10)
    arrival_delay = st.slider('Arrival Delay:', 0, 180, 10)

    submit_button = st.form_submit_button(label='Submit')

# Main area: Display the DataFrame and plot
if submit_button:
    with st.spinner("Processing... Please wait."):
        time.sleep(2)  # Simulate a delay for loading

        # Convert user input into features
        features = np.array([[
            1 if custype == 'Returning' else 0,
            1 if gender == 'Male' else 0,
            age,
            1 if travel_type == 'Business' else 0,
            flight_distance,
            inflight_wifi,
            departure_arrival_time,
            ease_online_booking,
            food_drink,
            online_boarding,
            seat_comfort,
            inflight_entertainment,
            onboard_service,
            leg_room_service,
            baggage_handling,
            checkin_service,
            inflight_service,
            cleanliness,
            departure_delay,
            arrival_delay,
            1 if class_type == 'Business' else (2 if class_type == 'Economy Plus' else 0)
        ]])

        # Calculate average rating
        ratings = [
            inflight_wifi, departure_arrival_time, ease_online_booking, 
            food_drink, online_boarding, seat_comfort, 
            inflight_entertainment, onboard_service, leg_room_service, 
            baggage_handling, checkin_service, inflight_service, cleanliness
        ]
        average_rating = np.mean(ratings)

        # Determine satisfaction based on average rating
        threshold = 4.0
        customer_satisfaction = 'Satisfied' if average_rating >= threshold else 'Neutral or Dissatisfied'

        # Display the result in a styled box
        st.markdown(f"""
        <div style='background-color: white; 
                    border-radius: 10px; 
                    padding: 20px; 
                    backdrop-filter: blur(20px); 
                    box-shadow: 0 0 20px rgba(0, 0, 0, 0.5);'>
            <h3 style='color: black;'>Prediction Results</h3>
            <h4 style='color: #007BFF;'>Customer Satisfaction: {customer_satisfaction} </h4>
            <h4 style='color: #007BFF;'>Average Rating: {average_rating:.2f}</h4> 
        </div>
        """, unsafe_allow_html=True)
