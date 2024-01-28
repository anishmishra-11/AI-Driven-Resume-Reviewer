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
        # Convert the pdf to image
        images = pdf2image.convert_from_bytes(uploaded_file.read())

        # Take the first page for simplicity, or loop through images for all pages
        first_page = images[0]

        # Convert to bytes
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

# Streamlit App
st.set_page_config(page_title="Resume Reviewer")

# Applying custom CSS
with open('style.css') as f :
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.header("AI-Driven Resume Review & Analysis")
st.subheader('Enhance Your Resume with AI Insights, ensuring it surpasses ATS screening in your job search.')

input_text = st.text_area("Paste Job Description here : ", key="input", placeholder="Enter Here")
uploaded_file = st.file_uploader("Upload your Resume Here (in PDF Format Only) :", type=["pdf"])

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")

# Used to give same space to buttons of second row.
col1, col2, col3 = st.columns([1,1,1])
with col1:
    submit1 = st.button("Tell me about the Resume")
with col2:
    submit2 = st.button("Check JD Match Percentage")
with col3:
    submit3 = st.button("How to Improve my Skills")

# Used to give same space to buttons of second row.
col1, col2, col3 = st.columns([1,1,1])
with col1:
    submit4 = st.button("Proofread & Edit Resume")
with col2:
    submit5 = st.button("ATS Compatibility Check")
with col3:
    submit6 = st.button("Measure SMART Impact")

# Used to align the text input and serach button in same row.
col4, col5 = st.columns([6.2,1])
with col4:
    query_text = st.text_input("Ask your Custom Questions : ", key="input_question", placeholder="Type Here")

with col5:
    search_btn = st.button("Search", type="primary")

#Prompts for Results.
input_prompt1 = """
 You are an experienced Human Resource Manager with tech experience in the field of Software Development,
 Data Science, Full Stack Web Development, DEVOPS, Data Analyst and Data Engineering roles. Your task is to 
 review the provided resume against the job description for these profiles. Please share your professional 
 evaluation on whether the candidate's profile aligns with the role. Highlight the strengths and weaknesses 
 of the applicant in relation to the specified job requirements.
"""

input_prompt2 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of Software Development,
Data Science, Full Stack Web Development, DEVOPS, Data Analyst, Data Engineering and deep ATS functionality. 
Your task is to evaluate the resume against the provided job description. Give me the percentage of match if the 
resume matches the job description. First the output should come as percentage and then keywords missing and in 
last final thoughts. All of these in paragraphs.
"""

input_prompt3 = """
You are an experienced Human Resource Manager with tech experience in the field of Software Development,
Data Science, Full Stack Web Development, DEVOPS, Data Analyst and Data Engineering roles. 
Please share your professional evaluation on how the candidate can improve his/her profile for the given role. 
Highlight the areas of improvement for the applicant with corresponding to given resume and in relation to 
the specified job requirements.
"""

input_prompt4 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of Software Development,
Data Science, Full Stack Web Development, DEVOPS, Data Analyst, Data Engineering and deep ATS functionality. 
Your task is to find any spelling errors, typos and formatting issues mistakes in the resume. Also, Give me 
highlights about the sentence structure used in the resume and if it requires any changes. First the output 
should come about spelling errors and then scope of improvements in the sentences used in resume and at last 
final thoughts. Don't find errors in given prompts, use only resume. List all the things in points. 
"""

input_prompt5 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of Software Development,
Data Science, Full Stack Web Development, DEVOPS, Data Analyst, Data Engineering and deep ATS functionality.  
Your task is to evaluate the formatting and structure of the given resume. Highlight any potential issues that 
might hinder ATS readability. Provide recommendations in well structured paragraphs for a clean and well-organized
layout to ensure optimal parsing by Applicant Tracking Systems. Evaluate the overall compatibility of the given
resume with common ATS platforms. Check for elements that might hinder parsing, and ensure adherence to ATS 
best practices. Provide feedback on optimizing the given resume to enhance its compatibility with Applicant 
Tracking Systems.
"""

input_prompt6 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of Software Development,
Data Science, Full Stack Web Development, DEVOPS, Data Analyst, Data Engineering and deep ATS functionality. 
Your task is to determine that did the uploaded resume effectively showcase accomplishments and quantify 
the impact? Were the achievements specific, measurable, achievable, relevant, and time-bound (SMART)? Give
detailed feedback(in points) on areas for improvement for future job searches. Give constructive criticism and 
an opportunity to learn from the experience.
"""

if submit1:#if button1 is clicked.
    if uploaded_file is not None: # To check if PDF is uploaded or not.
        pdf_content=input_pdf_setup(uploaded_file)
        with st.spinner("Analyzing Your Resume"): # This line is used to implement spinner.
            response=get_gemini_response(input_prompt1,pdf_content,input_text)
            st.subheader("The Repsonse is")
            st.write(response)
    else:
        st.write("Please upload the resume")

elif submit2:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        with st.spinner("Analyzing Your Resume"):
            response=get_gemini_response(input_prompt2,pdf_content,input_text)
            st.subheader("The Repsonse is")
            st.write(response)
    else:
        st.write("Please upload the resume")

elif submit3:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        with st.spinner("Analyzing Your Resume"):
            response=get_gemini_response(input_prompt3,pdf_content,input_text)
            st.subheader("The Repsonse is")
            st.write(response)
    else:
        st.write("Please upload the resume")

elif submit4:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        with st.spinner("Analyzing Your Resume"):
            response=get_gemini_response(input_prompt4,pdf_content,input_text)
            st.subheader("The Repsonse is")
            st.write(response)
    else:
        st.write("Please upload the resume")

elif submit5:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        with st.spinner("Analyzing Your Resume"):
            response=get_gemini_response(input_prompt5,pdf_content,input_text)
            st.subheader("The Repsonse is")
            st.write(response)
    else:
        st.write("Please upload the resume")

elif submit6:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        with st.spinner("Analyzing Your Resume"):
            response=get_gemini_response(input_prompt6,pdf_content,input_text)
            st.subheader("The Repsonse is")
            st.write(response)
    else:
        st.write("Please upload the resume")

elif search_btn:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        with st.spinner("Analyzing Your Resume"):
            response=get_gemini_response(query_text,pdf_content,input_text)
            st.subheader("The Repsonse is")
            st.write(response)
    else:
        st.write("Please upload the resume")

st.markdown("---")
st.caption("Resume Reviewer - Make Job Search Easier")
st.caption("Made with :orange_heart: - By Anish")
