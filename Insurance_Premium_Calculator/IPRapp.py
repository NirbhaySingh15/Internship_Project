import streamlit as st

#Pre-Define Values
base_premium = 1000
age_factor = 1.2
health_factor = 1.5
coverage_factor = 0.1
gender_factor = {
    "male": 1.2,
    "female": 1.1,
}
smoking_factor = 1.3

#Page layout, Name and icon
st.set_page_config(layout="wide", page_title="Insurance Premium App", page_icon="web-icon.png")

#Header
st.title("INSURANCE PREMIUM CALCULATOR")

#Value from User 
age = st.number_input("Enter your age: ", min_value=0, max_value=85, value=0)
health_status = st.text_input("Enter your health status (good/poor): ").lower()
coverage_amount = st.number_input("Enter the coverage amount: ", value=0)
gender = st.selectbox("Select your gender: ", ("male", "female"))
smoker = st.radio("Are you a smoker?", ("Yes", "No"))

premium = base_premium

#Condition on User data to calculate the premium
if age > 40:
    premium *= age_factor

if health_status == "poor":
    premium *= health_factor

premium += coverage_amount * coverage_factor

gender_factor_multiplier = gender_factor.get(gender, 1.0)
premium *= gender_factor_multiplier

if smoker == "Yes":
    premium *= smoking_factor

#Output by clicking on the button 
if st.button("Calculate Premium"):
    st.write(f'<span style="font-size: 20px;">CALCULATED INSURANCE PREMIUM: ₹ {premium}</span>', unsafe_allow_html=True)
