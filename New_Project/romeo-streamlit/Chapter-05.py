import streamlit as st
import requests

st.title("Live Currency Converter")
amount = st.number_input("Enter amount in INR", min_value=1)
target_currency = st.selectbox("Select target currency", ["USD", "EUR", "GBP"])

if st.button("Convert"):
    url = "https://api.exchangerate-api.com/v4/latest/INR"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        rates = data["rates"]
        
        if target_currency in rates:
            converted_amount = amount * rates[target_currency] 
            st.success(f"{amount} INR is equal to {converted_amount:.2f} {target_currency}")
        else:
            st.error("Currency not found.")
      