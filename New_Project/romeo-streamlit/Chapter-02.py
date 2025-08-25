import streamlit as st

st.title("Chai Maker App")

if st.button("Make Chai"):
    st.write("Chai is being made...")

add_masala = st.checkbox("Add Masala")
add_milk = st.checkbox("Add Milk")
add_sugar = st.checkbox("Add Sugar")

if add_masala:
    st.write("Masala has been added to your chai.")
if add_milk:
    st.write("Milk has been added to your chai.")
if add_sugar:
    st.write("Sugar has been added to your chai.")

tea_type = st.radio("Select your tea type:", ["Black Tea", "Green Tea", "Herbal Tea"])
st.write(f"You selected: {tea_type}")

flavour = st.selectbox("Choose your flavour:", ["Cardamom", "Ginger", "Lemon", "Mint"])
st.write(f"You chose: {flavour}")

sugar = st.slider("Select sugar level (spoon):", 0, 10, 5)
st.write(f"You selected sugar level: {sugar}")

cups = st.number_input("How many cups of chai do you want?", min_value=1, max_value=10, value=1)
st.write(f"You want {cups} cup(s) of chai.")

name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello {name}, your chai is being prepared!")

dob = st.date_input("Select your date of birth:")
st.write(f"Your date of birth is: {dob}")


