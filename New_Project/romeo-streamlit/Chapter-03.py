import streamlit as st

st.title("Tea Lover Poll")

col1, col2 = st.columns(2)

with col1:
    st.header("Tea Features")
    st.image("https://media.istockphoto.com/id/187691623/photo/one-letter-from-chrome-alphabet-set.jpg?s=1024x1024&w=is&k=20&c=Tyj78ch0jxJqS6_2lLpMimq0SvtddRS1eZr-ANPnM-Q=", width=100)
    vote1 = st.button("Vote C++ Features")

with col2:
    st.header("Coffee Community")
    st.image("https://media.istockphoto.com/id/155158351/photo/polished-silver-alphabet-c-on-white-background.jpg?s=1024x1024&w=is&k=20&c=XCcIs--Wb6U33V9ND52HKvHNWrtWfrgDyADyBmKAGNQ=", width=110)
    vote2 = st.button("Vote Coffee Community")

if vote1:
    st.success("Thanks for voting Tea Features!")
elif vote2:
    st.success("Thanks for voting Coffee Community!")

name = st.sidebar.text_input("Enter your name:") 
tea = st.sidebar.selectbox("Select your favorite tea:", ["Masala Chai", "Green Tea", "Black Tea", "Herbal Tea"])

st.write(f"Hello {name}, you selected {tea} as your favorite tea!") 

with st.expander("Show Tea Making Instructions"):
    st.write("""
    1. Boil water.
    2. Add tea leaves.
    3. Steep for 5 minutes.
    4. Strain and serve.
    """)

st.markdown("## Enjoy your tea!")
st.markdown("#### Share your thoughts on tea and coffee in the comments below!")
