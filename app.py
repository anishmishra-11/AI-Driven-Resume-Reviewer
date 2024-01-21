from dotenv import load_dotenv

load_dotenv()

import base64
import streamlit as st
import os
import io
from PIL import Image
import pdf2image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input,pdf_content,prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input,pdf_content[0],prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        ##Convert the pdf to image
        images = pdf2image.convert_from_bytes(uploaded_file.read())

        # Take the first page for simplicity, or loop through images for all pages
        first_page = images[0]

        #Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode() # encode to base64

            }
        ]

        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

## Streamlit App
st.set_page_config(page_title="ATS Resume Expert")

# Applying custom CSS
with open('style.css') as f :
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.header("ATS Tracking System")
st.subheader('This Application helps you in your Resume Review with help of GEMINI AI [LLM]')

input_text = st.text_area("Paste Job Description here : ", key="input")
uploaded_file = st.file_uploader("Upload your Resume Here (in PDF Format Only)", type=["pdf"])

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")

col1, col2, col3 = st.columns([1,1,1])

with col1:
    submit1 = st.button("Tell me about the Resume")
with col2:
    submit2 = st.button("How can I improve my skills")
with col3:
    submit3 = st.button("Generate Match Percentage")

col1, col2, col3 = st.columns([1,1,1])

with col1:
    submit1 = st.button("To Be Decided.")
with col2:
    submit2 = st.button("Will be Used.")
with col3:
    submit3 = st.button("Here you go")

input_prompt1 = """
 You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description. 
  Please share your professional evaluation on whether the candidate's profile aligns with the role. 
 Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt2 = """
 You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description. 
  Please share your professional evaluation on whether the candidate's profile aligns with the role. 
 Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt3 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and deep ATS functionality, 
your task is to evaluate the resume against the provided job description. Give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
"""

if submit1:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt1,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")

elif submit2:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt2,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")

elif submit3:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt3,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")

st.markdown("---")
st.caption("Resume Expert - Making Job Applications Easier")
st.caption("Made by :orange_heart: - Anish")
