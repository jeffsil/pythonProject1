import streamlit as st

st.title("OpenCV Streamlit Demo")
st.header("header")

image = st.file_uploader("Upload an image file")
#st.image(image)
st.text("This is text")
option = st.selectbox("Select Box", ["None", "Filter1", "Filter2"])
#st.text("option is: " +option)
st.write("option is: " +option)
checkbox_value = st.checkbox("Apply Filter")
st.write(checkbox_value)