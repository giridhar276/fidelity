import streamlit as st

st.number_input('Pick a number', 0, 10)
st.text_input('Email adress')  # typo preserved like the screenshot
st.date_input('Travelling date')
st.time_input('School time')
st.text_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('Choose your favourite color')
