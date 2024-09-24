import os
import streamlit as st
from pdfminer.high_level import extract_text
import docx
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from texttable import Texttable
import re
from dotenv import load_dotenv

load_dotenv()

gemini_api_key = os.getenv("API_KEY")

def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)

def extract_text_from_docx(docx_path):
    doc = docx.Document(docx_path)
    full_text = [para.text for para in doc.paragraphs]
    return '\n'.join(full_text)

def extract_text_from_txt(txt_path):
    with open(txt_path, 'r', encoding='utf-8') as file:
        return file.read()

def resume_to_text(file):
    file_extension = os.path.splitext(file.name)[1].lower()
    
    if file_extension == '.pdf':
        resume_text = extract_text_from_pdf(file)
    elif file_extension == '.docx':
        resume_text = extract_text_from_docx(file)
    elif file_extension == '.txt':
        resume_text = extract_text_from_txt(file)
    else:
        st.error("Unsupported file format. Please use PDF, DOCX, or TXT.")
        return None
    return resume_text

st.title('Resume Information Extractor')

uploaded_file = st.file_uploader("Upload a resume (PDF, DOCX, or TXT)", type=['pdf', 'docx', 'txt'])

if uploaded_file:
    with st.spinner('Extracting text from the resume...'):
        resume_text = resume_to_text(uploaded_file)
    
    if resume_text:
        st.write("Extracted Resume Text:")
        st.text_area("Resume Text", resume_text, height=300)
        
       
        llm = ChatGoogleGenerativeAI(api_key=gemini_api_key, model="gemini-pro")

        prompt_message = HumanMessage(
            content=f"Extract the following information from this resume: name, email, phone number, college name, and skills. Here is the resume text and dont send any unwanted special characters:\n\n{resume_text}"
        )

        with st.spinner('Extracting information from the resume...'):
            output = llm.invoke([prompt_message])
        
        extracted_content = output.content

        name, email, phone_number, college_name, skills = None, None, None, None, None
        for line in extracted_content.split('\n'):
            if "Name:" in line and not name:
                name = line.split("Name:")[-1].strip().lstrip('*').strip()
            elif "Email:" in line:
                email = line.split("Email:")[-1].strip().lstrip('*').strip()
            elif "Phone Number:" in line:
                phone_number = line.split("Phone Number:")[-1]
            elif "College Name:" in line and not college_name:
                college_name = line.split("College Name:")[-1].lstrip('*').strip()  
            elif "Skills:" in line:
                skills_section = extracted_content.split("Skills:")[-1].strip()
                skills = '\n'.join([s.lstrip('*').strip() for s in skills_section.split('\n') if s.strip().strip('*')])
        phone_number = phone_number.strip('*').strip()
        

        
        table = Texttable()
        table.set_cols_width([20, 100])
        table.set_cols_dtype(["t", "t"]) 
        table.add_row(["Field", "Information"])
        table.add_row(["Name", name])
        table.add_row(["Email", email])
        table.add_row(["Phone Number", phone_number])
        table.add_row(["College Name", college_name])
        table.add_row(["Skills", skills])

        st.subheader('Extracted Information')
        st.text(table.draw())

else:
    st.info("Please upload a resume to extract information.")
