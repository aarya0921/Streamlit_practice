import streamlit as st
import requests

st.set_page_config(page_title="Currency Converter", page_icon=":currency_exchange:", layout="centered" )
st.title("Currency Converter")

Amt_INR = st.number_input("Enter the Amount in INR", min_value=1, step=1)
currency=st.selectbox("Select the Currency", ["USD", "EUR", "GBP", "JPY", "DZD", "CAD", "BIF", "CNY", "SEK", "NZD"])


if st.button("Convert"):
    url="https://api.exchangerate-api.com/v4/latest/INR"
    response=requests.get(url)

    if response.status_code == 200:
        data = response.json()
        rate = data["rates"][currency]
        converted = rate * Amt_INR
        st.success(f"{Amt_INR} INR = {converted:.2f} {currency}")
    else:
        st.error("Failed to fetch conversion rate")    