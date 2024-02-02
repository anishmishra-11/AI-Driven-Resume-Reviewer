# AI-Driven Resume Reviewer

## Project Overview

Job application processes can be daunting, and resumes play a crucial role in representing individuals to HR professionals. This project aims to provide an application using Google generative AI [GEMINI] to offer feedback and identify missing keywords in resumes.

## Objectives

- Provide an intuitive tool for job seekers to match their resumes with job descriptions.
- Leverage advanced AI technology for analyzing and providing feedback on resumes.
- Offer a user-friendly interface that simplifies the resume review process.

## Features

1. **Resume Upload:** Users can upload their resume in PDF format.
2. **Job Description Input:** Users can paste the job description they are targeting.
3. **AI-Driven Analysis:** Utilizing Gemini AI for detailed analysis of the resume in context with the job description.
4. **Feedback on Different Aspects:**
   - **Resume Review:** General feedback on the resume.
   - **Skills Improvement:** Suggestions for skills enhancement.
   - **Keywords Analysis:** Identification of missing keywords in the resume.
   - **Match Percentage:** A percentage score indicating how well the resume matches the job description.
   
## Usage

To explore the AI-Driven Resume Reviewer and Analyzer, either access the [live demo here](https://huggingface.co/spaces/anishmishra11/ai) Use Dark Mode for better User Experience.
or follow these steps for local deployment:

1. Install all the requirements as per requirements.txt
2. Generate your api key of google gemini pro vision and store it in a .env file.
3. Clone the repository to your local machine
4. Run the app.py file using Streamlit in dark mode.

## Technologies Used

- Python: The primary programming language used for backend development.
- Google Generative AI (Gemini Pro Vision): For processing and analyzing the resume content.
- PDF2Image: For handling PDF file conversions and image processing.
- Streamlit: For creating the web application interface.
- Advanced CSS : For styling the web application UI.

## Challenges Faced

- Integration with Gemini AI: Ensuring seamless communication between the Streamlit interface and Gemini AI model.
- PDF Handling: Efficiently converting PDF content to a format suitable for analysis by the AI model.
- User Experience Optimization: Creating an intuitive and responsive UI.
- Enhanced Error Handling: Improve the system's robustness in handling various file formats and user inputs.

## Conclusion

The Resume Reviewer web application stands as a significant tool in bridging the gap between job seekers and their ideal job roles. By harnessing the power of AI, it provides valuable insights and recommendations, making it a pivotal step in enhancing the job application process.

