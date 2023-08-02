import streamlit as st
import pandas

st.set_page_config(layout='wide')

st.header('The Best Company')

texttowrite = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur eu semper justo. Fusce dapibus dapibus dolor, sed fringilla ligula convallis quis. Nulla risus enim, malesuada id sodales tempus, faucibus fringilla nunc. Nunc pretium et urna sed consequat. Integer porta, neque sit amet congue bibendum, orci ipsum sollicitudin mi, quis consectetur nibh nisi consectetur elit. Donec lacinia sem sem, et convallis nibh facilisis et. Nunc dignissim massa luctus quam vestibulum congue et vel elit.
"""

st.markdown(texttowrite)

st.subheader('Our Team')

col1, col2, col3 = st.columns(3)

df = pandas.read_csv('data.csv')

with col1:
    for index, rows in df[:4].iterrows():
        st.subheader(rows['first name'].capitalize() + ' ' + rows['last name'].capitalize())
        st.write(rows['role'])
        st.image('images/' + rows['image'])

with col2:
    for index, rows in df[4:8].iterrows():
        st.subheader(rows['first name'].capitalize() + ' ' + rows['last name'].capitalize())
        st.write(rows['role'])
        st.image('images/' + rows['image'])

with col3:
    for index, rows in df[8:].iterrows():
        st.subheader(rows['first name'].capitalize() + ' ' + rows['last name'].capitalize())
        st.write(rows['role'])
        st.image('images/' + rows['image'])
