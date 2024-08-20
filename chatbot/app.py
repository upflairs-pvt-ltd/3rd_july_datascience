from dotenv import load_dotenv
import os 
import google.generativeai as genai 
import streamlit as st
from PIL import Image  
load_dotenv()


API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=API_KEY)

def get_gemini_response(input_message,input_image): 
    model = genai.GenerativeModel("gemini-1.5-flash")
    if input_message != "":
        response = model.generate_content([input_message,input_image])
    else: 
        response = model.generate_content(input_image)
    return response.text 



st.set_page_config(page_title="Gemini base chatbot")
st.header("Gemini LLM Application 🤖👾")

input = st.text_input("Input Prompt : ",key="input")
uploaded_file = st.file_uploader("choose an image : ",type=['jpg','jpeg','png'])

image = ""
if uploaded_file is not None: 
    image =Image.open(uploaded_file)
    st.image(image,caption="uploaded image",use_column_width=True)

submit = st.button("Submit")

if submit: 
    response = get_gemini_response(input_message=input,input_image=image)
    st.subheader("Your response is : ")
    st.write(response) 


