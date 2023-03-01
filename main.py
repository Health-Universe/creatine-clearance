import streamlit as st

# Define the Cockcroft-Gault Equation
def cockcroft_gault(weight, serum_creatinine, age, gender):
    if gender == "Male":
        constant = 1
    else:
        constant = 0.85

    creatinine_clearance = ((140 - age) * weight * constant) / (72 * serum_creatinine)

    # Cockcroft-Gault CrCl, mL/min = (140 – age) × (weight, kg) × (0.85 if female) / (72 × Cr, mg/dL)

    return creatinine_clearance

# Create a Streamlit app

st.title("Creatinine Clearance Calculator")

gender = st.selectbox("Gender", ("Male", "Female"))
age = st.number_input("Age (years)", min_value=1, max_value=150, value=50, step=1)
weight = st.number_input("Weight (kg)", min_value=1.0, max_value=300.0, value=70.0, step=0.1)
serum_creatinine = st.number_input("Serum Creatinine (umol/L)", min_value=0.1, max_value=1500.0, value=60.0, step=0.1)

if st.button("Calculate"):
    result = cockcroft_gault(weight, serum_creatinine, age, gender)
    st.write(f"Creatinine Clearance: {result:.2f} ml/min")
