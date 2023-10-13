import streamlit as st

#Pre-Define Values
base_premium = 1000
age_factor = {
    (0,17):0,
    (18,35):0.2,
    (36,45):0.25,
    (46,55):0.3,
    (56,60):0.5,
    (61,99):0.9
}
health_factor = {
    'Excelent':1,
    'Good':1.5
    }
coverage_factor = 0.1
gender_factor = {
    "Male": 1.2,
    "Female": 1.1,
    "Prefer not to say":1.3
}
smoking_factor = 1.3

#Page layout and Name
st.set_page_config(layout="wide", page_title="Insurance Premium App", page_icon="web-icon.png")

#Header
st.title("INSURANCE PREMIUM CALCULATOR")

#Value from User 
name = st.text_input("PLEASE PROVIDE YOUR NAME: ",placeholder='Enter your Name')
age = st.number_input("PLEASE PROVIDE YOUR AGE: ", min_value=0, max_value=85, value=24)
gender = st.selectbox("PLEASE PROVIDE YOUR GENDER: ", ("Male", "Female","Prefer not to say"))
coverage_amount = st.number_input("PLEASE PROVIDE COVERAGE AMOUNT: ",min_value=50000, value=50000)
health_status = st.selectbox("PLEASE PROVIDE YOUR HEALTH STATUS: ", ('Excelent','Good','Poor'))
smoker = st.radio("ARE YOU A SMOKER?", ("YES", "NO"))

premium = base_premium

#Condition on User data to calculate the premium
for age_r, factor in age_factor.items():
    age_low,age_high=age_r
    if age_low <= age <= age_high:
        premium *= factor

for hlt,h_fact in health_factor.items():
    if health_status == hlt:
        premium *= h_fact

premium += coverage_amount * coverage_factor

gender_factor_multiplier = gender_factor.get(gender)
premium *= gender_factor_multiplier

if smoker == "YES":
    premium *= smoking_factor

#Output by clicking on the button 
if st.button("Calculate Premium"):
    if health_status == 'Poor':
        st.write(f'<span style="font-size: 40px; color: red;">SORRY!!! YOUR HEALTH STATUS IS {health_status.upper()} TRY AFTER 6 MONTHS</span>', unsafe_allow_html=True)
    else:
        st.write(f'<span style="font-size: 40px; color: orange;">CALCULATED INSURANCE PREMIUM: ₹ {premium:.2f}</span>', unsafe_allow_html=True)
        st.write(f'<span style="font-size: 30px; color: green; ">CUSTOMER DETAIL<BR></span><span style="font-size: 20px;"><u> Name</u>:&nbsp; <b> {name.upper()}</b><br> <u>Age</u>:&nbsp; <b> {age}</b> <br> <u>Gender</u>:&nbsp; <b>{gender.upper()}</b> <br> <u>Coverage Amount</u>: &nbsp; <b>{coverage_amount}</b> <br> <u> Premium</u>: &nbsp;<b>₹ {premium:.2f}</b> <br><u> Health</u>: &nbsp;<b>{health_status.upper()}</b> <br> <u> Smoker</u>: &nbsp;<b>{smoker}</b></span>', unsafe_allow_html=True)
