import streamlit as st
from datetime import date

st.title("🎂 Age Calculator")

# 1. Input birth date
birth_date = st.date_input("Enter your Birth Date",min_value=date(1900, 1, 1), max_value=date.today(), key="birth_date" )

# 2. Input or auto-set current date
use_today = st.checkbox("Use today's date as current date", value=True)

if use_today:
    current_date = date.today()
else:
    current_date = st.date_input("Enter Current Date", key="cur_date")

# 3. Calculate age if both dates are selected
if birth_date and current_date:
    if birth_date > current_date:
        st.error("Birth date cannot be in the future!")
    else:
        age_years = current_date.year - birth_date.year - (
            (current_date.month, current_date.day) < (birth_date.month, birth_date.day)
        )

        # 4. Output
        st.success(f"🎉 You are {age_years} years old.")
