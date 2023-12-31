import streamlit as st
import pandas

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image('images/Abdul Rehman Arif.jpg')

with col2:
    st.title('Abdul Rehman Arif')
    content = '''
    Hi, My name is Abdul Rehman Arif and I have recently started working as an 
    Trainee Software engineer at CureMD Lahore. It has been quite hard here to 
    learn new things but it is a good experience so far. WOWOWOWOWOWOWOW
    '''
    st.write(content)

st.write(content)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv('data.csv', sep=';')

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f"[Source Code]({row['url']})")
with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f"[Source Code]({row['url']})")
