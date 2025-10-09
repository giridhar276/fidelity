import streamlit as st

container = st.container()
container.write("This is written inside the container")
st.write("This is written outside the container")
