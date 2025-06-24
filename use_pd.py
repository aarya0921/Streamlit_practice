import streamlit as st
import pandas as pd
st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")
st.title("Sales Dashboard")

df = pd.read_csv(r"C:\Users\User\Desktop\sttreamlit\sales.csv")
st.write("Sales Data", df)

st.subheader("Sales Summary")
st.write(df.describe())

cities = df["City"].unique()
selected_city = st.selectbox("Filter by cities", cities)
filtered_data = df[df["City"] == selected_city]
st.dataframe(filtered_data)