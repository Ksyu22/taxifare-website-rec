import streamlit as st

import requests

'''
# TaxiFareModel front
'''

with st.form(key='params_for_api'):

    pickup_date = st.date_input('pickup date')
    pickup_time = st.time_input('pickup time')
    pickup_datetime = f'{pickup_date} {pickup_time}'

    pickup_longitude = st.number_input('pickup longitude',value=40.7783468743)
    pickup_latitude = st.number_input('pickup latitude',value=40.7783468743)
    dropoff_longitude = st.number_input('dropoff longitude',value=40.7783468743)
    dropoff_latitude = st.number_input('dropoff latitude',value=40.7783468743)
    passenger_count = st.number_input('passenger number',value=2)

    st.form_submit_button('Lets have a ride')


values = dict(pickup_datetime=pickup_datetime,  # 2014-07-06 19:18:00
                pickup_longitude=pickup_longitude,    # -73.950655
                pickup_latitude=pickup_latitude,     # 40.783282
                dropoff_longitude=dropoff_longitude,   # -73.984365
                dropoff_latitude=dropoff_latitude,    # 40.769802
                passenger_count=passenger_count)


url = st.secrets['wagon_cab_api_url']

if url:

    response = requests.get(url, params=values)
    prediction = response.json()

    pred = prediction['taxifare']

    st.header(f'You fare is {round(pred)}')
