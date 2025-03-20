import streamlit as st
import pandas as pd

def convert_units(category, from_unit, to_unit, value):
    conversion_factors = {
        "Length": {"Metre": 1, "Centimetre": 100, "Kilometre": 0.001, "Inch": 39.3701, "Foot": 3.28084},
        "Weight": {"Kilogram": 1, "Gram": 1000, "Pound": 2.20462, "Ounce": 35.274},
        "Temperature": {
            "Celsius": lambda c: c, 
            "Fahrenheit": lambda c: (c * 9/5) + 32, 
            "Kelvin": lambda c: c + 273.15
        }
    }
    
    if category == "Temperature":
        return conversion_factors[category][to_unit](value)
    else:
        return value * (conversion_factors[category][to_unit] / conversion_factors[category][from_unit])

st.title("🔢 Google Unit Converter")
st.markdown("Build a Google-style Unit Converter using Python & Streamlit")

conversion_factors = {
    "Length": {"Metre": 1, "Centimetre": 100, "Kilometre": 0.001, "Inch": 39.3701, "Foot": 3.28084},
    "Weight": {"Kilogram": 1, "Gram": 1000, "Pound": 2.20462, "Ounce": 35.274},
    "Temperature": {
        "Celsius": lambda c: c, 
        "Fahrenheit": lambda c: (c * 9/5) + 32, 
        "Kelvin": lambda c: c + 273.15
    }
}

category = st.selectbox("Category", list(conversion_factors.keys()))
units = list(conversion_factors[category].keys())

col1, col2, col3 = st.columns([3, 1, 3])

with col1:
    value = st.number_input("", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From", units, key="from_unit")

with col2:
    st.markdown("# =")

with col3:
    to_unit = st.selectbox("To", units, key="to_unit")
    result = convert_units(category, from_unit, to_unit, value)
    st.markdown(f"# {result:.2f}")

formula_text = f"Formula: Convert {from_unit} to {to_unit}" 
st.markdown(f"**🟡 Formula** {formula_text}")
