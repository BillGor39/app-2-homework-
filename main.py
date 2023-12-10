import streamlit as st
import pandas

st.set_page_config(layout="wide")

#add header and some other text
st.header("The Best Company")
content1="""Determining the "best" company can be subjective and depends on 
various factors such as industry, values, financial performance, and more. 
However, I can provide descriptions of a few companies that are often considered 
among the best in their respective fields as of my last knowledge update 
in January 2022. Please note that the status of companies can change, so it's a 
good idea to check the latest information.
"""
st.write(content1)

st.header("Our Team")

df = pandas.read_csv("data.csv", sep=",")
# prepare columns
col1, col2, col3 = st.columns(3)

# add content in each column
with col1:
    for index, row in df[0:4].iterrows():
        name = f"{row["first name"]} {row["last name"]}".title()
        st.header(name)
        st.write(row["role"])
        st.image(f"images/{row["image"]}")

with col2:
    for index, row in df[4:8].iterrows():
        name = f"{row["first name"]} {row["last name"]}".title()
        st.header(name)
        st.write(row["role"])
        st.image(f"images/{row["image"]}")

with col3:
    for index, row in df[8:].iterrows():
        name = f"{row["first name"]} {row["last name"]}".title()
        st.header(name)
        st.write(row["role"])
        st.image(f"images/{row["image"]}")




