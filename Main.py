import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Title and introduction
st.title('Airline Passenger Satisfaction Prediction App')
st.write('Please fill out the details below to predict passenger satisfaction and see a graph based on your input.')

# Sidebar for user input
with st.sidebar:
    st.subheader('Customer Information')

    # Form for user input
    with st.form(key='input_form'):
        # Selectbox for Customer Type
        custype = st.selectbox('Customer Type:', ['First-time', 'Returning'])

        # Slider for Age
        age = st.slider('Age:', 0, 120, 30)

        # Selectbox for Type of Travel
        travel_type = st.selectbox('Type of Travel:', ['Business', 'Personal'])

        # Slider for Flight Distance
        flight_distance = st.slider('Flight Distance (in km):', 0, 10000, 500)

        # Rating sliders for services
        st.subheader('Rate the services (0-5):')

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
        inflight_service = st.slider('Inflight service:', 0, 5, 3)
        cleanliness = st.slider('Cleanliness:', 0, 5, 3)

        # Sliders for delays
        st.subheader('Delays (in minutes):')

        departure_delay = st.slider('Departure Delay:', 0, 180, 10)
        arrival_delay = st.slider('Arrival Delay:', 0, 180, 10)

        # Submit button
        submit_button = st.form_submit_button(label='Submit')

# Main area: Display the DataFrame and plot
if submit_button:
    # Create a DataFrame for the graph
    data = pd.DataFrame({
        'Service': [
            'Inflight wifi', 'Departure/Arrival time', 'Ease of Online booking', 
            'Gate location', 'Food and drink', 'Online boarding', 'Seat comfort', 
            'Inflight entertainment', 'On-board service', 'Leg room service', 
            'Baggage handling', 'Checkin service', 'Inflight service', 'Cleanliness'
        ],
        'Rating': [
            inflight_wifi, departure_arrival_time, ease_online_booking, 
            gate_location, food_drink, online_boarding, seat_comfort, 
            inflight_entertainment, onboard_service, leg_room_service, 
            baggage_handling, checkin_service, inflight_service, cleanliness
        ]
    })

    # Display the DataFrame in the main area
    st.subheader('Customer Ratings Data')
    st.write(data)

    # Create a plot for the graph
    fig, ax = plt.subplots()
    ax.barh(data['Service'], data['Rating'], color='skyblue')
    ax.set_xlabel('Rating')
    ax.set_title('Service Ratings')

    # Display the plot in the main area
    st.pyplot(fig)
